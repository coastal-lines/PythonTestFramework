import appium
from appium import webdriver


class BaseDesktopPage:
    def __init__(self, driver: appium.webdriver):
        self._driver = driver

    @property
    def driver(self) -> appium.webdriver:
        return self._driver