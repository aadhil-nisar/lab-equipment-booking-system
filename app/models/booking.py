
from ..extensions import db


class Booking(db.Model):
    """A student's laboratory equipment booking request."""

    __tablename__ = "bookings"

    __table_args__ = (
        db.CheckConstraint(
            "status IN ('Pending', 'Approved', 'Rejected')",
            name="ck_booking_status",
        ),
    )

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    equipment_id = db.Column(
        db.Integer,
        db.ForeignKey("equipment.id"),
        nullable=False,
        index=True,
    )

    booking_date = db.Column(
        db.Date,
        nullable=False,
    )

    start_time = db.Column(
        db.Time,
        nullable=False,
    )

    end_time = db.Column(
        db.Time,
        nullable=False,
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Pending",
    )

    student = db.relationship(
        "User",
        backref="booking_requests",
    )

    equipment = db.relationship(
        "Equipment",
        backref="booking_requests",
    )
