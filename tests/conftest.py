import os
import pytest
from app import create_app, db


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

    print("TEST_DATABASE_URL =", test_db_uri)
    print("APP DB URI =", app.config["SQLALCHEMY_DATABASE_URI"])

    with app.app_context():
        db.drop_all()
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()