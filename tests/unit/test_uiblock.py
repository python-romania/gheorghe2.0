"""
test_uiblock.py

Contains the test for uiblock module.
"""
from slackbot import uiblock


def test_message_block() -> None:
    """ Test the message block. """
    channel = "GKZ71F9DW"
    user_id = "UFY99RRNU"
    text = "Hello World!"
    message_block = uiblock.Message(channel, user_id, text)

    assert message_block.channel == channel
    assert message_block.username == "gheorghe"
    assert message_block.icon_emoji == ":robot_face"
    assert message_block.user_id == user_id
    assert message_block.text == text
    assert message_block.timestamp == ""

    payload = message_block.get_message_payload()
    assert type(payload) == dict


def test_onboarding_block() -> None:
    """ Test the onboarding ui block. """
    channel = "GKZ71F9DW"
    user_id = "UFY99RRNU"
    text = "Hello World!"
    onboarding_block = uiblock.OnboardingMessage(channel, user_id)

    assert onboarding_block.channel == channel
    assert onboarding_block.username == "gheorghe"
    assert onboarding_block.icon_emoji == ":robot_face:"
    assert onboarding_block.user_id == user_id
    assert onboarding_block.timestamp == ""

    payload = onboarding_block.get_message_payload()
    assert type(payload) == dict
    assert "Salutare" in payload["blocks"][0]["text"]["text"]
    assert "grup" in payload["blocks"][2]["text"]["text"]
