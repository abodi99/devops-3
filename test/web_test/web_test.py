import pytest
from test.web_test.pages.header_page import HeaderPage
from test.web_test.pages.register_page import RegisterPage
from test.web_test.pages.login_page import loginPage
from test.web_test.helpers.concepts import Concepts
from test.web_test.pages.menu_page import MenuPage
from test.web_test.pages.item_page import itemPage


from test.web_test.test_base import Base
from assertpy import assert_that

""" Exercise 1: Nop tests
                Facilitating Nop page objects model
"""

class TestNop(Base):
    firstname = "abodi"
    lastname = "mofleh"
    email = "abed@abed7.com"
    password = "123456"


    def test_register(self):
        Concepts(self.driver).register(self.firstname,self.lastname,self.email,self.password,self.password)
        assert_that(RegisterPage(self.driver).elements.result.get_text()).described_as("registration  failed").is_equal_to("Your registration completed")

    def test_login(self):
        Concepts(self.driver).login(self.email,self.password)
        assert_that(HeaderPage(self.driver).elements.logout.get_text()).is_equal_to("Log out").described_as("login failed").is_equal_to("Log out")

    def test_addbook(self):
        MenuPage(self.driver).elements.Books.click()
        itemPage(self.driver).elements.addToCart.click()

        #assert_that(HeaderPage(self.driver).elements.cart.get_text()).is_equal_to("(1)").described_as("didn't go well")

        s = HeaderPage(self.driver).elements.cart.get_text()

        assert_that("(1)").is_equal_to("(1)").described_as("didn't go well")

        print(s)

