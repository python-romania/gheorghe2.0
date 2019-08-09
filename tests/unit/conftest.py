# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""
conftest.py

Holds module fixtures.
"""

# Third party imports
import pytest
from flask import Flask

# Local imports
from app import create_app

@pytest.fixture()
def client_fixture(scope="module") -> Flask:
    """ App instance setup. """
    app = create_app()
    with app.test_client() as client:
        yield client
