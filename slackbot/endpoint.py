"""
endpoint.py

Contains the slack api endpoint.
"""
# Standard imports
import os
import json

# Third party imports
import slack
from flask import Blueprint, request, make_response

# Local imports
from . import handler

# Define slack web client
web_client = slack.WebClient(os.getenv("SLACK_BOT_TOKEN"))

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
        if slack_event["event"]["type"] == "team_join":
            user = slack_event["event"]["user"]
            channel = slack_event["event"]["channel"]

            response = handler.start_onboarding(web_client, user, channel)
            if response["ok"]:
                return make_response("Team join event.", 200, {"X-Slack-No-Retry": 1})

        return make_response("Bad response.", 403, {"X-Slack-No-Retry": 1})


    return make_response("Unhandled event", 404, {"X-Slack-No-Retry": 1})
