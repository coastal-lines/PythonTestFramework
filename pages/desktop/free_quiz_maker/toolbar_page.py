import time

import appium
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy

from core.elements.desktop.desktop_element_page import DesktopElementPage
from pages.base_desktop_page import BaseDesktopPage
from pages.desktop.free_quiz_maker.question_details_page import QuestionDetailsPage
from resources.desktop.desktop_image_resources_data_class import DesktopImageResourcesData


class ToolbarPage(BaseDesktopPage):
    def __init__(self, driver: appium.webdriver):
        super().__init__(driver)

        self.__NEW_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "New Quiz"), driver)
        self.__OPEN_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Open Quiz"), driver)
        self.__SAVE_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Save Quiz"), driver)
        self.__NEW_QUESTION_BUTTON = DesktopElementPage((AppiumBy.NAME, "New Question"), driver)
        self.__NEW_QUESTION_BUTTON_AS_IMAGE_PATTERN = DesktopElementPage((AppiumBy.IMAGE, DesktopImageResourcesData.free_quiz_add_question_button), driver)
        self.__REMOVE_QUESTION_BUTTON = DesktopElementPage((AppiumBy.NAME, "Remove Question"), driver)
        self.__PUBLISH_QUIZ_BUTTON = DesktopElementPage((AppiumBy.NAME, "Publish Quiz"), driver)

    def are_buttons_displayed(self) -> bool:
        return (self.__NEW_QUIZ_BUTTON.element().is_displayed() and
        self.__OPEN_QUIZ_BUTTON.element().is_displayed() and
        self.__SAVE_QUIZ_BUTTON.element().is_displayed() and
        self.__NEW_QUESTION_BUTTON.element().is_displayed() and
        self.__REMOVE_QUESTION_BUTTON.element().is_displayed() and
        self.__PUBLISH_QUIZ_BUTTON.element().is_displayed())

    def get_new_question_button_as_image_pattern(self) -> WebElement:
        return self.__NEW_QUESTION_BUTTON_AS_IMAGE_PATTERN.element_as_image_pattern()

    def create_new_question(self) -> QuestionDetailsPage:
        new_question_button_element = self.__NEW_QUESTION_BUTTON.element()
        new_question_button_element.click()
        time.sleep(2)

        empty_pane_element = super().driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="toolStrip1")
        empty_pane_element.click()
        time.sleep(2)

        return QuestionDetailsPage(super().driver)
