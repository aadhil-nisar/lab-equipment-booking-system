
from app.models.user import User


def test_student_registration(client, app):
    response = client.post(
        "/auth/register",
        data={
            "username": "student1",
            "email": "student1@example.com",
            "password": "TestPass123!",
            "confirm_password": "TestPass123!",
        },
    )

    assert response.status_code == 302

    with app.app_context():
        user = User.query.filter_by(
            username="student1"
        ).first()

        assert user is not None
        assert user.role == "Student"
        assert user.password_hash != "TestPass123!"
        assert user.check_password("TestPass123!")


def test_student_login_and_logout(client):
    client.post(
        "/auth/register",
        data={
            "username": "student1",
            "email": "student1@example.com",
            "password": "TestPass123!",
            "confirm_password": "TestPass123!",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "student1",
            "password": "TestPass123!",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Welcome, student1!" in response.data

    response = client.post(
        "/auth/logout",
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Register" in response.data


def test_student_cannot_access_staff_page(client):
    client.post(
        "/auth/register",
        data={
            "username": "student1",
            "email": "student1@example.com",
            "password": "TestPass123!",
            "confirm_password": "TestPass123!",
        },
    )

    client.post(
        "/auth/login",
        data={
            "username": "student1",
            "password": "TestPass123!",
        },
    )

    response = client.get("/auth/staff")

    assert response.status_code == 403


def test_public_registration_cannot_create_staff(client, app):
    client.post(
        "/auth/register",
        data={
            "username": "student2",
            "email": "student2@example.com",
            "password": "TestPass123!",
            "confirm_password": "TestPass123!",
            "role": "Staff",
        },
    )

    with app.app_context():
        user = User.query.filter_by(
            username="student2"
        ).first()

        assert user is not None
        assert user.role == "Student"


def test_invalid_password(client):
    response = client.post(
        "/auth/login",
        data={
            "username": "unknown",
            "password": "WrongPassword",
        },
    )

    assert response.status_code == 200
    assert b"Invalid username or password" in response.data
