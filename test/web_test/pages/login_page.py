from test.web_test.pages.page_base import PageBase
from test.web_test.helpers.element import Element
from munch import munchify


class loginPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        page_elements = {

            'Email': Element('//input[@id="Email"]', self),
            'Password': Element('//input[@id="Password"]', self),
            'loginbutton': Element('//button[@Class="button-1 login-button"]', self),
            
            
        }

        self.elements = munchify(page_elements)


    def login(self, email, password):
        self.elements.Email.set(email)
        self.elements.Password.set(password)
        self.elements.loginbutton.click()




