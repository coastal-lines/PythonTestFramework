import time
from typing import List

import appium
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.select import Select

from core.desktop_element_page import DesktopElementPage
from core.driver.desktop.windows import windows_driver_manager
from pages.base_desktop_page import BaseDesktopPage


class QuestionDetailsPage(BaseDesktopPage):
    def __init__(self, driver: appium.webdriver):
        super().__init__(driver)

        self.QUESTION_DETAILS_TEXTBOX = DesktopElementPage((AppiumBy.ACCESSIBILITY_ID, "txtQuestion"), driver)
        self.POSSIBLE_ANSWER_LABEL = DesktopElementPage((AppiumBy.ACCESSIBILITY_ID, "lblPossibleAnswer"), driver)
        self.QUESTION_TYPE_COMBOBOX = DesktopElementPage((AppiumBy.ACCESSIBILITY_ID, "ddlQuestionType"), driver)
        self.POSSIBLE_ANSWER_LIST = DesktopElementPage((AppiumBy.XPATH, "//Pane[@AutomationId='pnlAnswers']//Pane[@AutomationId='chkSelect']"), driver)

    def get_question_details_title_text(self) -> str:
        return self.QUESTION_DETAILS_TEXTBOX.element().text

    def get_possible_answer_title_text(self) -> str:
        return self.POSSIBLE_ANSWER_LABEL.element().get_attribute("Name")

    def expand_question_type_combobox(self):
        question_type_combobox = self.QUESTION_TYPE_COMBOBOX.init_force()
        question_type_combobox.click()

    def get_question_type_combobox_items(self, driver_for_combobox) -> List[str]:
        combobox_items = driver_for_combobox.find_elements(by=AppiumBy.TAG_NAME, value="ListItem")
        list_text_items = [item.text for item in combobox_items]
        return list_text_items

    def get_all_possible_answers_list(self) -> List[WebElement]:
        return self.POSSIBLE_ANSWER_LIST.elements()

