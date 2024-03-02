from dataclasses import dataclass
from typing import List

import appium
from appium import webdriver
from appium.webdriver import WebElement


class DesktopDriverWrapper():

    def __init__(self, driver: appium.webdriver):
        self.__driver = driver
        self.__application_container: List[WebElement] = []

    @property
    def driver(self):
        return self.__driver
    
    def application_container(self):
        return self.__application_container


