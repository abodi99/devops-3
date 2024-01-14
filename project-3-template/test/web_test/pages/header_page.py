from test.web_test.pages.page_base import PageBase
from test.web_test.helpers.element import Element
from munch import munchify


class HeaderPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        page_elements = {
            'register': Element('//a[@class="ico-register"]', self),
            'login': Element('//a[@class="ico-login"]', self),
            'logout': Element('//a[@class="ico-logout"]', self),
            'cart': Element('//span[@class="cart-qty"]', self),
            
          
        }

        self.elements = munchify(page_elements)
