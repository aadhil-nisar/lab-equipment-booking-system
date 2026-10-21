import os
import secrets
from pathlib import Path

from flask import Flask, render_template

from .extensions import csrf, db, login_manager


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    Path(app.instance_path).mkdir(
        parents=True,
        exist_ok=True,
    )

    app.config.update(
        SECRET_KEY=(os.environ.get("SECRET_KEY") or secrets.token_hex(32)),
        SQLALCHEMY_DATABASE_URI="sqlite:///lab_equipment.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is not None:
        app.config.update(test_config)

    # Initialize Flask extensions.
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # FR-00: Accounts and Login.
    from .routes.auth import auth_bp

    app.register_blueprint(auth_bp)

    # FR-01: Equipment Catalogue.
    from .routes.equipment import equipment_bp

    app.register_blueprint(equipment_bp)

    # FR-02 and FR-03: Booking Requests and Validation.
    from .routes.booking import booking_bp

    app.register_blueprint(booking_bp)

    # FR-04: Staff Booking Approval and Rejection.
    from .routes.staff_bookings import staff_bookings_bp

    app.register_blueprint(staff_bookings_bp)

    # Register the Staff account creation command.
    from .commands import create_staff

    app.cli.add_command(create_staff)

    # Application homepage.
    @app.get("/")
    def index():
        return render_template("index.html")

    # Initialize database tables.
    with app.app_context():
        from . import models  # noqa: F401

        db.create_all()

    return app
