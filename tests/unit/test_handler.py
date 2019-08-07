"""
test_handler.py

Holds tests for events handler.
"""
# Standard imports
import os
from unittest.mock import MagicMock, patch

# Third party imports
import slack
import pytest
from dotenv import load_dotenv

# Local imports
from slackbot import handler

# Load environments
load_dotenv()


@pytest.fixture
def web_client_fixture() -> slack.WebClient:
    """ WebClient setup. """
    token = os.getenv("SLACK_BOT_TOKEN")
    web_client = slack.WebClient(token)
    yield web_client


@patch("slack.WebClient", spec=True)
def test_message_handler(fake_web_client: MagicMock) -> None:
    """ Test send message handler. """
    # Set fake response
    fake_response = {"ok": True}
    fake_web_client.chat_postMessage.return_value = fake_response

    # Data to create the message
    channel = "GKZ71F9DW"
    user_id = "UFY99RRNU"
    text = "Hello World!"

    response = handler.message_handler(fake_web_client, channel, user_id, text)
    assert response["ok"]


@patch("slack.WebClient", spec=True)
def test_onboarding_handler(fake_web_client: MagicMock) -> None:
    """ Test send onboarding message. """
    # Set fake response
    fake_response = {"ok": True, "ts": 0}
    fake_web_client.chat_postMessage.return_value = fake_response

    # Data to create the message
    channel = "GKZ71F9DW"
    user_id = "UFY99RRNU"

    response = handler.start_onboarding(fake_web_client, user_id, channel)
    assert response["ok"]
