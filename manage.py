# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""
manage.py
Entrypoint of the app.
"""
from app import create_app

app = create_app()