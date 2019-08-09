# -*- coding: utf-8 -*-
"""
test_commands.py
Contains all the test for slash commands.
"""

# Standard imports
import json
from unittest.mock import patch, MagicMock

# Third party imports
from flask.testing import FlaskClient

# Local imports


@patch("slackbot.endpoint.verify_signing")
def test_test_command(fake_verify_signing: MagicMock, client: FlaskClient) -> None:
    """ Test test slash command. """
    data = {"user_name": "madalin"}
    fake_verify_signing.return_value = True
    response = client.post(path="/slack/test", data=json.dumps(data), content_type="application/json")
    assert response.status == "200 OK"
