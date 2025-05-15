from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_item = (By.CSS_SELECTOR, "button.btn_primary.btn_inventory")
        self.conf_item = (By.CSS_SELECTOR, "button.btn_secondary.btn_inventory")
        self.logout_link = (By.ID, "logout_sidebar_link")
        self.filter = (By.CSS_SELECTOR, "select.product_sort_container")
        self.conf = (By.CLASS_NAME, "product_label")

    def login_conf(self):
        return self.driver.find_element(*self.conf).text
    
    def select_product(self, product):
        pass

    def add_all_items_to_cart(self):
        count = 0
        while(count <= 3):
            try:
                catch = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located
                                                        ((By.CLASS_NAME, "pricebar")))
            except NoSuchElementException as ne:
                print("No such element is found.")
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                count+=1
            else:
                for item in catch:
                    cart_button = item.find_element(*self.add_item)
                    assert "ADD TO CART" in cart_button.text
                    cart_button.click()
                break     
    
    def logout(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        burger = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                                      ((By.CLASS_NAME, "bm-burger-button")))
        burger.click()

        self.driver.find_element(*self.logout_link).click()
    #def click_conf_items(self, )
        