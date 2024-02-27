from typing import List

import appium
from appium import webdriver
from appium.webdriver import WebElement

from core.waiting_manager import WaitingManager


class DesktopElementPage:
    #def __init__(self, locator: tuple, driver: appium.webdriver):
    def __init__(self, locator: tuple, driver):
        self.__driver = driver
        self.__locator = locator
        self.__initialized_element: WebElement = None
        self.__initialized_elements: List[WebElement] = None

    def init(self, isList = False) -> WebElement:
        if (self.__initialized_element is None):
            if (isList):
                WaitingManager.wait_element_displayed(self.__driver, self.__locator)
                self.__initialized_element = self.__driver.find_elements(*self.__locator)
            else:
                WaitingManager.wait_element_displayed(self.__driver, self.__locator)
                self.__initialized_element = self.__driver.find_element(*self.__locator)
        else:
            return self.__initialized_element

    def init_force(self) -> WebElement:
        if (self.__initialized_element is None):
            WaitingManager.force_wait_element(self.__driver, self.__locator)
            self.__initialized_element = self.__driver.find_element(*self.__locator)

        return self.__initialized_element

    def init_list(self) -> List[WebElement]:
        if (self.__initialized_element is None):
            WaitingManager.wait_element_displayed(self.__driver, self.__locator)
            self.__initialized_elements = self.__driver.find_elements(*self.__locator)
        else:
            return self.__initialized_elements

    def element(self) -> WebElement:
        if (self.__initialized_element is None):
            self.init_force()
        return self.__initialized_element