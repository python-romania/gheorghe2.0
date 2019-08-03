"""
handler.py

Contains all the event handlers.
"""
# Standard lib imports
from typing import Optional

# Third party imports
import slack

# Local imports
from .uiblock import Message

def message_handler(web_client: slack.WebClient, channel_id: str, user_id: Optional[str], text:
        Optional[str]) -> dict:
    """ Send message """

    # Instantiate message block UI
    msg_block = Message(channel_id, user_id, text)

    # Create message block
    message_to_be_sent = msg_block.get_message_payload()

    # Send the message
    response = web_client.chat_postMessage(**message_to_be_sent)

    return response
