import appium
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy

from core.elements.mobile.mobile_element_object import MobileElementObject
from pages.base_mobile_page import BaseMobilePage
from pages.mobile.aptitude.dialogs.take_a_test_dialog import TakeATestDialog


class MainScreenPage(BaseMobilePage):
    def __init__(self, driver: appium.webdriver, container: WebElement=None):
        super().__init__(driver)
        self.__container = container

        self.__TAKE_A_TEST_BUTTON = MobileElementObject((AppiumBy.ID, "nithra.math.aptitude:id/test_dialog"), driver)

    def open_test_dialog(self) -> TakeATestDialog:
        self.__TAKE_A_TEST_BUTTON.element().click()
        return TakeATestDialog(super().driver)