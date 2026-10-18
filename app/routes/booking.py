
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

from ..booking_validation import validate_booking_slot
from ..extensions import db
from ..models.booking import Booking
from ..models.equipment import Equipment

booking_bp = Blueprint(
    "booking",
    __name__,
    url_prefix="/bookings",
)


def require_student():
    """Only Students can submit and view their own requests."""
    if current_user.role != "Student":
        abort(403)


def read_booking_form():
    """Read and validate basic booking form information."""
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

    if equipment.status != "Available":
        return (
            values,
            None,
            "Equipment is out of service.",
        )


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


    parsed = {
        "equipment_id": equipment.id,
        "booking_date": booking_date,
        "start_time": start_time,
        "end_time": end_time,
    }

    return values, parsed, None


@booking_bp.route("/new", methods=["GET", "POST"])
@login_required
def new():
    """Allow a Student to submit a booking request."""
    require_student()

    available_equipment = db.session.scalars(
        db.select(Equipment)
        .where(Equipment.status == "Available")
        .order_by(
            Equipment.name.asc(),
            Equipment.id.asc(),
        )
    ).all()

    if request.method == "POST":
        values, parsed, error = read_booking_form()

        if error:
            flash(error, "error")
            return render_template(
                "booking/new.html",
                equipment_items=available_equipment,
                form_data=values,
            ), 400

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

        return redirect(url_for("booking.mine"))

    return render_template(
        "booking/new.html",
        equipment_items=available_equipment,
        form_data={},
    )


@booking_bp.get("/")
@login_required
def mine():
    """Show only the logged-in Student's bookings."""
    require_student()

    bookings = db.session.scalars(
        db.select(Booking)
        .where(Booking.student_id == current_user.id)
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
