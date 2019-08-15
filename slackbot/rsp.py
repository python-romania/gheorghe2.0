# -*- coding: utf-8 -*-

# Standard imports
import random
from typing import List


class Game:
    """ Rock, Paper, Scissors """

    # Define the list with items
    items: List[str] = [
        "Gun",
        "Lighting",
        "Devil",
        "Dragon",
        "Water",
        "Air",
        "Paper",
        "Sponge",
        "Wolf",
        "Tree",
        "Human",
        "Snake",
        "Scissors",
        "Fire",
        "Rock",
        "Gun",
        "Lighting",
        "Devil",
        "Dragon",
        "Water",
        "Air",
        "Paper",
        "Sponge",
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
            self._player_choice = value

    @property
    def gheorghe_choice(self) -> str:
        """ Get gheorghe choice """
        return self._gheorghe_choice
