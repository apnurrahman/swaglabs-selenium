from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_field = (By.ID, "user-name")
        self.pass_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.err_msg = (By.CSS_SELECTOR, 'h3[data-test="error"]')
        self.cred = {"name": self.name_field, "pass": self.pass_field, 
                     "login": self.login_button, "err": self.err_msg}
    
    def wait(self, wait=5):
        """
        Function to wait for a specific time. Default waiting time is 5 seconds.
        
        :param wait: seconds to wait
        :return: Explicit wait for x seconds.
        :rtype: WebDriverWait object
        """

        return WebDriverWait(self.driver, wait)
        
    def input_username(self, username):
        """
        Function to fill in username field in Login page.

        :param username: input string to be filled in.
        :return: None
        """

        # using * (asteriks) to unpack
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

    def login_err_conf(self):
        """
        Function to get error message during unsuccessful login.
        
        :param: None
        :return: Error message during login
        :rtype: string
        """
        wait = self.wait()
        err_msg = wait.until(EC.visibility_of_element_located(self.cred["err"]))
        assert "Epic sadface" in err_msg.text, "Couldn't find the error message"