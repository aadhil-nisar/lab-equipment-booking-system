"""Booking validation rules for FR-03."""

from datetime import datetime, timedelta

from .extensions import db
from .models.booking import Booking

# Minimum and maximum booking durations.
MIN_DURATION = timedelta(minutes=30)
MAX_DURATION = timedelta(hours=4)

# Bookings that reserve equipment time slots.
ACTIVE_STATUSES = ("Pending", "Approved")


def validate_booking_slot(
    booking_date,
    start_time,
    end_time,
    *,
    now=None,
):
    """Validate booking date, time and duration.

    Returns:
        str: Validation error message.
        None: Booking time slot is valid.
    """

    current_time = datetime.now() if now is None else now

    start = datetime.combine(
        booking_date,
        start_time,
    )

    end = datetime.combine(
        booking_date,
        end_time,
    )

    # Rule 1: End time must be after start time.
    if end <= start:
        return "End time must be after start time."

    # Rule 2: Booking must start in the future.
    if start <= current_time:
        return "Bookings must start in the future."

    duration = end - start

    # Rule 3: Minimum booking duration.
    if duration < MIN_DURATION:
        return "Booking must be at least 30 minutes."

    # Rule 4: Maximum booking duration.
    if duration > MAX_DURATION:
        return "Booking cannot be longer than 4 hours."

    # All booking time validation rules passed.
    return None


def has_booking_conflict(
    equipment_id,
    booking_date,
    start_time,
    end_time,
    *,
    exclude_booking_id=None,
    blocking_statuses=ACTIVE_STATUSES,
):
    """Check for overlapping equipment bookings.

    Conflict policy:
        - Pending bookings block overlapping requests.
        - Approved bookings block overlapping requests.
        - Rejected bookings do not block requests.
        - Adjacent bookings are allowed.
        - Different equipment does not conflict.
        - Different dates do not conflict.

    Args:
        equipment_id: Equipment being requested.
        booking_date: Requested date.
        start_time: Requested start time.
        end_time: Requested end time.
        exclude_booking_id: Optional booking ID to ignore
            when validating an existing booking for approval.

    Returns:
        bool: True if a conflict exists, otherwise False.
    """

    statement = db.select(Booking.id).where(
        Booking.equipment_id == equipment_id,
        Booking.booking_date == booking_date,
        Booking.status.in_(blocking_statuses),
        Booking.start_time < end_time,
        Booking.end_time > start_time,
    )

    # Exclude the booking currently being approved.
    if exclude_booking_id is not None:
        statement = statement.where(Booking.id != exclude_booking_id)

    conflicting_booking_id = db.session.scalar(statement.limit(1))

    return conflicting_booking_id is not None
