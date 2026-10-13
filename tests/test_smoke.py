
from sqlalchemy import inspect

from app.extensions import db
from app.models.equipment import Equipment


def test_homepage(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Lab Equipment Booking System" in response.data


def test_invalid_route(client):
    response = client.get("/unknown-page")

    assert response.status_code == 404


def test_equipment_table_exists(app):
    with app.app_context():
        tables = inspect(db.engine).get_table_names()

        assert "equipment" in tables


def test_equipment_can_be_saved(app):
    with app.app_context():
        item = Equipment(
            name="Microscope",
            category="Optics",
            description="Laboratory microscope",
            status="Available",
        )

        db.session.add(item)
        db.session.commit()

        saved = db.session.get(Equipment, item.id)

        assert saved is not None
        assert saved.name == "Microscope"
        assert saved.status == "Available"
