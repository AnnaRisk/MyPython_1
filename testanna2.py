from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture()
def open_web():
    browser.open('https://google.com')
    browser.config.window_width = 1200
    browser.config.window_height = 600

def search_loc():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()


def positiv_test():
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))




@pytest.fixture()
def open_web2():
    browser.open('https://google.com')

def search_loc2():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()

def negativ_test2():
    browser.element('[id="search"]').should(have.text('error'))
