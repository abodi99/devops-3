from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from assertpy import assert_that
from selenium.common.exceptions import TimeoutException

class Element:

    def __init__(self, locator, page):
        self.page = page
        self.locator = locator

    def find(self):
        self.page.wait.until(EC.presence_of_element_located((By.XPATH, self.locator)))
        return self

    def click(self):
        self.page.wait.until(EC.element_to_be_clickable((By.XPATH, self.locator))).click()
        return self

    def set(self, value):
        element = self.page.wait.until(EC.element_to_be_clickable((By.XPATH, self.locator)))
        element.clear()
        element.send_keys(value)
        return self
    
    def is_displayed(self):
        try: 
            element = self.page.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator)))
            return True
        except TimeoutException:
            return False
        

    def get_text(self):
        try:
            element = self.page.wait.until(EC.visibility_of_element_located((By.XPATH, self.locator)))
            return element.text
        except TimeoutException:
            return None
        
    



    @property
    def text(self):
        return self.page.wait.until(EC.presence_of_element_located((By.XPATH, self.locator))).text