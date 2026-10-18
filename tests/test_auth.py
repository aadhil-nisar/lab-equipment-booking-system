
import pytest

from app.models.user import User

STUDENT_DATA = {
    "username": "student1",
    "email": "student1@example.com",
    "password": "StrongPass123!",
    "confirm_password": "StrongPass123!",
    "role": "Staff",
}


def register_student(client, **changes):
    data = STUDENT_DATA.copy()
    data.update(changes)

    return client.post("/auth/register", data=data)


def login_student(client, password="StrongPass123!"):
    return client.post(
        "/auth/login",
        data={
            "username": "student1",
            "password": password,
        },
        follow_redirects=True,
    )


def test_registration_creates_student(client, app):
    response = register_student(client)

    assert response.status_code == 302

    with app.app_context():
        user = User.query.filter_by(
            username="student1"
        ).one()

        assert user.role == "Student"
        assert user.email == "student1@example.com"
        assert user.password_hash != "StrongPass123!"
        assert user.check_password("StrongPass123!")


@pytest.mark.parametrize(
    "changes",
    [
        {"username": "a"},
        {"email": "invalid-email"},
        {"password": "short", "confirm_password": "short"},
        {"confirm_password": "Different123!"},
    ],
)
def test_invalid_registration(client, app, changes):
    response = register_student(client, **changes)

    assert response.status_code == 200

    with app.app_context():
        assert User.query.count() == 0


def test_duplicate_username_rejected(client, app):
    register_student(client)

    response = register_student(
        client,
        email="another@example.com",
    )

    assert response.status_code == 200
    assert b"Username already exists" in response.data

    with app.app_context():
        assert User.query.count() == 1


def test_duplicate_email_rejected(client, app):
    register_student(client)

    response = register_student(
        client,
        username="student2",
    )

    assert response.status_code == 200
    assert b"Email already exists" in response.data

    with app.app_context():
        assert User.query.count() == 1


def test_login_and_logout(client):
    register_student(client)

    response = login_student(client)

    assert response.status_code == 200
    assert b"Welcome, student1!" in response.data
    assert b"<strong>Student</strong>" in response.data

    response = client.post(
        "/auth/logout",
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Logged in as student1" not in response.data
    assert b"Register" in response.data


def test_wrong_password_rejected(client):
    register_student(client)

    response = login_student(
        client,
        password="WrongPassword123",
    )

    assert b"Invalid username or password" in response.data
    assert b"Welcome, student1!" not in response.data


def test_anonymous_staff_access_redirects(client):
    response = client.get("/auth/staff")

    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]


def test_student_cannot_access_staff_page(client):
    register_student(client)
    login_student(client)

    response = client.get("/auth/staff")

    assert response.status_code == 403


def test_staff_command_and_login(client, app):
    runner = app.test_cli_runner()

    result = runner.invoke(
        args=["create-staff"],
        input=(
            "staff1\n"
            "staff1@example.com\n"
            "StrongPass123!\n"
            "StrongPass123!\n"
        ),
    )

    assert result.exit_code == 0

    with app.app_context():
        staff = User.query.filter_by(
            username="staff1"
        ).one()

        assert staff.role == "Staff"
        assert staff.check_password("StrongPass123!")

    login_response = client.post(
        "/auth/login",
        data={
            "username": "staff1",
            "password": "StrongPass123!",
        },
    )

    assert login_response.status_code == 302

    staff_response = client.get("/auth/staff")

    assert staff_response.status_code == 200
    assert b"Staff Dashboard" in staff_response.data
