from typing import Tuple, List

import selenium
from selenium.webdriver.remote.webelement import WebElement

from core.waiting_manager import WaitingManager


class BaseWebElementObject:
    def __init__(self, locator: Tuple[str, str], driver: selenium.webdriver, container: WebElement=None):
        self._driver = driver
        self._locator = locator
        self._container = container
        self._initialized_element: WebElement = None
        self._initialized_elements: List[WebElement] = None

    def _init(self, isList = False) -> WebElement:
        if (self._initialized_element is None):
            if (isList):
                WaitingManager.wait_element_displayed(self._driver, self._locator)
                self._initialized_element = self._driver.find_elements(*self._locator)
            else:
                WaitingManager.wait_element_displayed(self._driver, self._locator)
                self._initialized_element = self._driver.find_element(*self._locator)
        else:
            return self._initialized_element

    def _init_force(self) -> WebElement:
        if (self._initialized_element is None):
            WaitingManager.force_wait_element(self._driver, self._locator)
            self._initialized_element = self._driver.find_element(*self._locator)

        return self._initialized_element

    def _init_list(self) -> List[WebElement]:
        if (self._initialized_elements is None):
            WaitingManager.force_wait_element(self._driver, self._locator)
            WaitingManager.wait_element_displayed(self._driver, self._locator)
            self._initialized_elements = self._driver.find_elements(*self._locator)
        else:
            return self._initialized_elements

