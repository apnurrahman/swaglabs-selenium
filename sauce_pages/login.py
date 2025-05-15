from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_field = (By.ID, "user-name")
        self.pass_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
    
    def inputUsername(self, username):
        # if you use without pointer, it will produce //'using' must be a string error//
        # pointer helps to point the address, not the value since it's one set
        """
        Fill username form
        """
        self.driver.find_element(*self.name_field).send_keys(username)
    
    def inputPass(self, password):
        """
        Fill password form
        """
        self.driver.find_element(*self.pass_field).send_keys(password)
    
    def login(self, username="standard_user", password="secret_sauce"):
        """
        Attempting to login.
        """
        self.driver.get("https://www.saucedemo.com/v1")
        self.inputUsername(username)
        self.inputPass(password)
        self.driver.find_element(*self.login_button).click()
