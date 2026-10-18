
import pytest

from app.extensions import db
from app.models.equipment import Equipment
from app.models.user import User

VALID_EQUIPMENT = {
    "name": "Microscope",
    "category": "Optics",
    "description": "Laboratory microscope",
    "status": "Available",
}


@pytest.fixture
def student_client(client):
    """Create and log in a Student."""
    registration = client.post(
        "/auth/register",
        data={
            "username": "student1",
            "email": "student1@example.com",
            "password": "StrongPass123!",
            "confirm_password": "StrongPass123!",
        },
    )
    assert registration.status_code == 302

    login = client.post(
        "/auth/login",
        data={
            "username": "student1",
            "password": "StrongPass123!",
        },
    )
    assert login.status_code == 302

    return client


@pytest.fixture
def staff_client(client, app):
    """Create and log in a Staff user."""
    with app.app_context():
        staff = User(
            username="staff1",
            email="staff1@example.com",
            role="Staff",
        )
        staff.set_password("StrongPass123!")

        db.session.add(staff)
        db.session.commit()

    login = client.post(
        "/auth/login",
        data={
            "username": "staff1",
            "password": "StrongPass123!",
        },
    )
    assert login.status_code == 302

    return client


def create_equipment(
    app,
    name="Microscope",
    category="Optics",
    status="Available",
):
    """Insert an equipment record for a test."""
    with app.app_context():
        item = Equipment(
            name=name,
            category=category,
            description="Test equipment",
            status=status,
        )

        db.session.add(item)
        db.session.commit()

        return item.id


def test_anonymous_cannot_view_catalogue(client):
    response = client.get("/equipment/")

    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]


def test_logged_in_student_can_view_catalogue(
    student_client,
    app,
):
    create_equipment(app)

    response = student_client.get("/equipment/")

    assert response.status_code == 200
    assert b"Microscope" in response.data
    assert b"Optics" in response.data
    assert b"Available" in response.data


def test_category_filter(student_client, app):
    create_equipment(
        app,
        name="Microscope",
        category="Optics",
    )
    create_equipment(
        app,
        name="Power Supply",
        category="Electronics",
    )

    response = student_client.get(
        "/equipment/?category=Optics"
    )

    assert response.status_code == 200
    assert b"Microscope" in response.data
    assert b"Power Supply" not in response.data

    response = student_client.get("/equipment/")

    assert b"Microscope" in response.data
    assert b"Power Supply" in response.data


def test_empty_catalogue(student_client):
    response = student_client.get("/equipment/")

    assert response.status_code == 200
    assert b"No equipment found" in response.data


def test_student_cannot_add_equipment(student_client, app):
    get_response = student_client.get("/equipment/new")

    assert get_response.status_code == 403

    post_response = student_client.post(
        "/equipment/new",
        data=VALID_EQUIPMENT,
    )

    assert post_response.status_code == 403

    with app.app_context():
        assert Equipment.query.count() == 0


def test_student_cannot_edit_or_delete(
    student_client,
    app,
):
    equipment_id = create_equipment(app)

    edit_url = f"/equipment/{equipment_id}/edit"
    delete_url = f"/equipment/{equipment_id}/delete"

    assert student_client.get(
        edit_url
    ).status_code == 403

    assert student_client.post(
        edit_url,
        data=VALID_EQUIPMENT,
    ).status_code == 403

    assert student_client.post(
        delete_url
    ).status_code == 403

    with app.app_context():
        assert db.session.get(
            Equipment,
            equipment_id,
        ) is not None


def test_staff_can_view_add_form(staff_client):
    response = staff_client.get("/equipment/new")

    assert response.status_code == 200
    assert b"Add Equipment" in response.data


def test_staff_can_add_edit_and_delete(
    staff_client,
    app,
):
    # CREATE
    response = staff_client.post(
        "/equipment/new",
        data=VALID_EQUIPMENT,
    )

    assert response.status_code == 302

    with app.app_context():
        item = Equipment.query.filter_by(
            name="Microscope"
        ).one()

        equipment_id = item.id
        assert item.status == "Available"

    # READ
    response = staff_client.get("/equipment/")

    assert response.status_code == 200
    assert b"Microscope" in response.data

    # UPDATE
    edited_data = {
        "name": "Digital Microscope",
        "category": "Optics",
        "description": "Updated equipment",
        "status": "Out of service",
    }

    response = staff_client.post(
        f"/equipment/{equipment_id}/edit",
        data=edited_data,
    )

    assert response.status_code == 302

    with app.app_context():
        item = db.session.get(
            Equipment,
            equipment_id,
        )

        assert item.name == "Digital Microscope"
        assert item.description == "Updated equipment"
        assert item.status == "Out of service"

    # DELETE
    response = staff_client.post(
        f"/equipment/{equipment_id}/delete"
    )

    assert response.status_code == 302

    with app.app_context():
        assert db.session.get(
            Equipment,
            equipment_id,
        ) is None


@pytest.mark.parametrize(
    "changes",
    [
        {"name": ""},
        {"name": "N" * 121},
        {"category": ""},
        {"category": "C" * 81},
        {"description": "D" * 2001},
        {"status": "Broken"},
    ],
)
def test_invalid_equipment_is_rejected(
    staff_client,
    app,
    changes,
):
    data = VALID_EQUIPMENT.copy()
    data.update(changes)

    response = staff_client.post(
        "/equipment/new",
        data=data,
    )

    assert response.status_code == 400

    with app.app_context():
        assert Equipment.query.count() == 0


def test_invalid_edit_does_not_change_record(
    staff_client,
    app,
):
    equipment_id = create_equipment(app)

    response = staff_client.post(
        f"/equipment/{equipment_id}/edit",
        data={
            **VALID_EQUIPMENT,
            "status": "Invalid Status",
        },
    )

    assert response.status_code == 400

    with app.app_context():
        item = db.session.get(
            Equipment,
            equipment_id,
        )

        assert item.name == "Microscope"
        assert item.status == "Available"


def test_delete_requires_post(staff_client, app):
    equipment_id = create_equipment(app)

    response = staff_client.get(
        f"/equipment/{equipment_id}/delete"
    )

    assert response.status_code == 405

    with app.app_context():
        assert db.session.get(
            Equipment,
            equipment_id,
        ) is not None


def test_missing_equipment_returns_404(staff_client):
    response = staff_client.get(
        "/equipment/999999/edit"
    )

    assert response.status_code == 404
