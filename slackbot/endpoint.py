"""
endpoint.py

Contains the slack api endpoint.
"""
# Standard imports
import os
import json

# Third party imports
from flask import Blueprint, request, make_response

# Define blueprint
bot_app = Blueprint("bot_app", __name__)

@bot_app.route("/slack", methods=["GET", "POST"])
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

    # Check for any event
    if "event" in slack_event:
        print(slack_event)

    return make_response("Unhandled event", 404, {"X-Slack-No-Retry": 1})
