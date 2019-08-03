"""
uiblock.py

Contains the UI block for messages and responses.
"""

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
        return {"timestamp": self.timestamp,
                "channel": self.channel,
                "username": self.username,
                "icon_emoji": self.icon_emoji,
                "blocks":[
                    self._get_message_block(),
                    self.DIVIDER_BLOCK,
                    ],
                }

    def _get_message_block(self) -> dict:
        """ Return message block. """
        message = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": self.text,
                    }
                }
        return message

