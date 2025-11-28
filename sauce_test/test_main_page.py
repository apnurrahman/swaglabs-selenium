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
    def test_logout_cart(self, setup):
        login = LoginPage(setup)
        mainPage = MainPage(setup)
        cart = Cart(setup)

        login.login()
        mainPage.add_all_items_to_cart()
        mainPage.nav_cart()
        cart.logout()