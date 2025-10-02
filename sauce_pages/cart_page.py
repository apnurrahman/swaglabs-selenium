from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cart:
    def __init__(self, driver):
            self.driver = driver
            self.cont_shop_loc = (By.PARTIAL_LINK_TEXT, "Shopping")
            self.checkout_loc = (By.PARTIAL_LINK_TEXT, "CHECKOUT")
            self.remove_loc = (By.CSS_SELECTOR, "button.btn_secondary.cart_button")
            self.inspect_loc = (By.CLASS_NAME, "inventory_item_name")
            self.logout_loc = (By.ID, "logout_sidebar_link")
            
    def back_to_main_page(self):
          self.driver.find_element(*self.cont_shop_loc).click()
    
    def remove_item(self, product=""):
          """
          Function to remove specific item from cart.
          
          Args:
            product: string equivalent of said product.
          """
          
          # look for items
          cart_items = ''
          try:
                cart_items = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                                                  ((By.CLASS_NAME, "inventory_item_name")))
          except NoSuchElementException:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                cart_items = self.driver.find_elements(*self.inspect_loc)
          else: 
                for item in cart_items:
                      if item.text == product:
                            pass
                      

    
    def inspect_item(self, item=""):
          """
          Checking product details.
          """
          pass
    
    def checkout(self):
          """
          Function to simulate checkout flow. Navigate to checkout page.
          """

          self.driver.find_element(*self.checkout_loc).click()

    def logout(self):
          """
          Function to simulate logout flow. Navigate to login page.
          """
          
          self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
          #self.driver.find_element(By.ID, "react-burger-menu-btn").click()
          burger = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
          burger.click()
          #self.driver.find_element(*self.logout_loc).click()
          logout_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
          logout_button.click()
          
          login_button = self.driver.find_element(By.ID, "login-button")
          assert "Login" in login_button.get_attribute("value")
