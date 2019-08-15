# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""
uiblock.py
Contains the UI block for messages and responses.
"""

# Standard imports
import pathlib

HERE = pathlib.Path(__file__).parent

ABOUT_GROUP = (HERE / "data/about.txt").read_text()
INTRODUCE = (HERE / "data/introduce.txt").read_text()


class Message:
    """ Message UI Block constructor. """

    # Divider block
    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, channel: str, user_id: str, text: str):
        self.channel = channel
        self.username = "gheorghe"
        self.icon_emoji = ":robot_face"
        self.user_id = user_id
        self.text = text
        self.timestamp = ""

    def get_message_payload(self) -> dict:
        """ Return message payload. """
        return {
            "timestamp": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [self._get_message_block(), self.DIVIDER_BLOCK],
        }

    def _get_message_block(self) -> dict:
        """ Return message block. """
        message = {"type": "section", "text": {"type": "mrkdwn", "text": self.text}}
        return message


class OnboardingMessage:
    """
    Onboarding UI bulding message
    """

    # Message block
    WELCOME_BLOCK = {"type": "section", "text": {"type": "mrkdwn", "text": ABOUT_GROUP}}

    # Divider blocnk
    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, channel: str, new_user_id: str) -> None:
        self.channel = channel
        self.username = "gheorghe"
        self.icon_emoji = ":robot_face:"
        self.user_id = new_user_id
        self.timestamp = ""

    def get_message_payload(self) -> dict:
        """
        Returns the message block
        """
        return {
            "timestamp": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self._introduce_yourself_block(),
                self.DIVIDER_BLOCK,
                self.WELCOME_BLOCK,
            ],
        }

    def _introduce_yourself_block(self) -> dict:
        """
        Returns introduce yourself block
        """
        return {"type": "section", "text": {"type": "mrkdwn", "text": INTRODUCE}}
