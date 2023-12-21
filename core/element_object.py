import selenium
from selenium.webdriver.support.wait import WebDriverWait
from core.utils.config_manager import ConfigUtils
from selenium.webdriver.support import expected_conditions as EC

from core.waiting_manager import WaitingManager


class Element:

    def __init__(self, locator: tuple):
        self._locator = locator
        #self._waiting_manager = WaitingManager()

    @property
    def locator(self) -> tuple:
        return self._locator

    def init(self, driver: selenium.webdriver):
        return WaitingManager.wait_element_displayed(driver, self)
        #return WebDriverWait(driver, ConfigUtils.get_config().web.wait_timeout).until(EC.presence_of_element_located(self._locator))

    def value_of_css_property(self, driver: selenium.webdriver, property: str, value: str):
        element = self.init(driver)
        WaitingManager.wait_css_value_in_css_property(driver, element, property, value)

        #WebDriverWait(driver, ConfigUtils.get_config().web.wait_timeout).until(
        #    lambda drv: value in element.value_of_css_property(property)
        #)

        return element.value_of_css_property(property)