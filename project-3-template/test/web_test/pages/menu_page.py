from test.web_test.pages.page_base import PageBase
from test.web_test.helpers.element import Element
from munch import munchify


class MenuPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        page_elements = {
    'Books': Element('//ul[@class="top-menu notmobile"]//a[contains(., "Books")]',
    self),


            
        }
        self.elements = munchify(page_elements)






