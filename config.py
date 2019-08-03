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
    SECRET_KEY = os.getenv("SECRET_KEY")

# Production configuration
class ProductionConfig(BaseConfig):
    """
    Production settings. Holds additional settings
    for production environment.
    """
    pass

# Development configuration
class DevelopmentConfig(BaseConfig):
    """
    Development settings. Holds additional settings
    for development environment.
    """
    DEBUG = True
