"""
test_bot.py

Holds the bot app tests.
"""
# Standard lib imports
import json

# Third party imports
from flask.testing import FlaskClient

def test_challenge_response(client_fixture: FlaskClient) -> None:
    """ Test connection response. """
    data = {"challenge": "challenge"}

    response = client_fixture.post(path="/slack",
            data=json.dumps(data),
            content_type="application/json")
    assert response.status == "200 OK"

def test_verification(client_fixture: FlaskClient) -> None:
    """ Test verification key """
    data = {"token": "invalid token key"}

    response = client_fixture.post(path="/slack",
            data=json.dumps(data),
            content_type="application/json")
    assert response.status == "403 FORBIDDEN"
