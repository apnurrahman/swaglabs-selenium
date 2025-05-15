import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sauce_pages.login import LoginPage
from sauce_pages.mainPage import MainPage
from sauce_pages.cart import Cart

@pytest.fixture
def setup():
    #start incognito to prevent annoying password breached message
    ch_options = webdriver.ChromeOptions()
    ch_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=ch_options)
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestLogin():
    def test_valid_login(self, setup):
        login = LoginPage(setup)
        mainPage = MainPage(setup)
        login.login("standard_user", "secret_sauce")
        assert "Products" in mainPage.login_conf()
        mainPage.logout()
    
    def test_multiple_valid_login(self, setup):
        #for user other than 'standard_user' will experience problem. That was no accident. It was by design.
        login = LoginPage(setup)
        mainPage = MainPage(setup)

        usernames = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]
        for username in usernames:
            login.login(username)
            assert "Products" in mainPage.login_conf()
            mainPage.logout()
    
@pytest.mark.usefixtures("setup")
class TestMainPage():
    def test_add_to_cart(self, setup):
        login = LoginPage(setup)
        mainPage = MainPage(setup)
        login.login()
        mainPage.add_all_items_to_cart()
        mainPage.logout()

@pytest.mark.usefixtures("setup")
class TestCart():
    def something(self, setup):
        pass
