# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""
endpoint.py

Contains the slack api endpoint.
"""
# Standard imports
import os
import hmac
import json
import hashlib

# Third party imports
import slack
from flask import Blueprint, request, make_response

# Local imports
from slackbot import handler
from slackbot.rsp import Game

# Define slack web client
WEB_CLIENT = slack.WebClient(os.getenv("SLACK_BOT_TOKEN"))

# Define blueprint
BOT_APP = Blueprint("BOT_APP", __name__)

# Compute Signing
def verify_signing(body: str) -> True:
    """ Veryfiy the Slack Signing Secret Key """

    # Get slack Request timestamp
    timestamp = request.headers.get("X-Slack-Request-Timestamp")

    # Get slack signiture
    slack_signature = request.headers.get("X-Slack-Signature")

    # Get request body
    body = body

    # Build the basestring
    sig_basestring = str.encode(f"v0:{timestamp}:{body}")

    # Get the secret key
    slack_signing_secret = str.encode(os.getenv("SIGNING_SECRET"))

    # Create the hash
    my_signiture = f"v0={hmac.new(slack_signing_secret, sig_basestring, hashlib.sha256).hexdigest()}"

    # Test Signature
    if hmac.compare_digest(my_signiture, slack_signature):
        return True
    return False


@BOT_APP.route("/slack", methods=["GET", "POST"])
def listening():
    """ Listening for envents coming form slack. """
    slack_event = {}

    if request.data:
        slack_event = json.loads(request.data)

    content_type = {"content_type": "application/json"}

    # Return challenge
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, content_type)

    # Check received token
    if not verify_signing(request.get_data(as_text=True)):
        message = "Invalid token"
        return make_response(message, 403, {"X-Slack-No-Retry": 1})

    # Check for team_join event
    if "event" in slack_event:
        if slack_event["event"]["type"] == "team_join":
            user = slack_event["event"]["user"]
            channel = slack_event["event"]["channel"]
            response = handler.start_onboarding(WEB_CLIENT, user, channel)
            if response["ok"]:
                return make_response("Team join event.", 200, {"X-Slack-No-Retry": 1})
        return make_response(
            "Bad response from team_join event.", 404, {"X-Slack-No-Retry": 1}
        )
    return make_response("Unhandled event", 404, {"X-Slack-No-Retry": 1})


# A simple text command used for experimenting.
@BOT_APP.route("/slack/test", methods=["POST"])
def test() -> None:
    """ Simple Test command. """
    data = request.get_data(as_text=True)
    content_type = {"Content-Type": "application/json"}

    if verify_signing(data):
        message = f"Hello {request.form.to_dict()['user_name']}!"
        response = {"response_type": "in_channel", "text": message}
        response_to_be_sent = json.dumps(response)
        return make_response(response_to_be_sent, 200, content_type)
    return make_response("Error!", 200, content_type)


@BOT_APP.route("/slack/rsp", methods=["POST"])
def rsp() -> None:
    """ RSP command """
    data = request.get_data(as_text=True)
    content_type = {"Content-Type": "application/json"}

    if verify_signing(data):
        # Request data
        request_data = request.form.to_dict()

        # Extract the user item
        player_choice = request_data["text"].split(" ")

        # Start a new game
        game = Game(player_choice[0])
        if not game.calculate():
            response = {
                "response_type": "in_channel",
                "text": "Please chose a valid item if you wanna play!",
            }
            return make_response(json.dumps(response), 200, content_type)
        if game.calculate():
            if game.player_choice == game.gheorghe_choice:
                text = f"Nice try, it's a draw! My choice was: {game.gheorghe_choice}"
                response = {"response_type": "in_channel", "text": text}
                return make_response(json.dumps(response), 200, content_type)
            elif game.gheorghe_choice in game.calculate():
                text = f"I won! My choice was: {game.gheorghe_choice}"
                response = {"response_type": "in_channel", "text": text}
                return make_response(json.dumps(response), 200, content_type)
            else:
                text = f"You won! My choice was: {game.gheorghe_choice}"
                response = {"response_type": "in_channel", "text": text}
                return make_response(json.dumps(response), 200, content_type)
    return make_response("Error!", 200, content_type)


@BOT_APP.route("/slack/items", methods=["POST"])
def rsp_items() -> None:
    """ RSP Items Command """
    data = request.get_data(as_text=True)
    content_type = {"Content-Type": "application/json"}

    if verify_signing(data):
        items = [
            "1. *Rock*, *Gun*, *Lighting*",
            "2. *Devil*, *Dragon*, *Water*",
            "3, *Air*, *Paper*, *Sponge*",
            "4. *Wolf*, *Tree*, *Human*",
            "5. *Snake*, *Scissors*, *Fire*",
        ]
        message = "\n".join(items)
        response_url = request.form.to_dict()["response_url"]
        response = {
            "response_type": "in_channel",
            "text": message,
            "response_url": response_url,
        }
        response_to_be_sent = json.dumps(response)
        return make_response(response_to_be_sent, 200, content_type)
    return make_response("Error!", 200, content_type)
