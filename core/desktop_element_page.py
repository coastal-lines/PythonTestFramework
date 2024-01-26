import appium
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from core.waiting_manager import WaitingManager


class DesktopElementPage:
    def __init__(self, locator: tuple):
        self._locator = locator

    def init(self, driver: appium.webdriver, isList = False):
        if (isList):
            WaitingManager.wait_element_displayed(driver, self._locator)
            return driver.find_elements(*self._locator)
        else:
            WaitingManager.wait_element_displayed(driver, self._locator)
            return driver.find_element(*self._locator)

    def init_force(self, driver: appium.webdriver):
        WaitingManager.force_wait_element(driver, self._locator)
        return driver.find_element(*self._locator)