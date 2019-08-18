# -*- coding: utf-8 -*-
# pylint: disable=invalid-name

"""
app.py

Main file. Contains application factory along with the
installed extensions.
"""

# Third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Setup database
db = SQLAlchemy()

def create_app(development: bool = True) -> Flask:
    """ Application factory """
    flask_app = Flask(__name__)
    
    # Load configurations
    if development:
        flask_app.config.from_object("config.DevelopmentConfig")
    else:
        flask_app.config.from_object("config.ProductionConfig")

    # Initialize database
    db.init_app(flask_app)
    migrate = Migrate(flask_app, db) 

    # Import blueprints
    from website.views import main_app
    from slackbot.endpoint import BOT_APP

    # Register blueprints
    flask_app.register_blueprint(main_app)
    flask_app.register_blueprint(BOT_APP)
    return flask_app