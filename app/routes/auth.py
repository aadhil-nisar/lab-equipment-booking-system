
import re

from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)

from ..extensions import db
from ..models.user import User

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    if request.method == "POST":
        username = request.form.get(
            "username", ""
        ).strip().lower()

        email = request.form.get(
            "email", ""
        ).strip().lower()

        password = request.form.get("password", "")
        confirm_password = request.form.get(
            "confirm_password", ""
        )

        username_valid = (
            3 <= len(username) <= 80
            and re.fullmatch(r"[a-z0-9_]+", username)
        )

        email_valid = (
            len(email) <= 120
            and re.fullmatch(
                r"[^@\s]+@[^@\s]+\.[^@\s]+",
                email,
            )
        )

        if not username_valid:
            flash(
                "Username must be 3-80 letters, "
                "numbers or underscores.",
                "error",
            )

        elif not email_valid:
            flash("Enter a valid email address.", "error")

        elif len(password) < 8:
            flash(
                "Password must be at least 8 characters.",
                "error",
            )

        elif password != confirm_password:
            flash("Passwords do not match.", "error")

        elif User.query.filter_by(
            username=username
        ).first():
            flash("Username already exists.", "error")

        elif User.query.filter_by(email=email).first():
            flash("Email already exists.", "error")

        else:
            user = User(
                username=username,
                email=email,
                role="Student",
            )

            user.set_password(password)

            db.session.add(user)
            db.session.commit()

            flash(
                "Registration successful. Please log in.",
                "success",
            )

            return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    if request.method == "POST":
        username = request.form.get(
            "username", ""
        ).strip().lower()

        password = request.form.get("password", "")

        user = User.query.filter_by(
            username=username
        ).first()

        if user and user.check_password(password):
            login_user(user)

            return redirect(url_for("index"))

        flash(
            "Invalid username or password.",
            "error",
        )

    return render_template("auth/login.html")


@auth_bp.post("/logout")
@login_required
def logout():
    logout_user()

    flash("You have been logged out.", "success")

    return redirect(url_for("index"))


@auth_bp.get("/staff")
@login_required
def staff_page():
    if not current_user.is_staff:
        abort(403)

    return render_template("auth/staff.html")
