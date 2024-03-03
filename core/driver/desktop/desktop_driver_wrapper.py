from typing import Dict
import appium
from appium import webdriver
from appium.webdriver import WebElement

from core.utils.logging_manager import desktop_logger


class DesktopDriverWrapper():

    def __init__(self, driver: appium.webdriver):
        self.__driver = driver
        self.__application_container: Dict[str, WebElement] = {}

    @property
    def driver(self):
        return self.__driver

    def add_application_container(self, application_name: str, application_web_element: WebElement):
        self.__application_container.update({application_name:application_web_element})

    def get_application_container(self, application_name: str):
        if (application_name not in self.__application_container.keys()):
            desktop_logger.exception(f"Wrapper for desktop driver doesn't have any container for '{application_name}' application.")

        return self.__application_container[application_name]





