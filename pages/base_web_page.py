from selenium.webdriver.remote.webdriver import WebDriver

from core.driver.web.web_driver_helper import WebDriverHelper


class BaseWebPage:

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__web_driver_helper = WebDriverHelper(driver)

    @property
    def driver(self) -> WebDriver:
        return self.__driver

    @property
    def web_driver_helper(self) -> WebDriverHelper:
        return self.__web_driver_helper

    def navigate_into_page(self, url: str):
        self.__driver.get(url)