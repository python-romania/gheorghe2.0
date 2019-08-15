# -*- coding: utf-8 -*-
# pylint: disable=invalid-name

"""
test_game.py
This file holds tests for rock, paper, sicissors game
"""
from importlib import reload
from unittest import mock

import pytest

from slackbot import rsp


@pytest.fixture
def game() -> rsp.Game:
    """ Game setup """
    g = rsp.Game("rock")
    return g


def test_game_instance(game: game) -> None:
    """ Test game instance """
    # Test game instance
    assert game is not None

    # Test attributes
    assert hasattr(rsp.Game, "items")
    assert hasattr(game, "player_choice")
    assert hasattr(game, "gheorghe_choice")


def test_game_items() -> None:
    """ Test game items list """
    assert type(rsp.Game.items) == list
    assert len(rsp.Game.items) == 23


def test_player_choice(game: game) -> None:
    """ Test player choice """
    assert type(game.player_choice) == str
    assert game.player_choice == "rock"


def test_gheorghe_choice() -> None:
    """ Test gheorghe choice """
    with mock.patch("random.choice", lambda seq: seq[0]):
        reload(rsp)
        game = rsp.Game("Rock")
        assert game.gheorghe_choice == "Gun"
    reload(rsp)


def test_game_calculate(game: game) -> None:
    """ Test calculate method """

    # Test item not in the list
    result = game._calculate()
    assert not result

    # Test returning next 7 items


def test_game_winner(game: game) -> None:
    """ Test winner method """
