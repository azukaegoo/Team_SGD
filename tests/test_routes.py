from app.models import OneAppButton
from unittest.mock import patch


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200


def test_submit_saves_button_click(client, app):
    response = client.post("/submit", follow_redirects=True)

    assert response.status_code == 200
    assert b"Button click saved successfully." in response.data

    with app.app_context():
        rows = OneAppButton.query.all()
        assert len(rows) == 1
        assert rows[0].value == "button_clicked"


def test_submit_failure_rolls_back(client):
    with patch("app.routes.db.session.commit", side_effect=Exception("DB fail")), \
         patch("app.routes.db.session.rollback") as mock_rollback:

        response = client.post("/submit", follow_redirects=True)

        assert response.status_code == 200
        assert b"Could not save button click." in response.data
        mock_rollback.assert_called_once()
