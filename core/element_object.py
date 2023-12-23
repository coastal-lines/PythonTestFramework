import selenium
from selenium.webdriver.support.wait import WebDriverWait

from core.waiting_manager import WaitingManager


class Element:

    def __init__(self, locator: tuple):
        self._locator = locator

    @property
    def locator(self) -> tuple:
        return self._locator

    def init(self, driver: selenium.webdriver, isList = False):
        if (isList):
            WaitingManager.wait_element_displayed(driver, self._locator)
            return driver.find_elements(*self._locator)
        else:
            return WaitingManager.wait_element_displayed(driver, self._locator)

    def init_force(self, driver: selenium.webdriver):
        return WaitingManager.force_wait_element(driver, self._locator)

    def value_of_css_property(self, driver: selenium.webdriver, property: str, value: str):
        element = self.init(driver)
        WaitingManager.wait_css_value_in_css_property(driver, element, property, value)

        return element.value_of_css_property(property)