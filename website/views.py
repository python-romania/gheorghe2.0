# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""
views.py

Contains the blueprings and routes to main site pages.
"""
# Third party imports
from flask import Blueprint, render_template

# Define blueprint
main_app = Blueprint("main_app", __name__)


@main_app.route("/")
def index() -> render_template:
    """ Site home page. """
    return render_template("website/index.html")
