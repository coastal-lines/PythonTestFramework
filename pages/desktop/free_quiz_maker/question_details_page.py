import appium
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from core.desktop_element_page import DesktopElementPage
from pages.base_desktop_page import BaseDesktopPage


class QuestionDetailsPage(BaseDesktopPage):
    QUESTION_DETAILS_TITLE = DesktopElementPage((AppiumBy.ACCESSIBILITY_ID, "txtQuestion"))

    def __init__(self, driver: appium.webdriver):
        super().__init__(driver)

    def get_question_details_title_text(self) -> str:
        return self.QUESTION_DETAILS_TITLE.init_force(super().driver).text

