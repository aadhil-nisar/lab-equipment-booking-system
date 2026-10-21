"""FR-04 Staff booking decisions and final integration tests."""

from datetime import date, time, timedelta

import pytest

from app.extensions import db
from app.models.booking import Booking
from app.models.equipment import Equipment
from app.models.user import User

PASSWORD = "TestPass123!"


def future_date():
    return date.today() + timedelta(days=3)


@pytest.fixture
def records(app):
    """Create a Staff user, Student, equipment and Pending booking."""
    with app.app_context():
        staff = User(username="decisionstaff", email="staff@example.com", role="Staff")
        student = User(
            username="decisionstudent",
            email="student@example.com",
            role="Student",
        )
        staff.set_password(PASSWORD)
        student.set_password(PASSWORD)
        equipment = Equipment(
            name="Decision Microscope",
            category="Optics",
            description="Staff tests",
            status="Available",
        )
        db.session.add_all([staff, student, equipment])
        db.session.flush()
        booking = Booking(
            student_id=student.id,
            equipment_id=equipment.id,
            booking_date=future_date(),
            start_time=time(9, 0),
            end_time=time(10, 0),
            status="Pending",
        )
        db.session.add(booking)
        db.session.commit()
        return {
            "booking_id": booking.id,
            "equipment_id": equipment.id,
            "student_id": student.id,
        }


def login(client, username):
    response = client.post(
        "/auth/login", data={"username": username, "password": PASSWORD}
    )
    assert response.status_code == 302


def booking_status(app, booking_id):
    with app.app_context():
        return db.session.get(Booking, booking_id).status


def test_staff_sees_pending_request(client, records):
    login(client, "decisionstaff")
    response = client.get("/staff/bookings/")
    assert response.status_code == 200
    assert b"Pending Requests" in response.data
    assert b"decisionstudent" in response.data
    assert b"Decision Microscope" in response.data
    assert b"Approve" in response.data
    assert b"Reject" in response.data


def test_anonymous_user_is_redirected(client, records):
    booking_id = records["booking_id"]
    response = client.get("/staff/bookings/")
    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]
    response = client.post(f"/staff/bookings/{booking_id}/approve")
    assert response.status_code == 302
    assert booking_status(client.application, booking_id) == "Pending"


@pytest.mark.parametrize("action", ["approve", "reject"])
def test_student_cannot_change_status(client, records, action):
    login(client, "decisionstudent")
    assert client.get("/staff/bookings/").status_code == 403
    response = client.post(f"/staff/bookings/{records['booking_id']}/{action}")
    assert response.status_code == 403
    assert booking_status(client.application, records["booking_id"]) == "Pending"


def test_staff_can_approve_and_student_sees_status(client, records):
    booking_id = records["booking_id"]
    login(client, "decisionstaff")
    response = client.post(f"/staff/bookings/{booking_id}/approve")
    assert response.status_code == 302
    assert booking_status(client.application, booking_id) == "Approved"

    history = client.get("/staff/bookings/")
    assert b"Recent Decisions" in history.data
    assert b"Approved" in history.data
    assert b"No Pending booking requests." in history.data

    client.post("/auth/logout")
    login(client, "decisionstudent")
    student_page = client.get("/bookings/")
    assert student_page.status_code == 200
    assert b"Approved" in student_page.data


def test_staff_can_reject_and_student_sees_status(client, records):
    booking_id = records["booking_id"]
    login(client, "decisionstaff")
    response = client.post(f"/staff/bookings/{booking_id}/reject")
    assert response.status_code == 302
    assert booking_status(client.application, booking_id) == "Rejected"

    client.post("/auth/logout")
    login(client, "decisionstudent")
    response = client.get("/bookings/")
    assert b"Rejected" in response.data


def test_rejected_request_frees_booking_slot(client, records):
    booking_id = records["booking_id"]
    login(client, "decisionstaff")
    assert client.post(f"/staff/bookings/{booking_id}/reject").status_code == 302
    client.post("/auth/logout")
    login(client, "decisionstudent")

    result = client.post(
        "/bookings/new",
        data={
            "equipment_id": str(records["equipment_id"]),
            "booking_date": future_date().isoformat(),
            "start_time": "09:00",
            "end_time": "10:00",
        },
    )
    assert result.status_code == 302
    with client.application.app_context():
        assert db.session.scalar(db.select(db.func.count()).select_from(Booking)) == 2


