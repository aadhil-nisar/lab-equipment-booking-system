
from ..extensions import db


class Equipment(db.Model):
    """Basic equipment model for the E1 database foundation."""

    __tablename__ = "equipment"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    name = db.Column(
        db.String(120),
        nullable=False,
    )

    category = db.Column(
        db.String(80),
        nullable=False,
    )

    description = db.Column(
        db.Text,
        nullable=False,
        default="",
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Available",
    )
