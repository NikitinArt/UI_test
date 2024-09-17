import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Edge(options=options)
    browser.maximize_window()
    browser.implicitly_wait(2)
    yield browser
    browser.close()
