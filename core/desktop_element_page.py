import appium
from appium import webdriver
from appium.webdriver import WebElement

from core.waiting_manager import WaitingManager


class DesktopElementPage:
    def __init__(self, locator: tuple):
        self.__locator = locator
        self.__initialized_element = None

    def init(self, driver: appium.webdriver, isList = False) -> WebElement:
        if (self.__initialized_element is None):
            if (isList):
                WaitingManager.wait_element_displayed(driver, self.__locator)
                self.__initialized_element = driver.find_elements(*self.__locator)
            else:
                WaitingManager.wait_element_displayed(driver, self.__locator)
                self.__initialized_element = driver.find_element(*self.__locator)
        else:
            return self.__initialized_element

    def init_force(self, driver: appium.webdriver) -> WebElement:
        if (self.__initialized_element is None):
            WaitingManager.force_wait_element(driver, self.__locator)
            self.__initialized_element = driver.find_element(*self.__locator)

        return self.__initialized_element

    #def element(self):
    #    if (self.__initialized_element is None):
    #        self.init()