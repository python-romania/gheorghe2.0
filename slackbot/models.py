# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""
models.py

This module holds the models for database.
"""

# Local Imports
from app import db

class Score(db.Model):
    """ Score Model. """
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(50))
    score = db.Column(db.Integer)

    def __init__(self, username, score):
        self.username = username
        self.score = score

    def __repr__(self):
        return f"<Score {self.username}={self.score}>"

    def __lt__(self, value):
        return self.score < value.score
    
    def __gt__(self, value):
        return self.score > value.score