import appium
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy

from core.elements.mobile.mobile_element_object import MobileElementObject
from pages.base_mobile_page import BaseMobilePage
from pages.mobile.aptitude.test_screen_page import TestScreenPage


class ChooseYourTestOption(BaseMobilePage):
    def __init__(self, driver: appium.webdriver, container: WebElement=None):
        super().__init__(driver)
        self.__container = container

        self.__NORMAL_BUTTON = MobileElementObject((AppiumBy.ID, "nithra.math.aptitude:id/normal"), driver)

    def select_normal_option(self):
        self.__NORMAL_BUTTON.element().click()
        return TestScreenPage(super().driver)
