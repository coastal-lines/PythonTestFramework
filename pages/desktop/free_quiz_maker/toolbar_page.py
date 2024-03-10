import appium
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from core.desktop_element_page import DesktopElementPage
from pages.base_desktop_page import BaseDesktopPage
from pages.desktop.free_quiz_maker.question_details_page import QuestionDetailsPage


class ToolbarPage(BaseDesktopPage):
    def __init__(self, driver: appium.webdriver):
        super().__init__(driver)

        self.__NEW_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "New Quiz"), driver)
        self.__OPEN_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Open Quiz"), driver)
        self.__SAVE_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Save Quiz"), driver)
        self.__NEW_QUESTION_BUTTON = DesktopElementPage((AppiumBy.NAME, "New Question"), driver)
        self.__REMOVE_QUESTION_BUTTON = DesktopElementPage((AppiumBy.NAME, "Remove Question"), driver)
        self.__PUBLISH_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Publish Quiz"), driver)

    def are_buttons_displayed(self):
        return (self.__NEW_QUIZ_BUTTON.element().is_displayed() and
        self.__OPEN_QUIZ_BUTTON.element().is_displayed() and
        self.__SAVE_QUIZ_BUTTON.element().is_displayed() and
        self.__NEW_QUESTION_BUTTON.element().is_displayed() and
        self.__REMOVE_QUESTION_BUTTON.element().is_displayed() and
        self.__PUBLISH_QUIZ_BUTTON.element().is_displayed())

    def create_new_question(self):
        new_question_button_element = self.__NEW_QUESTION_BUTTON.element()
        new_question_button_element.click()
        return QuestionDetailsPage(super().driver)
