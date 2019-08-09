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

# Define slack web client
WEB_CLIENT = slack.WebClient(os.getenv("SLACK_BOT_TOKEN"))

# Define blueprint
BOT_APP = Blueprint("BOT_APP", __name__)

# Compute Signing
def verify_signing(body: str) -> True:
    """ Veryfiy the Slack Signing Secret Key """

    # Get slack Request timestamp
    timestamp = request.headers.get('X-Slack-Request-Timestamp')

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
    if slack_event.get("token") != os.getenv("VERIFICATION"):
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
        return make_response("Bad response from team_join event.", 404, {"X-Slack-No-Retry": 1})
    return make_response("Unhandled event", 404, {"X-Slack-No-Retry": 1})


# Implementing a hello command.
@BOT_APP.route("/slack/hello", methods=["POST"])
def hello():
    """ /hello command. Say hello to gheorghe. """
    data = request.get_data(as_text=True)

    if verify_signing(data):
        if request.form["user_name"]:
            message = f"Hello {request.form['user_name']}"
            response = {"response_type": "in_channel", "text": message, }
            response_to_be_sent = json.dumps(response)
            content_type = {"Content-Type": "application/json"}
            return make_response(response_to_be_sent, 200, content_type)
    return make_response("I'm sorry. I don't understand.", 200, {"X-Slack-No-Retry": 1})

# A simple text command used for experimenting.
@BOT_APP.route("/slack/test", methods=["POST"])
def test() -> None:
    """ Simple Test command. """
    data = request.get_data(as_text=True)
    content_type = {"Content-Type": "application/json"}

    if verify_signing(data):
        message = "This is a simple test!"
        response = {"response_type": "in_channel", "text": message, }
        response_to_be_sent = json.dumps(response)
        return make_response(response_to_be_sent, 200, content_type)
    return make_response("Error!", 200, content_type)