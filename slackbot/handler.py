# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""
handler.py
Contains all the event handlers.
"""

# Standard lib imports
from typing import Optional

# Third party imports
import slack

# Local imports
from .uiblock import Message, OnboardingMessage

# In memory storage
ONBOARDING_MESSAGE_LOG: dict = {}


def start_onboarding(web_client: slack.WebClient, new_user_id: str, channel: str) -> dict:
    """ Send onboarding message. """

    # Build the message
    onboarding_message = OnboardingMessage(channel=channel, new_user_id=new_user_id)

    # Get the message
    message_to_be_sent = onboarding_message.get_message_payload()

    # Send the message to user
    response = web_client.chat_postMessage(**message_to_be_sent)

    # Get the timestamp
    onboarding_message.timestamp = response["ts"]

    # Log the message sent
    if channel not in ONBOARDING_MESSAGE_LOG:
        ONBOARDING_MESSAGE_LOG["channel"] = {}
    ONBOARDING_MESSAGE_LOG["channel"]["user_id"] = onboarding_message

    return response


def message_handler(web_client: slack.WebClient,
                    channel_id: str, user_id: Optional[str], text: Optional[str]) -> dict:
    """ Send message """

    # Instantiate message block UI
    msg_block = Message(channel_id, user_id, text)

    # Create message block
    message_to_be_sent = msg_block.get_message_payload()

    # Send the message
    response = web_client.chat_postMessage(**message_to_be_sent)

    return response
