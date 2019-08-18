# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""
test_models.py

This module holds tests for slackbot models.
"""
# Local imports
from slackbot.models import Score

def test_score() -> None:
    """ Test Score instance. """
    score = Score("madalin", 1)
    assert isinstance(score, Score)

def test_score_attributes() -> None:
    """ Test score attributes. """
    assert hasattr(Score, "id")
    assert hasattr(Score, "username")
    assert hasattr(Score, "score")

def test_score_attributes_value() -> None:
    """ Test values for attributes. """
    score = Score("madalin", 1)
    
    assert score.username == "madalin"
    assert score.score == 1

    # Test representation
    assert repr(score) == "<Score madalin=1>"