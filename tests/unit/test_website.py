# -*- coding: utf-8 -*-
# pylint: disable=invalid-name

"""
test_website.py
"""

# Third party imports
from flask.testing import FlaskClient

def test_home_page(client_fixture: FlaskClient) -> None:
    """ Test website home page. """
    response = client_fixture.get("/")
    assert response.status == "200 OK"
    html = response.get_data(as_text=True)
    assert "<title>Python Study Group</title>" in html
