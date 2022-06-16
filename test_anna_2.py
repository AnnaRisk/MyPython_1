from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture()
def test_open_web():
    browser.open('https://google.com')
    browser.config.window_width = 1200
    browser.config.window_height = 600


def test_search_loc():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()


def test_positiv():
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


@pytest.fixture()
def test_open_web2():
    browser.open('https://google.com')


def test_search_loc2():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()


def test_negativ_test2():
    browser.element('[id="search"]').should(have.text('error'))
