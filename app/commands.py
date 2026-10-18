
import re

import click
from flask.cli import with_appcontext

from .extensions import db
from .models.user import User


@click.command("create-staff")
@click.option("--username", prompt=True)
@click.option("--email", prompt=True)
@click.password_option(confirmation_prompt=True)
@with_appcontext
def create_staff(username, email, password):
    username = username.strip().lower()
    email = email.strip().lower()

    if not re.fullmatch(r"[a-z0-9_]{3,80}", username):
        raise click.ClickException(
            "Username must be 3-80 letters, "
            "numbers or underscores."
        )

    if (
        len(email) > 120
        or not re.fullmatch(
            r"[^@\s]+@[^@\s]+\.[^@\s]+",
            email,
        )
    ):
        raise click.ClickException("Invalid email address.")

    if len(password) < 8:
        raise click.ClickException(
            "Password must be at least 8 characters."
        )

    if User.query.filter_by(username=username).first():
        raise click.ClickException(
            "Username already exists."
        )

    if User.query.filter_by(email=email).first():
        raise click.ClickException(
            "Email already exists."
        )

    staff = User(
        username=username,
        email=email,
        role="Staff",
    )

    staff.set_password(password)

    db.session.add(staff)
    db.session.commit()

    click.echo("Staff account created successfully.")
