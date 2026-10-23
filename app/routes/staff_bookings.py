"""FR-04: Staff booking approval and rejection."""

from flask import Blueprint, abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from ..booking_validation import has_booking_conflict, validate_booking_slot
from ..extensions import db
from ..models.booking import Booking
from ..models.equipment import Equipment

staff_bookings_bp = Blueprint("staff_bookings", __name__, url_prefix="/staff/bookings")


def require_staff():
    """Allow only authenticated Staff accounts to manage requests."""
    if not current_user.is_staff:
        abort(403)


def render_dashboard(status_code=200):
    """Show outstanding requests and the most recent decisions."""
    pending = db.session.scalars(
        db.select(Booking)
        .where(Booking.status == "Pending")
        .order_by(
            Booking.booking_date.asc(),
            Booking.start_time.asc(),
            Booking.id.asc(),
        )
    ).all()

    history = db.session.scalars(
        db.select(Booking)
        .where(Booking.status.in_(("Approved", "Rejected")))
        .order_by(Booking.id.desc())
        .limit(30)
    ).all()

    return (
        render_template("staff/bookings.html", pending=pending, history=history),
        status_code,
    )


@staff_bookings_bp.get("/")
@login_required
def index():
    """List booking requests for Staff review."""
    require_staff()
    return render_dashboard()


@staff_bookings_bp.post("/<int:booking_id>/approve")
@login_required
def approve(booking_id):
    """Approve a valid, non-conflicting Pending request."""
    require_staff()
    booking = db.get_or_404(Booking, booking_id)

    if booking.status != "Pending":
        flash("Only Pending requests can be approved.", "error")
        return render_dashboard(409)

    equipment = db.session.get(Equipment, booking.equipment_id)
    if equipment is None or equipment.status != "Available":
        flash("Equipment is unavailable; approval was blocked.", "error")
        return render_dashboard(409)

    error = validate_booking_slot(
        booking.booking_date, booking.start_time, booking.end_time
    )
    if error:
        flash(f"Approval blocked: {error}", "error")
        return render_dashboard(409)


    if has_booking_conflict(
        booking.equipment_id,
        booking.booking_date,
        booking.start_time,
        booking.end_time,
        exclude_booking_id=booking.id,
        blocking_statuses=("Approved",),
    ):

        flash("Approval blocked: conflicting booking exists.", "error")
        return render_dashboard(409)

    booking.status = "Approved"
    db.session.commit()
    flash("Booking approved successfully.", "success")
    return redirect(url_for("staff_bookings.index"))


@staff_bookings_bp.post("/<int:booking_id>/reject")
@login_required
def reject(booking_id):
    """Reject a Pending request without deleting its history."""
    require_staff()
    booking = db.get_or_404(Booking, booking_id)

    if booking.status != "Pending":
        flash("Only Pending requests can be rejected.", "error")
        return render_dashboard(409)

    booking.status = "Rejected"
    db.session.commit()
    flash("Booking rejected successfully.", "success")
    return redirect(url_for("staff_bookings.index"))
