
from datetime import date, timedelta

import pytest

from app.extensions import db
from app.models.booking import Booking
from app.models.equipment import Equipment
from app.models.user import User


@pytest.fixture
def student_client(client):
    client.post(
        "/auth/register",
        data={
            "username": "student1",
            "email": "student1@example.com",
            "password": "StrongPass123!",
            "confirm_password": "StrongPass123!",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "student1",
            "password": "StrongPass123!",
        },
    )

    assert response.status_code == 302
    return client


@pytest.fixture
def equipment_id(app):
    with app.app_context():
        equipment = Equipment(
            name="Microscope",
            category="Optics",
            description="Laboratory microscope",
            status="Available",
        )

        db.session.add(equipment)
        db.session.commit()

        return equipment.id


def booking_data(equipment_id, **changes):
    data = {
        "equipment_id": str(equipment_id),
        "booking_date": (
            date.today() + timedelta(days=2)
        ).isoformat(),
        "start_time": "09:00",
        "end_time": "10:00",
    }

    data.update(changes)
    return data


def test_anonymous_user_redirected(client):
    response = client.get("/bookings/new")

    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]


def test_student_can_open_form(
    student_client,
    equipment_id,
):
    response = student_client.get("/bookings/new")

    assert response.status_code == 200
    assert b"Microscope" in response.data


def test_student_can_submit_booking(
    student_client,
    app,
    equipment_id,
):
    response = student_client.post(
        "/bookings/new",
        data=booking_data(equipment_id),
    )

    assert response.status_code == 302

    with app.app_context():
        booking = db.session.scalar(db.select(Booking))

        student = User.query.filter_by(
            username="student1"
        ).one()

        assert booking is not None
        assert booking.student_id == student.id
        assert booking.equipment_id == equipment_id
        assert booking.status == "Pending"


def test_student_can_view_bookings(
    student_client,
    equipment_id,
):
    student_client.post(
        "/bookings/new",
        data=booking_data(equipment_id),
    )

    response = student_client.get("/bookings/")

    assert response.status_code == 200
    assert b"Microscope" in response.data
    assert b"Pending" in response.data


def test_student_cannot_view_another_students_booking(
    student_client,
    app,
    equipment_id,
):
    with app.app_context():
        other_student = User(
            username="student2",
            email="student2@example.com",
            role="Student",
        )
        other_student.set_password("StrongPass123!")

        db.session.add(other_student)
        db.session.flush()

        other_booking = Booking(
            student_id=other_student.id,
            equipment_id=equipment_id,
            booking_date=date.today() + timedelta(days=3),
            start_time="14:00",
            end_time="15:00",
            status="Pending",
        )

        # Use Python time objects for database fields.
        from datetime import time

        other_booking.start_time = time(14, 0)
        other_booking.end_time = time(15, 0)

        db.session.add(other_booking)
        db.session.commit()

    response = student_client.get("/bookings/")

    assert response.status_code == 200
    assert b"not submitted any" in response.data


def test_invalid_time_rejected(
    student_client,
    app,
    equipment_id,
):
    response = student_client.post(
        "/bookings/new",
        data=booking_data(
            equipment_id,
            start_time="11:00",
            end_time="10:00",
        ),
    )

    assert response.status_code == 400

    with app.app_context():
        assert Booking.query.count() == 0


def test_out_of_service_equipment_rejected(
    student_client,
    app,
):
    with app.app_context():
        item = Equipment(
            name="Broken Microscope",
            category="Optics",
            description="Needs repair",
            status="Out of service",
        )

        db.session.add(item)
        db.session.commit()
        item_id = item.id

    response = student_client.post(
        "/bookings/new",
        data=booking_data(item_id),
    )

    assert response.status_code == 400

    with app.app_context():
        assert Booking.query.count() == 0


def test_student_cannot_set_approved_status(
    student_client,
    app,
    equipment_id,
):
    data = booking_data(equipment_id)
    data["status"] = "Approved"
    data["student_id"] = "999"

    response = student_client.post(
        "/bookings/new",
        data=data,
    )

    assert response.status_code == 302

    with app.app_context():
        booking = db.session.scalar(db.select(Booking))

        assert booking.status == "Pending"


def test_staff_cannot_submit_booking(
    client,
    app,
    equipment_id,
):
    with app.app_context():
        staff = User(
            username="staff1",
            email="staff1@example.com",
            role="Staff",
        )
        staff.set_password("StrongPass123!")

        db.session.add(staff)
        db.session.commit()

    client.post(
        "/auth/login",
        data={
            "username": "staff1",
            "password": "StrongPass123!",
        },
    )

    response = client.post(
        "/bookings/new",
        data=booking_data(equipment_id),
    )

    assert response.status_code == 403
