# -*- coding: utf-8 -*-
# pylint: disable=invalid-name

"""
config.py
Holds configuration for different development environments.
"""

# Standard imports
import os

# Base class configuration
class BaseConfig:
    """
    Base settings. Holds default settings
    for all environments.
    """
    # Environment setup
    DEBUG = False
    TESTING = False
    DB_SERVER = "localhost"
    
    

# Production configuration
class ProductionConfig(BaseConfig):
    """
    Production settings. Holds additional settings
    for production environment.
    """
    DB_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True 

class TestConfig(BaseConfig):
    """
    Test settings. Holds additional settings for
    test environment.
    """
    DEBUG = True
    


# Development configuration
class DevelopmentConfig(BaseConfig):
    """
    Development settings. Holds additional settings
    for development environment.
    """
    DEBUG = True
    # Database setup
    SECRET_KEY = os.getenv("SECRET_KEY")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    DB_URI = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DATABASE_NAME}"
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
