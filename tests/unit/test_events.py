"""
test_events.py

Test events received from slack.
"""
# Standard lib imports
import os
import json

# Third party imports
from flask.testing import FlaskClient
from dotenv import load_dotenv

# Load env
load_dotenv()

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

def test_onboarding_event(client_fixture: FlaskClient) -> None:
    """ Test team_join event. """
    data = {"token":os.getenv("VERIFICATION"),
            "event":{"type": "team_join",
                "user": "UFY99RRNU",
                "channel": "GKZ71F9DW",
                }
            }

    response = client_fixture.post(path="/slack",
            data=json.dumps(data),
            content_type="application/json")
    assert response.status == "200 OK"

