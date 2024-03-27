from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from core.web_element_object import WebElementObject
from core.utils.regexp_utils import RegExpUtils
from pages.base_web_page import BaseWebPage


class GorillaExamPage(BaseWebPage):
    PAGE_URL = "https://app.testgorilla.com/preview/7aee275a-8df7-469f-98b2-68ea44c994e4?language=en"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.__QUESTION_ELEMENT = WebElementObject((By.CSS_SELECTOR, 'p strong'), driver)
        self.__ANSWERS_ELEMENT = WebElementObject((By.CSS_SELECTOR, 'app-tgo-choice tgo-quill-view'), driver)
        self.__ANSWERED_ITEM_ELEMENT = WebElementObject((By.XPATH, '//div[@class="tgo-choice tgo-choice--selected"]'), driver)

    def load(self):
        super().driver.get(self.PAGE_URL)

    def get_question_text(self) -> str:
        return self.__QUESTION_ELEMENT.element().text

    def get_answer_rgb_colour(self) -> tuple:
        background_colour = self.__ANSWERED_ITEM_ELEMENT.value_of_css_property("background-color", "rgba")
        pattern = r'rgba\((\d+),\s*(\d+),\s*(\d+),\s*([0-9.]+)\)'
        color_values = RegExpUtils.match_and_return_group(background_colour, pattern, 3)

        return color_values

    def select_answer(self, answer_index: int):
        answers_list_element = self.__ANSWERS_ELEMENT.elements()
        answers_list_element[answer_index].click()