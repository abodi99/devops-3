from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


""" Exercise 1: Nop tests
                Base class
"""


class Base:

    @classmethod
    def setup_class(cls):
        """ Setup to run once
            Initiatiung some common parameters
        """
        cls.app_url = 'http://host.docker.internal:90/'
        cls.app_wait_timeout = 30

    def setup_method(self):
        """ Setup to run before every test
            Initiate a new driver for every test in order to reset to its initial state.
        """
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--window-size=1920,1080")
       # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver = webdriver.Remote(command_executor = "http://localhost:4444", options=chrome_options)
        self.driver.maximize_window()

        self.driver.get(self.app_url)

    def teardown_method(self):
        """ Teardown to run after every test
            Stop the driver
        """
        self.driver.quit()