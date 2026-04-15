import pytest
from app import create_app, db
import os


@pytest.fixture
def app():
    test_db_uri = os.getenv(
        "TEST_DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/testdb"
    )

    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": test_db_uri
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()