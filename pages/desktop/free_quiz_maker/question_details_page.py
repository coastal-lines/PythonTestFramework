from typing import List

import appium
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy

from core.desktop_element_page import DesktopElementPage
from core.driver.desktop import desktop_driver_wrapper
from pages.base_desktop_page import BaseDesktopPage
from pages.desktop.select_image_dialog import SelectImageDialog


class QuestionDetailsPage(BaseDesktopPage):
    def __init__(self, driver: appium.webdriver, container: WebElement=None):
        super().__init__(driver)

        self.__container = container
        self.__QUESTION_DETAILS_TEXTBOX = DesktopElementPage((AppiumBy.ACCESSIBILITY_ID, "txtQuestion"), driver)
        self.__POSSIBLE_ANSWER_LABEL = DesktopElementPage((AppiumBy.ACCESSIBILITY_ID, "lblPossibleAnswer"), driver)
        self.__QUESTION_TYPE_COMBOBOX = DesktopElementPage((AppiumBy.ACCESSIBILITY_ID, "ddlQuestionType"), driver)
        self.__POSSIBLE_ANSWER_LIST = DesktopElementPage((AppiumBy.XPATH, "//Pane[@AutomationId='pnlAnswers']//Pane[@AutomationId='chkSelect']"), driver)
        self.__IMAGE_PANE = DesktopElementPage((AppiumBy.ACCESSIBILITY_ID, "pnlImage"), driver)

    def get_question_details_title_text(self) -> str:
        return self.__QUESTION_DETAILS_TEXTBOX.element().text

    def get_possible_answer_title_text(self) -> str:
        return self.__POSSIBLE_ANSWER_LABEL.element().get_attribute("Name")

    def expand_question_type_combobox(self):
        question_type_combobox = self.__QUESTION_TYPE_COMBOBOX.element()
        question_type_combobox.click()

    def get_question_type_combobox_items(self, driver_for_combobox) -> List[str]:
        combobox_items = driver_for_combobox.find_elements(by=AppiumBy.TAG_NAME, value="ListItem")
        list_text_items = [item.text for item in combobox_items]
        return list_text_items

    def get_all_possible_answers_list(self) -> List[WebElement]:
        return self.__POSSIBLE_ANSWER_LIST.elements()

    def upload_question_image(self, file_path: str):
        self.__IMAGE_PANE.element().click()

        select_image_dialog = SelectImageDialog(super().driver, self.__container)
        select_image_dialog.load_file(file_path)

        self.__container.screenshot(r"C:\Repos\MyGit\PythonTestFramework\resources\logs\desktop\screenshots\testimage1.png")
        i = self.__container.screenshot_as_png
