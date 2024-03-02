import selenium
from selenium.webdriver.remote.webdriver import WebDriver


class BaseWebPage:

    def __init__(self, driver: selenium.webdriver):
        self.__driver = driver

    @property
    def driver(self):
        return self.__driver