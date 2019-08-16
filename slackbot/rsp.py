# -*- coding: utf-8 -*-

# Standard imports
import random
from typing import List


class Game:
    """ Rock, Paper, Scissors """

    # Define the list with items
    items: List[str] = [
        "gun",
        "lighting",
        "devil",
        "dragon",
        "water",
        "air",
        "paper",
        "sponge",
        "wolf",
        "tree",
        "human",
        "snake",
        "scissors",
        "fire",
        "rock",
        "gun",
        "lighting",
        "devil",
        "dragon",
        "water",
        "air",
        "paper",
        "sponge",
    ]

    def __init__(self, player_choice: str):
        self._player_choice = player_choice
        self._gheorghe_choice = random.choice(Game.items)

    @property
    def player_choice(self) -> str:
        """ Get player choice """
        return self._player_choice

    @player_choice.setter
    def player_choice(self, value) -> None:
        """ Set player choice """
        if type(value) == str:
            self._player_choice = value.lower()

    @property
    def gheorghe_choice(self) -> str:
        """ Get gheorghe choice """
        return self._gheorghe_choice

    def calculate(self) -> List[str]:
        """ Get the list with elements wich can beat player """

        if self._player_choice not in Game.items:
            return None

        player_choice_index = Game.items.index(self._player_choice)

        return Game.items[player_choice_index + 1 : player_choice_index + 8]
