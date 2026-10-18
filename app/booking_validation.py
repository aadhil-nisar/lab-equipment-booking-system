
"""Booking time validation rules for FR-03."""

from datetime import datetime, timedelta

MIN_DURATION = timedelta(minutes=30)
MAX_DURATION = timedelta(hours=4)


def validate_booking_slot(
    booking_date,
    start_time,
    end_time,
    *,
    now=None,
):
    """Return an error message or None for a valid time slot."""

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
