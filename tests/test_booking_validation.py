
"""FR-03 E2 booking validation tests."""

from datetime import date, datetime, time, timedelta

import pytest

from app.booking_validation import validate_booking_slot
from app.extensions import db
from app.models.booking import Booking
from app.models.equipment import Equipment
from app.models.user import User

FIXED_NOW = datetime(2026, 10, 19, 8, 0)


@pytest.mark.parametrize(
    ("day", "start", "end", "expected"),
    [
        (
            "2026-10-20", "09:00", "09:29",
            "Booking must be at least 30 minutes.",
        ),
        (
            "2026-10-20", "09:00", "09:30",
            None,
        ),
        (
            "2026-10-20", "09:00", "09:31",
            None,
        ),
        (
            "2026-10-20", "09:00", "12:59",
            None,
        ),
        (
            "2026-10-20", "09:00", "13:00",
            None,
        ),
        (
            "2026-10-20", "09:00", "13:01",
            "Booking cannot be longer than 4 hours.",
        ),
        (
            "2026-10-20", "09:00", "09:00",
            "End time must be after start time.",
        ),
        (
            "2026-10-20", "11:00", "10:00",
            "End time must be after start time.",
        ),
        (
            "2026-10-18", "09:00", "10:00",
            "Bookings must start in the future.",
        ),
        (
            "2026-10-19", "07:59", "08:59",
            "Bookings must start in the future.",
        ),
        (
            "2026-10-19", "08:00", "09:00",
            "Bookings must start in the future.",
        ),
        (
            "2026-10-19", "08:01", "09:01",
            None,
        ),
    ],
)
def test_booking_time_boundaries(
    day,
    start,
    end,
    expected,
):
    """Check valid, invalid and boundary time slots."""
    result = validate_booking_slot(
        date.fromisoformat(day),
        time.fromisoformat(start),
        time.fromisoformat(end),
        now=FIXED_NOW,
    )

    assert result == expected


@pytest.fixture
def student_client(client, app):
    """Create and log in a Student."""
    with app.app_context():
        student = User(
            username="validationstudent",
            email="validation@example.com",
            role="Student",
        )
        student.set_password("StrongPass123!")

        db.session.add(student)
        db.session.commit()

    response = client.post(
        "/auth/login",
        data={
            "username": "validationstudent",
            "password": "StrongPass123!",
        },
    )

    assert response.status_code == 302

    return client


@pytest.fixture
def equipment_id(app):
    """Create one available equipment item."""
    with app.app_context():
        equipment = Equipment(
            name="Test Microscope",
            category="Optics",
            description="For FR-03 tests",
            status="Available",
        )

        db.session.add(equipment)
        db.session.commit()

        return equipment.id


def booking_form(equipment_id, **changes):
    """Build valid booking form data."""
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


@pytest.mark.parametrize(
    ("end_time", "expected_status", "message"),
    [
        (
            "09:29", 400,
            b"Booking must be at least 30 minutes.",
        ),
        (
            "09:30", 302,
            None,
        ),
        (
            "13:00", 302,
            None,
        ),
        (
            "13:01", 400,
            b"Booking cannot be longer than 4 hours.",
        ),
    ],
)
def test_booking_form_duration_limits(
    student_client,
    app,
    equipment_id,
    end_time,
    expected_status,
    message,
):
    """Verify duration rules through the actual Flask form."""
    response = student_client.post(
        "/bookings/new",
        data=booking_form(
            equipment_id,
            end_time=end_time,
        ),
    )

    assert response.status_code == expected_status

    if message is not None:
        assert message in response.data

    with app.app_context():
        expected_count = (
            1 if expected_status == 302 else 0
        )

        assert Booking.query.count() == expected_count


def test_past_booking_is_rejected(
    student_client,
    app,
    equipment_id,
):
    """Reject a date that has already passed."""
    yesterday = (
        date.today() - timedelta(days=1)
    ).isoformat()

    response = student_client.post(
        "/bookings/new",
        data=booking_form(
            equipment_id,
            booking_date=yesterday,
        ),
    )

    assert response.status_code == 400
    assert b"Bookings must start in the future." in response.data

    with app.app_context():
        assert Booking.query.count() == 0


def test_end_before_start_is_rejected(
    student_client,
    app,
    equipment_id,
):
    response = student_client.post(
        "/bookings/new",
        data=booking_form(
            equipment_id,
            start_time="11:00",
            end_time="10:00",
        ),
    )

    assert response.status_code == 400
    assert b"End time must be after start time." in response.data

    with app.app_context():
        assert Booking.query.count() == 0


def test_valid_duration_creates_pending_booking(
    student_client,
    app,
    equipment_id,
):
    response = student_client.post(
        "/bookings/new",
        data=booking_form(
            equipment_id,
            start_time="10:00",
            end_time="11:00",
        ),
    )

    assert response.status_code == 302

    with app.app_context():
        booking = db.session.scalar(
            db.select(Booking)
        )

        assert booking is not None
        assert booking.status == "Pending"
        assert booking.equipment_id == equipment_id
