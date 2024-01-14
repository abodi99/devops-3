from selenium import webdriver

from test.web_test.pages.header_page import HeaderPage
from test.web_test.pages.register_page import RegisterPage
from test.web_test.pages.login_page import loginPage

class Concepts:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        HeaderPage(self.driver).elements.login.click()
        loginPage(self.driver).login(username, password)

    def register(self, gender, FirstName, LastName, password, confirmpass):
        HeaderPage(self.driver).elements.register.click()
        RegisterPage(self.driver).register(gender, FirstName, LastName, password, confirmpass)



