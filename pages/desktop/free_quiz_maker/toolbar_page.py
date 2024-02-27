import appium
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from core.desktop_element_page import DesktopElementPage
from pages.base_desktop_page import BaseDesktopPage
from pages.desktop.free_quiz_maker.question_details_page import QuestionDetailsPage


class ToolbarPage(BaseDesktopPage):

    '''
    NEW_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "New Quiz"))
    OPEN_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Open Quiz"))
    SAVE_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Save Quiz"))
    NEW_QUESTION_BUTTON = DesktopElementPage((AppiumBy.NAME, "New Question"))
    REMOVE_QUESTION_BUTTON = DesktopElementPage((AppiumBy.NAME, "Remove Question"))
    PUBLISH_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Publish Quiz"))
    '''



    def __init__(self, driver: appium.webdriver):
        super().__init__(driver)

        self.NEW_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "New Quiz"), driver)
        self.OPEN_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Open Quiz"), driver)
        self.SAVE_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Save Quiz"), driver)
        self.NEW_QUESTION_BUTTON = DesktopElementPage((AppiumBy.NAME, "New Question"), driver)
        self.REMOVE_QUESTION_BUTTON = DesktopElementPage((AppiumBy.NAME, "Remove Question"), driver)
        self.PUBLISH_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Publish Quiz"), driver)

    def are_buttons_displayed(self):
        return (self.NEW_QUIZ_BUTTON.init_force().is_displayed() and
        self.OPEN_QUIZ_BUTTON.init_force().is_displayed() and
        self.SAVE_QUIZ_BUTTON.init_force().is_displayed() and
        self.NEW_QUESTION_BUTTON.init_force().is_displayed() and
        self.REMOVE_QUESTION_BUTTON.init_force().is_displayed() and
        self.PUBLISH_QUIZ_BUTTON.init_force().is_displayed())

    def create_new_question(self):
        new_question_button_element = self.NEW_QUESTION_BUTTON.element()
        new_question_button_element.click()
        return QuestionDetailsPage(super().driver)