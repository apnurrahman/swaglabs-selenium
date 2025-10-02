from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_field_loc = (By.ID, "user-name")
        self.pass_field_loc = (By.ID, "password")
        self.login_button_loc = (By.ID, "login-button")
    
    def input_username(self, username):
        """
        This function fills in username inside username form field.

        Args:
            username: input string to be filled in.
        """

        # if you use without pointer, it will produce //'using' must be a string error//
        # pointer helps to point the address, not the value since it's one set
        self.driver.find_element(*self.name_field_loc).send_keys(username)
    
    def input_pass(self, password):
        """
        This function fills in password inside password form field.

        Args:
            password: input string to be filled in.
        """
        self.driver.find_element(*self.pass_field_loc).send_keys(password)
    
    def login(self, username="standard_user", password="secret_sauce"):
        """
        Function to simulate login flow.

        Args:
            username: input string to be filled in. Defaults to "standard_user".
            password: input string to be filled in. Defaults to "secret_sauce".
        """

        self.driver.get("https://www.saucedemo.com")
        self.input_username(username)
        self.input_pass(password)
        self.driver.find_element(*self.login_button_loc).click()