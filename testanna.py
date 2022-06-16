from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture()
def before_each(request):
    browser.open('https://google.com')


@pytest.fixture()
def size_window(before_each):
    browser.config.window_width = 1200
    browser.config.window_height = 600


@pytest.fixture()
def search_loc(before_each):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()


def positiv_test():
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


@pytest.fixture()
def negativ_test(before_each):
    browser.element('[id="search"]').should(have.text('error'))
