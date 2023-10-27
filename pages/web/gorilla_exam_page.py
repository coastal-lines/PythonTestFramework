import re

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from core.utils.regexp_utils import RegExpUtils


class GorillaExamPage():

    PAGE_URL = "https://app.testgorilla.com/preview/7aee275a-8df7-469f-98b2-68ea44c994e4?language=en"

    QUESTION = (By.CSS_SELECTOR, 'p strong')
    ANSWERS = (By.CSS_SELECTOR, 'app-tgo-choice tgo-quill-view')
    ANSWERED_ITEM = (By.XPATH, '//div[@class="tgo-choice tgo-choice--selected"]')

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def load(self):
        self.browser.get(self.PAGE_URL)

    def get_question_text(self) -> str:
        question_element = self.browser.find_element(*self.ANSWERS)
        return question_element.text

    def get_answer_rgb_colour(self) -> tuple:
        colour = self.browser.find_element(*self.ANSWERED_ITEM).value_of_css_property("background-color")

        pattern = r'rgba\((\d+), (\d+), (\d+), \d+\.\d+\)'
        color_values = RegExpUtils.match_and_return_group(colour, pattern, 3)

        return color_values

    def select_answer(self, answer_index: int):
        answer_element = self.browser.find_elements(*self.ANSWERS)[answer_index]
        answer_element.click()