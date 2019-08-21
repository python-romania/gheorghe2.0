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
def test_test_command(fake_signing: MagicMock, client: FlaskClient) -> None:
    """ Test test slash command. """
    data = "user_name=madalin&text=test text"
    fake_signing.return_value = True
    content_type = "application/x-www-form-urlencoded"
    response = client.post(path="/slack/test", data=data, content_type=content_type)
    assert response.status == "200 OK"
    assert "Hello madalin!" in str(response.data)


@patch("slackbot.endpoint.verify_signing")
def test_rsp_command(fake_signing: MagicMock, client: FlaskClient) -> None:
    """ Test rsp slash command """
    data = "user_name=madalin&text=rock&response_url=response"
    fake_signing.return_value = True
    content_type = "application/x-www-form-urlencoded"

    # Draw game
    fgame = MagicMock()
    fgame.return_value.player_choice = "rock"
    fgame.return_value.gheorghe_choice = "rock"

    with patch("slackbot.endpoint.Game", fgame):
        response = client.post(path="/slack/rsp", data=data, content_type=content_type)
        assert response.status == "200 OK"
        assert "draw" in str(response.data)

    # Player Win game
    fgame = MagicMock()
    fgame.return_value.player_choice = "dragon"
    fgame.return_value.gheorghe_choice = "rock"

    with patch("slackbot.endpoint.Game", fgame):
        response = client.post(path="/slack/rsp", data=data, content_type=content_type)
        assert response.status == "200 OK"
        assert "You won" in str(response.data)

    # Gheorghe win game
    fgame = MagicMock()
    fgame.return_value.player_choice = "rock"
    fgame.return_value.gheorghe_choice = "dragon"
    fgame.return_value.calculate.return_value = ["dragon"]

    with patch("slackbot.endpoint.Game", fgame):
        response = client.post(path="/slack/rsp", data=data, content_type=content_type)
        assert response.status == "200 OK"
        assert "I won" in str(response.data)

@patch("slackbot.endpoint.verify_signing")
def test_list_items(fake_signing: MagicMock, client: FlaskClient) -> None:
    """ Test list items command """
    data = "user_name=madalin&text=Rock&response_url=response"
    fake_signing.return_value = True
    content_type = "application/x-www-form-urlencoded"
    response = client.post(path="/slack/items", data=data, content_type=content_type)
    assert response.status == "200 OK"
    assert "Rock" in str(response.data)

@patch("slackbot.endpoint.verify_signing")
def test_score(fake_signing: MagicMock, client: FlaskClient) -> None:
    """ Test score command """
    data = "user_name=madalin&text=rock&response_url=response"
    fake_signing.return_value = True
    content_type = "application/x-www-form-urlencoded"
    response = client.post(path="/slack/score", data=data, content_type=content_type)
    assert response.status == "200 OK"