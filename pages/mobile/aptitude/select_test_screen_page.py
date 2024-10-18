import appium
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy

from core.elements.mobile.mobile_element_object import MobileElementObject
from pages.base_mobile_page import BaseMobilePage
from pages.mobile.aptitude.dialogs.choose_your_test_option_dialog import ChooseYourTestOption


class SelectTestScreenPage(BaseMobilePage):
    def __init__(self, driver: appium.webdriver, container: WebElement=None):
        super().__init__(driver)
        self.__container = container

        self.__START_BUTTON = MobileElementObject((AppiumBy.ID, "nithra.math.aptitude:id/txtStart"), driver)
        self.__AGE_TEST_CHECKBOX = MobileElementObject((AppiumBy.XPATH, "//android.widget.CheckBox[@text='AGE']"), driver)

    def select_test_and_start(self):
        self.__AGE_TEST_CHECKBOX.element().click()
        self.__START_BUTTON.element().click()
        return ChooseYourTestOption(super().driver)

