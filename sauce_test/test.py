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

#@pytest.mark.skip(reason="success")
@pytest.mark.usefixtures(setup)
@pytest.mark.login
class TestLogin():
    def test_valid_login(self, setup):
        login = LoginPage(setup)
        main_page = MainPage(setup)
        login.login("standard_user", "secret_sauce")
        main_page.login_conf()
        main_page.logout()
    
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
        main_page = MainPage(setup)
        login.login()
        main_page.add_all_items_to_cart()
        main_page.logout()

@pytest.mark.usefixtures("setup")
class TestCart():
    def test_logout_cart(self, setup):
        login = LoginPage(setup)
        mainPage = MainPage(setup)
        cart = Cart(setup)

        login.login()
        mainPage.add_all_items_to_cart()
        mainPage.nav_cart()
        cart.logout()