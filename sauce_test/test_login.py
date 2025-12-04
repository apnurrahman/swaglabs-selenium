import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sauce_pages.login_page import LoginPage
from sauce_pages.main_page import MainPage
from sauce_pages.cart_page import Cart

@pytest.fixture
def setup():
    #start incognito to prevent annoying password breached message
    ch_options = webdriver.ChromeOptions()
    ch_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=ch_options)
    yield driver
    driver.quit()

@pytest.mark.login
class TestLogin():
    def test_valid_login(self, setup):
        login = LoginPage(setup)
        mainPage = MainPage(setup)
        login.login("standard_user", "secret_sauce")
        mainPage.login_conf()
        mainPage.logout()
    
    def test_invalid_login(self, setup):
        login = LoginPage(setup)
        mainPage = MainPage(setup)
        login.login("standarduser")
        login.login_err_conf()