@pytest.mark.parametrize("action", ["approve", "reject"])
def test_decisions_cannot_be_repeated(client, records, action):
    booking_id = records["booking_id"]
    login(client, "decisionstaff")
    assert client.post(f"/staff/bookings/{booking_id}/{action}").status_code == 302
    again = client.post(f"/staff/bookings/{booking_id}/{action}")
    assert again.status_code == 409
    expected = "Approved" if action == "approve" else "Rejected"
    assert booking_status(client.application, booking_id) == expected


def test_rejected_booking_cannot_be_approved(client, records):
    booking_id = records["booking_id"]
    login(client, "decisionstaff")
    client.post(f"/staff/bookings/{booking_id}/reject")
    response = client.post(f"/staff/bookings/{booking_id}/approve")
    assert response.status_code == 409
    assert booking_status(client.application, booking_id) == "Rejected"


def test_cannot_approve_out_of_service_equipment(client, app, records):
    booking_id = records["booking_id"]
    with app.app_context():
        equipment = db.session.get(Equipment, records["equipment_id"])
        equipment.status = "Out of service"
        db.session.commit()
    login(client, "decisionstaff")
    response = client.post(f"/staff/bookings/{booking_id}/approve")
    assert response.status_code == 409
    assert b"Equipment is unavailable" in response.data
    assert booking_status(app, booking_id) == "Pending"


def test_cannot_approve_past_booking(client, app, records):
    booking_id = records["booking_id"]
    with app.app_context():
        booking = db.session.get(Booking, booking_id)
        booking.booking_date = date.today() - timedelta(days=1)
        db.session.commit()
    login(client, "decisionstaff")
    response = client.post(f"/staff/bookings/{booking_id}/approve")
    assert response.status_code == 409
    assert b"start in the future" in response.data
    assert booking_status(app, booking_id) == "Pending"


def test_cannot_approve_legacy_overlap(client, app, records):
    """Legacy/inserted overlap must still be caught at decision time."""
    booking_id = records["booking_id"]
    with app.app_context():
        overlapping = Booking(
            student_id=records["student_id"],
            equipment_id=records["equipment_id"],
            booking_date=future_date(),
            start_time=time(9, 30),
            end_time=time(10, 30),
            status="Approved",
        )
        db.session.add(overlapping)
        db.session.commit()
    login(client, "decisionstaff")
    response = client.post(f"/staff/bookings/{booking_id}/approve")
    assert response.status_code == 409
    assert b"conflicting booking" in response.data
    assert booking_status(app, booking_id) == "Pending"



def test_staff_can_choose_one_of_two_pending_overlaps(
    client, app, records
):
    """One Pending request can be approved, but not both."""

    first_id = records["booking_id"]

    with app.app_context():
        second = Booking(
            student_id=records["student_id"],
            equipment_id=records["equipment_id"],
            booking_date=future_date(),
            start_time=time(9, 30),
            end_time=time(10, 30),
            status="Pending",
        )

        db.session.add(second)
        db.session.commit()
        second_id = second.id

    login(client, "decisionstaff")

    first_response = client.post(
        f"/staff/bookings/{first_id}/approve"
    )

    assert first_response.status_code == 302
    assert booking_status(app, first_id) == "Approved"

    second_response = client.post(
        f"/staff/bookings/{second_id}/approve"
    )

    assert second_response.status_code == 409
    assert booking_status(app, second_id) == "Pending"


def test_unknown_booking_returns_404(client, records):
    login(client, "decisionstaff")
    assert client.post("/staff/bookings/999999/approve").status_code == 404
    assert client.post("/staff/bookings/999999/reject").status_code == 404


def test_decision_urls_require_post(client, records):
    login(client, "decisionstaff")
    bid = records["booking_id"]
    assert client.get(f"/staff/bookings/{bid}/approve").status_code == 405
    assert client.get(f"/staff/bookings/{bid}/reject").status_code == 405


def test_cannot_delete_equipment_with_booking_history(client, app, records):
    login(client, "decisionstaff")
    response = client.post(f"/equipment/{records['equipment_id']}/delete")
    assert response.status_code == 409
    assert b"Cannot delete equipment with booking history" in response.data
    with app.app_context():
        assert db.session.get(Equipment, records["equipment_id"]) is not None
        assert db.session.get(Booking, records["booking_id"]) is not None
