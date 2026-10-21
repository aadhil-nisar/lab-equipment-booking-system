
"""Booking validation rules for FR-03."""

from datetime import datetime, timedelta

from .extensions import db
from .models.booking import Booking

MIN_DURATION = timedelta(minutes=30)
MAX_DURATION = timedelta(hours=4)

ACTIVE_STATUSES = ("Pending", "Approved")


def validate_booking_slot(
    booking_date,
    start_time,
    end_time,
    *,
    now=None,
):
    """Validate booking date, time and duration."""

    current_time = datetime.now() if now is None else now

    start = datetime.combine(
        booking_date,
        start_time,
    )

    end = datetime.combine(
        booking_date,
        end_time,
    )

    if end <= start:
        return "End time must be after start time."

    if start <= current_time:
        return "Bookings must start in the future."

    duration = end - start

    if duration < MIN_DURATION:
        return "Booking must be at least 30 minutes."

    if duration > MAX_DURATION:
        return "Booking cannot be longer than 4 hours."

    return None


def has_booking_conflict(
    equipment_id,
    booking_date,
    start_time,
    end_time,
    *,
    exclude_booking_id=None,
):
    """Check whether an active booking overlaps the requested slot."""

    statement = db.select(Booking.id).where(
        Booking.equipment_id == equipment_id,
        Booking.booking_date == booking_date,
        Booking.status.in_(ACTIVE_STATUSES),
        Booking.start_time < end_time,
        Booking.end_time > start_time,
    )

    if exclude_booking_id is not None:
        statement = statement.where(
            Booking.id != exclude_booking_id
        )

    return db.session.scalar(
        statement.limit(1)
    ) is not None
