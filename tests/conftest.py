
import pytest

from app import create_app


@pytest.fixture
def app():
    application = create_app(
{
    "TESTING": True,
    "SECRET_KEY": "test-only-secret",
    "WTF_CSRF_ENABLED": False,
    "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
}
    )

    return application


@pytest.fixture
def client(app):
    return app.test_client()
