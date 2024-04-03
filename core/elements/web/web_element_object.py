from typing import Tuple, List

import selenium
from selenium.webdriver.remote.webelement import WebElement

from core.elements.web.base_web_element_object import BaseWebElementObject
from core.waiting_manager import WaitingManager


class WebElementObject(BaseWebElementObject):
    def __init__(self, locator: Tuple[str, str], driver: selenium.webdriver, container: WebElement=None):
        super().__init__(locator, driver, container)

    def element(self) -> WebElement:
        return super().initialized_element

    def elements(self) -> List[WebElement]:
        return super().initialized_elements

    def value_of_css_property(self, property: str, value: str):
        element = super().initialized_element
        WaitingManager.wait_css_value_in_css_property(self._driver, element, property, value)
        return element.value_of_css_property(property)

    def scroll_to_element_and_get_coordinates(self) -> tuple[int, int]:
        x, y = super().initialized_element.location_once_scrolled_into_view
        return x, y
