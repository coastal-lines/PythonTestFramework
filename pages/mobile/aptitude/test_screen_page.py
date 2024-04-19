import appium
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy

from core.elements.mobile.mobile_element_object import MobileElementObject
from pages.base_mobile_page import BaseMobilePage


class TestScreenPage(BaseMobilePage):
    def __init__(self, driver: appium.webdriver, container: WebElement=None):
        super().__init__(driver)
        self.__container = container

        self.__QUESTION_TEXT = MobileElementObject((AppiumBy.XPATH, "//node[@class='android.widget.TextView'][string-length(@text) > 50]"), driver)

    def get_question_text(self) -> str:
        return self.__QUESTION_TEXT.element().text