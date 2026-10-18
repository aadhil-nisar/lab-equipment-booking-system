
from app.extensions import db
from app.models.equipment import Equipment


def test_student_login_to_catalogue(client, app):
    # Create sample equipment
    with app.app_context():
        equipment = Equipment(
            name="Microscope",
            category="Optics",
            description="Laboratory equipment",
            status="Available",
        )
        db.session.add(equipment)
        db.session.commit()

    # Register a student
    response = client.post(
        "/auth/register",
        data={
            "username": "teststudent",
            "email": "student@example.com",
            "password": "TestPass123!",
            "confirm_password": "TestPass123!",
        },
    )
    assert response.status_code == 302

    # Login
    response = client.post(
        "/auth/login",
        data={
            "username": "teststudent",
            "password": "TestPass123!",
        },
    )
    assert response.status_code == 302

    # View equipment catalogue
    response = client.get("/equipment/")
    assert response.status_code == 200
    assert b"Microscope" in response.data

    # Student cannot manage equipment
    response = client.get("/equipment/new")
    assert response.status_code == 403
