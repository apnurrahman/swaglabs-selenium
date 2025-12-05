from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import random

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_item = (By.CSS_SELECTOR, "button.btn_primary.btn_inventory")
        self.conf_item = (By.CSS_SELECTOR, "button.btn_secondary.btn_inventory")
        self.logout_link = (By.ID, "logout_sidebar_link")
        self.filter = (By.CSS_SELECTOR, "select.product_sort_container")
        self.login = (By.CSS_SELECTOR, "span.title")
        self.cart = (By.CSS_SELECTOR, "a.shopping_cart_link")
        self.locators = {"add": self.add_item, "conf_item": self.conf_item, "logout": self.logout_link, 
                           "filter": self.filter, "login": self.login, "cart": self.cart}
    
    def scroll_within_page(self):
        """
        Function to scroll anywhere within the page
        
        :param: None
        :return: None
        :rtype: None
        """
        pass

    def login_conf(self):
        """
        Function to confirm successful login.

        :param: None
        :return: Confirmation whether login successful or denied.
        :rtype: None
        """
        assert "Product" in self.driver.find_element(*self.locators["login"]).text
        
    
    def select_product(self, product=""):
        """
        Selecting a single product. Insert product number. Number will be randomized if it's not written
        """
        count = 0
        item_selected = product
        
        if item_selected is None:
            item_selected = random.randint(0, 5)
        
        #finding product
        while(count<=2):
            try:
                self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
                get_all_products = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
            except NoSuchElementException as NE:
                print("Element not found. Scrolling down..")
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                count+=1
        for product in get_all_products:
            sel_prod = product.find_element(By.CSS_SELECTOR, "div.inventory_item_label")
            id_value = sel_prod.find_element(By.TAG_NAME, "id").get_attribute("id")
            finding_id = id_value.split("_")
            if finding_id[1] == item_selected:
                pass
       
        #selecting button
        while(count <= 2):
            try:
                self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
                selected_prod = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "pricebar")))
                selected_prod.click()
                break
            except NoSuchElementException as NE: 
                print("No such element is found.")
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                count+=1
        #clicked_prod = self.driver.find_element(*self.conf_item_loc)     
    
    def logout(self):
        """
        Function to simulate logout action. It opens button on the top left.

        :param: None
        :return: None
        :rtype: None
        """

        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        burger = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located
                                                      ((By.ID, "react-burger-menu-btn")))
        burger.click()
        log_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located
                                                         ((By.ID, "logout_sidebar_link"))).click()

        login_button = self.driver.find_element(By.ID, "login-button")
        assert "Login" in login_button.get_attribute("value")
    #def click_conf_items(self, )

    def nav_cart(self):
        """
        Function to navigate to Cart page.

        :param: None
        :return: None
        :rtype: None
        """
        self.driver.find_element(*self.locators["cart"]).click()
        