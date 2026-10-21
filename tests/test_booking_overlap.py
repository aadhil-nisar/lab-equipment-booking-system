
"""FR-03 E3 overlapping booking tests."""

from datetime import date, time, timedelta

import pytest

from app.booking_validation import has_booking_conflict
from app.extensions import db
from app.models.booking import Booking
from app.models.equipment import Equipment
from app.models.user import User


def future_date():
    return date.today() + timedelta(days=3)


@pytest.fixture
def student_client(client, app):
    """Create and log in a Student."""
    with app.app_context():
        student = User(
            username="overlapstudent",
            email="overlap@example.com",
            role="Student",
        )
        student.set_password("StrongPass123!")

        db.session.add(student)
        db.session.commit()

    response = client.post(
        "/auth/login",
        data={
            "username": "overlapstudent",
            "password": "StrongPass123!",
        },
    )

    assert response.status_code == 302
    return client


@pytest.fixture
def equipment_ids(app):
    """Create two available equipment items."""
    with app.app_context():
        first = Equipment(
            name="Microscope",
            category="Optics",
            description="First equipment",
            status="Available",
        )

        second = Equipment(
            name="Oscilloscope",
            category="Electronics",
            description="Second equipment",
            status="Available",
        )

        db.session.add_all([first, second])
        db.session.commit()

        return first.id, second.id


def make_existing_booking(
    app,
    equipment_id,
    *,
    booking_date=None,
    start="09:00",
    end="10:00",
    status="Pending",
    student_id=None,
):
    """Insert an existing booking for testing."""
    with app.app_context():
        if student_id is None:
            student_id = db.session.scalar(
                db.select(User.id).where(
                    User.username == "overlapstudent"
                )
            )

        booking = Booking(
            student_id=student_id,
            equipment_id=equipment_id,
            booking_date=booking_date or future_date(),
            start_time=time.fromisoformat(start),
            end_time=time.fromisoformat(end),
            status=status,
        )

        db.session.add(booking)
        db.session.commit()

        return booking.id


def request_data(
    equipment_id,
    *,
    booking_date=None,
    start="09:30",
    end="10:30",
):
    """Create form data for a booking request."""
    return {
        "equipment_id": str(equipment_id),
        "booking_date": (
            booking_date or future_date()
        ).isoformat(),
        "start_time": start,
        "end_time": end,
    }


@pytest.mark.parametrize(
    ("start", "end", "expected"),
    [
        ("08:00", "09:00", False),
        ("08:59", "09:30", True),
        ("09:00", "10:00", True),
        ("09:30", "10:30", True),
        ("09:59", "11:00", True),
        ("10:00", "11:00", False),
        ("08:00", "11:00", True),
    ],
)
def test_overlap_boundaries(
    student_client,
    app,
    equipment_ids,
    start,
    end,
    expected,
):
    equipment_id, _ = equipment_ids

    make_existing_booking(app, equipment_id)

    with app.app_context():
        result = has_booking_conflict(
            equipment_id,
            future_date(),
            time.fromisoformat(start),
            time.fromisoformat(end),
        )

        assert result is expected


@pytest.mark.parametrize(
    ("status", "expected"),
    [
        ("Pending", True),
        ("Approved", True),
        ("Rejected", False),
    ],
)
def test_booking_status_conflict_policy(
    student_client,
    app,
    equipment_ids,
    status,
    expected,
):
    equipment_id, _ = equipment_ids

    make_existing_booking(
        app,
        equipment_id,
        status=status,
    )

    with app.app_context():
        result = has_booking_conflict(
            equipment_id,
            future_date(),
            time(9, 30),
            time(10, 30),
        )

        assert result is expected


def test_different_equipment_does_not_conflict(
    student_client,
    app,
    equipment_ids,
):
    first_id, second_id = equipment_ids

    make_existing_booking(app, first_id)

    with app.app_context():
        assert not has_booking_conflict(
            second_id,
            future_date(),
            time(9, 30),
            time(10, 30),
        )


def test_different_date_does_not_conflict(
    student_client,
    app,
    equipment_ids,
):
    equipment_id, _ = equipment_ids

    make_existing_booking(app, equipment_id)

    with app.app_context():
        assert not has_booking_conflict(
            equipment_id,
            future_date() + timedelta(days=1),
            time(9, 30),
            time(10, 30),
        )


def test_excluding_same_booking_id(
    student_client,
    app,
    equipment_ids,
):
    equipment_id, _ = equipment_ids

    booking_id = make_existing_booking(
        app,
        equipment_id,
    )

    with app.app_context():
        assert not has_booking_conflict(
            equipment_id,
            future_date(),
            time(9, 0),
            time(10, 0),
            exclude_booking_id=booking_id,
        )


def test_form_rejects_overlapping_request(
    student_client,
    app,
    equipment_ids,
):
    equipment_id, _ = equipment_ids

    make_existing_booking(app, equipment_id)

    response = student_client.post(
        "/bookings/new",
        data=request_data(equipment_id),
    )

    assert response.status_code == 400
    assert (
        b"Equipment is already booked"
        in response.data
    )

    with app.app_context():
        assert Booking.query.count() == 1


def test_form_accepts_adjacent_request(
    student_client,
    app,
    equipment_ids,
):
    equipment_id, _ = equipment_ids

    make_existing_booking(app, equipment_id)

    response = student_client.post(
        "/bookings/new",
        data=request_data(
            equipment_id,
            start="10:00",
            end="11:00",
        ),
    )

    assert response.status_code == 302

    with app.app_context():
        assert Booking.query.count() == 2


def test_rejected_booking_does_not_block(
    student_client,
    app,
    equipment_ids,
):
    equipment_id, _ = equipment_ids

    make_existing_booking(
        app,
        equipment_id,
        status="Rejected",
    )

    response = student_client.post(
        "/bookings/new",
        data=request_data(equipment_id),
    )

    assert response.status_code == 302

    with app.app_context():
        assert Booking.query.count() == 2


def test_other_student_booking_blocks_request(
    student_client,
    app,
    equipment_ids,
):
    equipment_id, _ = equipment_ids

    with app.app_context():
        other = User(
            username="student2",
            email="student2@example.com",
            role="Student",
        )
        other.set_password("StrongPass123!")

        db.session.add(other)
        db.session.commit()

        other_id = other.id

    make_existing_booking(
        app,
        equipment_id,
        student_id=other_id,
    )

    response = student_client.post(
        "/bookings/new",
        data=request_data(equipment_id),
    )

    assert response.status_code == 400

    with app.app_context():
        assert Booking.query.count() == 1


def test_approved_booking_blocks_request(
    student_client,
    app,
    equipment_ids,
):
    equipment_id, _ = equipment_ids

    make_existing_booking(
        app,
        equipment_id,
        status="Approved",
    )

    response = student_client.post(
        "/bookings/new",
        data=request_data(equipment_id),
    )

    assert response.status_code == 400

    with app.app_context():
        assert Booking.query.count() == 1
