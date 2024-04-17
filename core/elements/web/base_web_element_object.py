from typing import Tuple, List

import selenium
from selenium.webdriver.remote.webelement import WebElement

from core.driver.utils.waiting_manager import WaitingManager


class BaseWebElementObject:
    def __init__(self, locator: Tuple[str, str], driver: selenium.webdriver, container: WebElement=None):
        self._driver = driver
        self._locator = locator
        self._container = container
        self.__initialized_element: WebElement = None
        self.__initialized_elements: List[WebElement] = None

    @property
    def initialized_element(self) -> WebElement:
        if (self.__initialized_element is None):
            WaitingManager.force_wait_element(self._driver, self._locator)
            self._initialized_element = self._driver.find_element(*self._locator)

        return self._initialized_element

    @property
    def initialized_elements(self) -> List[WebElement]:
        if (self.__initialized_elements is None):
            WaitingManager.force_wait_element(self._driver, self._locator)
            WaitingManager.wait_element_displayed(self._driver, self._locator)
            self._initialized_elements = self._driver.find_elements(*self._locator)

        return self._initialized_elements

