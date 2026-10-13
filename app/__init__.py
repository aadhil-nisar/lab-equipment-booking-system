
from pathlib import Path

from flask import Flask, render_template

from .extensions import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    Path(app.instance_path).mkdir(
        parents=True,
        exist_ok=True,
    )

    app.config.update(
        SQLALCHEMY_DATABASE_URI="sqlite:///lab_equipment.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is not None:
        app.config.update(test_config)

    db.init_app(app)

    @app.get("/")
    def index():
        return render_template("index.html")

    with app.app_context():
        from . import models  # noqa: F401

        db.create_all()

    return app
