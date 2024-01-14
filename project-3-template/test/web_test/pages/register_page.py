from test.web_test.pages.page_base import PageBase
from test.web_test.helpers.element import Element
from munch import munchify


class RegisterPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        page_elements = {
            'gender': Element('//input[@id="gender-male"]', self),
            'Firstname': Element('//input[@id="FirstName"]', self),
            'Lastname': Element('//input[@id="LastName"]', self),
            'Email': Element('//input[@id="Email"]', self),
            'Password': Element('//input[@id="Password"]', self),
            'Confirmpassword': Element('//input[@id="ConfirmPassword"]', self),
            'registerButton': Element('//button[@id="register-button"]', self),
            
            'Continue': Element('//a[@class="button-1 register-continue-button"]', self),
            'result': Element('//div[@class="result"]', self)

            
        }

        self.elements = munchify(page_elements)


    def register(self, firstname, lastname, email, password, confirmpassword):
        self.elements.gender.click()
        self.elements.Firstname.set(firstname)
        self.elements.Lastname.set(lastname)
        self.elements.Email.set(email)
        self.elements.Password.set(password)
        self.elements.Confirmpassword.set(confirmpassword)
        self.elements.registerButton.click()
