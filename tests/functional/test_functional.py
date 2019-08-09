# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""
functional_test.py
"""

# Third party imports
import pytest
from selenium import webdriver

@pytest.fixture
def driver_fixture() -> webdriver.Firefox():
    """ Setup function. """
    driver = webdriver.Firefox()
    driver.get("http://localhost:5000/")
    yield driver
    driver.close()

def test_website_title(driver_fixture: webdriver.Firefox) -> None:
    """ Test website title main page. """
    assert "Python Study Group" in driver_fixture.title

def test_website_headers(driver_fixture: webdriver.Firefox) -> None:
    """ Test website headers. """
    heading4 = driver_fixture.find_elements_by_tag_name("h4")
    heading3 = driver_fixture.find_elements_by_tag_name("h3")
    assert "Python Study Group" in heading3[0].text
    assert "Our Mission" in heading4[0].text
    assert "Join the Community!" in heading4[1].text

def test_github_button(driver_fixture: webdriver.Firefox) -> None:
    """ Test github button redirect. """
    github_button = driver_fixture.find_element_by_id("github-btn")
    github_button.click()
    current_url = driver_fixture.current_url
    assert current_url == "https://github.com/python-romania"
    assert "GitHub" in driver_fixture.title

def test_slack_button(driver_fixture: webdriver.Firefox) -> None:
    """ Test slack button redirect. """
    slack_button = driver_fixture.find_element_by_id("slack-btn")
    slack_button.click()
    current_url = driver_fixture.current_url
    expected_url = "https://pythonromania.slack.com/join/"
    assert expected_url in current_url
    assert "Slack" in driver_fixture.title
