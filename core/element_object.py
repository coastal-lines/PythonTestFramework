import selenium
from selenium.webdriver.support.wait import WebDriverWait
from core.utils.config_manager import ConfigUtils


class Element:

    def __init__(self, locator: tuple):
        self._locator = locator

    def init(self, driver: selenium.webdriver):
        return WebDriverWait(driver, ConfigUtils.get_config().web.wait_timeout).until(EC.presence_of_element_located(self._locator))

    def value_of_css_property(self, driver: selenium.webdriver, property: str, value: str):
        element = self.init(driver)

        WebDriverWait(driver, ConfigUtils.get_config().web.wait_timeout).until(
            lambda drv: value in element.value_of_css_property(property)
        )

        return element.value_of_css_property(property)