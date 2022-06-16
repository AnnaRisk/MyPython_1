from selene.support.shared import browser
from selene import be, have




def test_open_web11():
    browser.open('https://google.com')
    browser.config.window_width = 1200
    browser.config.window_height = 600

    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()

    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


