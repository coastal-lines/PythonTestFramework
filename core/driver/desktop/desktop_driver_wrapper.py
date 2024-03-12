from typing import Dict
import appium
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy

from core.driver.desktop.windows import windows_driver_manager
from core.utils.logging_manager import desktop_logger
from core.waiting_manager import WaitingManager


class DesktopDriverWrapper():

    def __init__(self, driver: appium.webdriver):
        self.__driver = driver
        self.__application_container: Dict[str, WebElement] = {}

    @property
    def driver(self):
        return self.__driver

    def __get_application_window_as_element(self, application_window_name: str) -> WebElement:
        locator = (AppiumBy.XPATH, f"//Window[@Name='{application_window_name}']")
        WaitingManager.force_wait_element(self.__driver, locator)

        application_window_as_element = self.__driver.find_element(*locator)

        return application_window_as_element

    def __get_element(self, xpath_locator: str):
        locator = (AppiumBy.XPATH, xpath_locator)
        element = WaitingManager.force_wait_element(self.__driver, locator)

        return element

    def add_application_container(self, application_name: str, application_web_element: WebElement):
        self.__application_container.update({application_name:application_web_element})

    def find_new_window_and_add_as_container(self, application_name: str):
        application_window_as_web_element = self.__get_application_window_as_element(application_name)
        self.add_application_container(application_name, application_window_as_web_element)

    def find_element_and_add_as_container(self, element_name: str, xpath_locator: str):
        element = self.__get_element(xpath_locator)
        self.add_application_container(element_name, element)

    def get_container(self, application_name: str):
        if (application_name not in self.__application_container.keys()):
            desktop_logger.exception(f"Wrapper for desktop driver doesn't have any container for '{application_name}' application.")

        return self.__application_container[application_name]




