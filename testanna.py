from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture()
def test_before_each(request):
    browser.open('https://google.com')


@pytest.fixture()
def test_size_window1(before_each):
    browser.config.window_width = 1200
    browser.config.window_height = 600


@pytest.fixture()
def test_search_loc1(before_each):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()


def test_positiv_test1():
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


@pytest.fixture()
def test_negativ_test(before_each):
    browser.element('[id="search"]').should(have.text('error'))
