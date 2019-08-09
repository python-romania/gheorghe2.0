# -*- coding: utf-8 -*-
# pylint: disable=invalid-name

"""
app.py

Main file. Contains application factory along with the
installed extensions.
"""

# Standard imports
import os
import json

# Third party imports
from flask import Flask, make_response, request


def create_app(development: bool = True) -> Flask:
    """ Application factory """

    flask_app = Flask(__name__)

    # Load configurations
    if development:
        flask_app.config.from_object("config.DevelopmentConfig")
    else:
        flask_app.config.from_object("config.ProductionConfig")

    # Import blueprints
    from website.views import main_app
    from slackbot.endpoint import BOT_APP

    # Register blueprints
    flask_app.register_blueprint(main_app)
    flask_app.register_blueprint(BOT_APP)

    return flask_app


if __name__ == "__main__":
    app = create_app()
