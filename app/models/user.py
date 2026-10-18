
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from ..extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    __table_args__ = (
        db.CheckConstraint(
            "role IN ('Student', 'Staff')",
            name="ck_user_role",
        ),
    )

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    username = db.Column(
        db.String(80),
        nullable=False,
        unique=True,
    )

    email = db.Column(
        db.String(120),
        nullable=False,
        unique=True,
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False,
    )

    role = db.Column(
        db.String(10),
        nullable=False,
        default="Student",
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(
            self.password_hash,
            password,
        )

    @property
    def is_staff(self):
        return self.role == "Staff"
