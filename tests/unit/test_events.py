"""
test_events.py
Test events received from slack.
"""
# Standard lib imports
import os
import json
import hmac
import hashlib
from unittest.mock import MagicMock, patch

# Third party imports
import pytest
import slack
from flask.testing import FlaskClient
from dotenv import load_dotenv

# Local imports
from slackbot import endpoint
from manage import app

# Load env
load_dotenv()


def test_challenge_response(client_fixture: FlaskClient) -> None:
    """ Test connection response. """
    data = {"challenge": "challenge"}

    response = client_fixture.post(path="/slack",
                                   data=json.dumps(data),
                                   content_type="application/json")
    assert response.status == "200 OK"

# @patch("slackbot.endpoint.request.headers", spec=True)
@pytest.mark.skip()
def test_verify_signing(client_fixture: FlaskClient) -> None:
    """ Test verification key """
    expected_basestring = str.encode("v0:1:test")
    secret_key = str.encode(os.getenv("SIGNING_SECRET"))
    slack_hash = hmac.new(secret_key, expected_basestring, hashlib.sha256).hexdigest()
    fake_request_headers = {"X-Slack-Request-Timestamp": 1, "X-Slack-Signature": f"v=0{slack_hash}"}
    with app.test_request_context("/slack/hello", data="test", headers=fake_request_headers):
        assert endpoint.verify_signing("test")

@patch("slackbot.endpoint.WEB_CLIENT", spec=True)
def test_onboarding_event(fake_web_client, client_fixture: FlaskClient) -> None:
    """ Test team_join event. """
    data = {"token": os.getenv("VERIFICATION"),
            "event": {"type": "team_join",
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
