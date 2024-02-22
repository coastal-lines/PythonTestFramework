import appium
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from core.desktop_element_page import DesktopElementPage
from pages.base_desktop_page import BaseDesktopPage


class ToolbarPage(BaseDesktopPage):
    NEW_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "New Quiz"))
    OPEN_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Open Quiz"))
    SAVE_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Save Quiz"))
    NEW_QUESTION_BUTTON = DesktopElementPage((AppiumBy.NAME, "New Question"))
    REMOVE_QUESTION_BUTTON = DesktopElementPage((AppiumBy.NAME, "Remove Question"))
    PUBLISH_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Publish Quiz"))

    def __init__(self, driver: appium.webdriver):
        super().__init__(driver)

    def are_buttons_displayed(self):
        return self.NEW_QUIZ_BUTTON.init_force(super().driver).is_displayed()

