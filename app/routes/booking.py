
"""Student booking request routes for FR-02 and FR-03."""

from datetime import date, datetime

from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required

from ..booking_validation import (
    has_booking_conflict,
    validate_booking_slot,
)
from ..extensions import db
from ..models.booking import Booking
from ..models.equipment import Equipment

booking_bp = Blueprint(
    "booking",
    __name__,
    url_prefix="/bookings",
)


def require_student():
    """Allow only Students to access booking request routes."""
    if current_user.role != "Student":
        abort(403)


def read_booking_form():
    """Read and validate Student booking request information."""

    values = {
        "equipment_id": request.form.get(
            "equipment_id", ""
        ).strip(),
        "booking_date": request.form.get(
            "booking_date", ""
        ).strip(),
        "start_time": request.form.get(
            "start_time", ""
        ).strip(),
        "end_time": request.form.get(
            "end_time", ""
        ).strip(),
    }

    # Step 1: Validate form input formats.
    try:
        equipment_id = int(values["equipment_id"])

        if equipment_id < 1:
            raise ValueError("Invalid equipment ID")

        booking_date = date.fromisoformat(
            values["booking_date"]
        )

        start_time = datetime.strptime(
            values["start_time"],
            "%H:%M",
        ).time()

        end_time = datetime.strptime(
            values["end_time"],
            "%H:%M",
        ).time()

    except ValueError:
        return (
            values,
            None,
            "Select equipment and enter a valid date and time.",
        )

    # Step 2: Check that the equipment exists.
    equipment = db.session.get(
        Equipment,
        equipment_id,
    )

    if equipment is None:
        return (
            values,
            None,
            "Selected equipment does not exist.",
        )

    # Step 3: Reject equipment that is out of service.
    if equipment.status != "Available":
        return (
            values,
            None,
            "Equipment is out of service.",
        )

    # Step 4: Validate dates, times and booking duration.
    validation_error = validate_booking_slot(
        booking_date,
        start_time,
        end_time,
    )

    if validation_error:
        return (
            values,
            None,
            validation_error,
        )

    # Step 5: Check for overlapping booking requests.
    if has_booking_conflict(
        equipment.id,
        booking_date,
        start_time,
        end_time,
    ):
        return (
            values,
            None,
            "Equipment is already booked for this time.",
        )

    # Step 6: Return validated booking information.
    parsed = {
        "equipment_id": equipment.id,
        "booking_date": booking_date,
        "start_time": start_time,
        "end_time": end_time,
    }

    return values, parsed, None


@booking_bp.route(
    "/new",
    methods=["GET", "POST"],
)
@login_required
def new():
    """Allow Students to submit booking requests."""

    require_student()

    # Display only available equipment in the form.
    available_equipment = db.session.scalars(
        db.select(Equipment)
        .where(
            Equipment.status == "Available"
        )
        .order_by(
            Equipment.name.asc(),
            Equipment.id.asc(),
        )
    ).all()

    if request.method == "POST":

        # Validate all submitted booking details.
        values, parsed, error = read_booking_form()

        if error:
            flash(error, "error")

            return render_template(
                "booking/new.html",
                equipment_items=available_equipment,
                form_data=values,
            ), 400

        # New booking requests always start as Pending.
        booking = Booking(
            student_id=current_user.id,
            equipment_id=parsed["equipment_id"],
            booking_date=parsed["booking_date"],
            start_time=parsed["start_time"],
            end_time=parsed["end_time"],
            status="Pending",
        )

        db.session.add(booking)
        db.session.commit()

        flash(
            "Booking request submitted successfully.",
            "success",
        )

        return redirect(
            url_for("booking.mine")
        )

    # Display the booking request form.
    return render_template(
        "booking/new.html",
        equipment_items=available_equipment,
        form_data={},
    )


@booking_bp.get("/")
@login_required
def mine():
    """Display only the current Student's booking requests."""

    require_student()

    bookings = db.session.scalars(
        db.select(Booking)
        .where(
            Booking.student_id == current_user.id
        )
        .order_by(
            Booking.booking_date.desc(),
            Booking.start_time.desc(),
            Booking.id.desc(),
        )
    ).all()

    return render_template(
        "booking/mine.html",
        bookings=bookings,
    )
