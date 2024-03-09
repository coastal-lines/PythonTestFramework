from typing import List, Tuple

import appium
from appium import webdriver
from appium.webdriver import WebElement

from core.waiting_manager import WaitingManager


class DesktopElementPage:
    def __init__(self, locator: Tuple[str, str], driver: appium.webdriver, container: WebElement=None):
        self.__driver = driver
        self.__locator = locator
        self.__container = container
        self.__initialized_element: WebElement = None
        self.__initialized_elements: List[WebElement] = None

    def __init(self, isList = False) -> WebElement:
        if (self.__initialized_element is None):
            if (isList):
                WaitingManager.wait_element_displayed(self.__driver, self.__locator)
                self.__initialized_element = self.__driver.find_elements(*self.__locator)
            else:
                WaitingManager.wait_element_displayed(self.__driver, self.__locator)
                self.__initialized_element = self.__driver.find_element(*self.__locator)
        else:
            return self.__initialized_element

    def __init_force(self) -> WebElement:
        if (self.__initialized_element is None):
            WaitingManager.force_wait_element(self.__driver, self.__locator)
            self.__initialized_element = self.__driver.find_element(*self.__locator)

        return self.__initialized_element

    def __init_list(self) -> List[WebElement]:
        if (self.__initialized_elements is None):
            WaitingManager.force_wait_element(self.__driver, self.__locator)
            WaitingManager.wait_element_displayed(self.__driver, self.__locator)
            self.__initialized_elements = self.__driver.find_elements(*self.__locator)
        else:
            return self.__initialized_elements

    def element(self) -> WebElement:
        if (self.__initialized_element is None):
            self.__init_force()
        return self.__initialized_element

    def elements(self) -> List[WebElement]:
        if (self.__initialized_elements is None):
            self.__init_list()
        return self.__initialized_elements

    def element_in_container(self):
        if (self.__initialized_element is None):
            WaitingManager.force_wait_element_in_container(self.__driver, self.__container, self.__locator)
            self.__initialized_element = self.__container.find_element(*self.__locator)

        return self.__initialized_element