from selenium.webdriver.common.by import By

class Cart:
    def __init__(self, driver):
            self.driver = driver
            self.cont_shop_loc = (By.PARTIAL_LINK_TEXT, "Shopping")
            self.checkout_loc = (By.PARTIAL_LINK_TEXT, "CHECKOUT")
            self.remove_loc = (By.CSS_SELECTOR, "button.btn_secondary.cart_button")
            self.inspect_loc = (By.CLASS_NAME, "inventory_item_name")
    
    def back_to_main_page(self):
          self.driver.find_element(*self.cont_shop_loc).click()
    
    def remove_item(self, item):
          pass
    
    def inspect_item(self, item):
          pass
    
    def checkout(self):
          self.driver.find_element(*self.checkout_loc).click()
