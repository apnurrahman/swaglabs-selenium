from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_field = (By.ID, "user-name")
        self.pass_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.cred = {"name": self.name_field, "pass": self.pass_field, "login": self.login_button}
        
        
    
    def input_username(self, username):
        """
        Function to fill in username field in Login page.

        :param username: input string to be filled in.
        :return: None
        """

        # if you use without pointer, it will produce //'using' must be a string error//
        # pointer helps to point the address, not the value since it's one set
        self.driver.find_element(*self.cred["name"]).send_keys(username)
    
    def input_pass(self, password):
        """
        Function to fill in password field in Login page.

        
        :param password: password to be filled in.
        :return: None.
        """
        self.driver.find_element(*self.cred["pass"]).send_keys(password)
    
    def login(self, username="standard_user", password="secret_sauce"):
        """
        Function to simulate login workflow.
        
        :param username: input string to be filled in. Defaults to "standard_user".
        :param password: input string to be filled in. Defaults to "secret_sauce".
        :return: None
        """

        self.driver.get("https://www.saucedemo.com")
        self.input_username(username)
        self.input_pass(password)
        self.driver.find_element(*self.cred["login"]).click()