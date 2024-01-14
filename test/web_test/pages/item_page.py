from test.web_test.pages.page_base import PageBase
from test.web_test.helpers.element import Element
from munch import munchify


class itemPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        page_elements = {

            'addToCart': Element('/html/body/div[6]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[3]/div[2]/button[1]', self),

            
            
        }

        self.elements = munchify(page_elements)


    def login(self, email, password):
        self.elements.Email.set(email)
        self.elements.Password.set(password)
        self.elements.loginbutton.click()




