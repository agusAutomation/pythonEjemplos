import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver


# Constante
STORE_WEB = 'https://automationteststore.com/index.php?rt=account/login'


@pytest.fixture
def browser():
    b = webdriver.Firefox()
    #b = webdriver.Chrome('../../Drivers/chromedriver.exe')
    #b.maximize_window()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given Steps
@given('the Login Store webPage')
@given('the search is in the header')
def open_store_web(browser):
    browser.get(STORE_WEB)
    print('Open Store webPage')
