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

def create_app(development: bool =True) -> Flask:
    """ Application factory """

    app = Flask(__name__)

    # Load configurations
    if development:
        app.config.from_object("config.DevelopmentConfig")
    else:
        app.config.from_object("config.ProductionConfig")

    # Import blueprints
    from website.views import main_app
    from slackbot.endpoint import bot_app

    # Register blueprints
    app.register_blueprint(main_app)
    app.register_blueprint(bot_app)

    return app


if __name__ == "__main__":
    app = create_app()
