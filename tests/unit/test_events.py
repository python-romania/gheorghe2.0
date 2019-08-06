"""
test_events.py

Test events received from slack.
"""
# Standard lib imports
import os
import json
from unittest.mock import MagicMock, patch

# Third party imports
import slack
from flask.testing import FlaskClient
from dotenv import load_dotenv

# Local imports
from slackbot import endpoint

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

@patch("slackbot.endpoint.WEB_CLIENT", spec=True)
def test_onboarding_event(fake_web_client, client_fixture: FlaskClient) -> None:
    """ Test team_join event. """
    data = {"token":os.getenv("VERIFICATION"),
            "event":{"type": "team_join",
                "user": "UFY99RRNU",
                "channel": "GKZ71F9DW",
                }
            }

    # Set fake response
    fake_response = {"ok": True, "ts": 0}
    fake_web_client.chat_postMessage.return_value = fake_response

    response = client_fixture.post(path="/slack",
            data=json.dumps(data),
            content_type="application/json")
    assert response.status == "200 OK"
