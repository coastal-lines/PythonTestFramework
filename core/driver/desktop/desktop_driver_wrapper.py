from dataclasses import dataclass

import appium
from appium import webdriver
from appium.webdriver import WebElement


@dataclass
class DesktopDriverWrapper():
    driver: appium.webdriver
    container: WebElement