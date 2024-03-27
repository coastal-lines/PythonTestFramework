from typing import Tuple, List

import selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from core.waiting_manager import WaitingManager


class WebElementObject:

    def __init__(self, locator: Tuple[str, str], driver: selenium.webdriver, container: WebElement=None):
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

    def value_of_css_property(self, property: str, value: str):
        element = self.__init()
        WaitingManager.wait_css_value_in_css_property(self.__driver, element, property, value)

        return element.value_of_css_property(property)