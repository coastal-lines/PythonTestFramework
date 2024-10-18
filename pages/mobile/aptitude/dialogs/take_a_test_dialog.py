import appium
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy

from core.elements.mobile.mobile_element_object import MobileElementObject
from pages.base_mobile_page import BaseMobilePage
from pages.mobile.aptitude.select_test_screen_page import SelectTestScreenPage


class TakeATestDialog(BaseMobilePage):
    def __init__(self, driver: appium.webdriver, container: WebElement=None):
        super().__init__(driver)
        self.__container = container

        self.__TEST_LINEAR_LAYOUT= MobileElementObject((AppiumBy.ID, "nithra.math.aptitude:id/lin_test"), driver)

    def select_test_type(self):
        self.__TEST_LINEAR_LAYOUT.element().click()
        return SelectTestScreenPage(super().driver)