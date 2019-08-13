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
from flask.testing import FlaskClient
from dotenv import load_dotenv

# Local imports
from slackbot import endpoint

# Load env
load_dotenv()

def test_challenge_response(client: FlaskClient) -> None:
    """ Test connection response. """
    data = {"challenge": "challenge"}

    response = client.post(path="/slack", data=json.dumps(data), content_type="application/json")
    assert response.status == "200 OK"

# @patch("slackbot.endpoint.request", spec=True)
def test_verify_signing() -> None:
    """ Test verification key """
    # Setup
    expected_basestring = str.encode("v0:1:test")
    secret_key = str.encode(os.getenv("SIGNING_SECRET"))
    slack_hash = hmac.new(secret_key, expected_basestring, hashlib.sha256).hexdigest()
    headers = {"X-Slack-Request-Timestamp": 1, "X-Slack-Signature": f"v0={slack_hash}"}

    # Set facke request
    faker = MagicMock()
    faker.headers = headers

    # Test verify_signing
    # Should return True
    with patch("slackbot.endpoint.request", faker):
        assert endpoint.verify_signing("test")

@patch("slackbot.endpoint.WEB_CLIENT", spec=True)
def test_onboarding_event(fake_web_client: MagicMock, client: FlaskClient) -> None:
    """ Test team_join event. """
    # Set data
    data = {"event": {"type": "team_join", "user": "UFY99RRNU", "channel": "GKZ71F9DW",}}

    # Set fake response
    fake_response = {"ok": True, "ts": 0}
    fake_web_client.chat_postMessage.return_value = fake_response

    # Patch verify_signing function
    with patch("slackbot.endpoint.verify_signing", lambda a: True):
        response = client.post(path="/slack", data=json.dumps(data), content_type="application/json")
        assert response.status == "200 OK"

def test_message_event(client: FlaskClient) -> None:
    """ Test Listen for specific messages. """
    data = {"challenge":"challenge", "token": os.getenv("VERIFICATION"), "event": {"type": "message"}}

    # Set response
    response = client.post(path="/slack", data=json.dumps(data), content_type="application/json")
    assert response.status == "200 OK"
