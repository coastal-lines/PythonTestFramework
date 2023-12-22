import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from core.element_object import Element
from core.utils.regexp_utils import RegExpUtils


class BaseWebPage:

    def __init__(self, driver: selenium.webdriver):
        self._driver = driver

    @property
    def driver(self):
        return self._driver

class GorillaExamPage(BaseWebPage):

    PAGE_URL = "https://app.testgorilla.com/preview/7aee275a-8df7-469f-98b2-68ea44c994e4?language=en"

    QUESTION_ELEMENT = Element((By.CSS_SELECTOR, 'p strong'))
    ANSWERS = (By.CSS_SELECTOR, 'app-tgo-choice tgo-quill-view')
    ANSWERED_ITEM = Element((By.XPATH, '//div[@class="tgo-choice tgo-choice--selected"]'))

    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    def load(self):
        super().driver.get(self.PAGE_URL)

    def get_question_text(self) -> str:
        return self.QUESTION_ELEMENT.init_force(super().driver).text

    def get_answer_rgb_colour(self) -> tuple:
        background_colour = self.ANSWERED_ITEM.value_of_css_property(super().driver, "background-color", "rgba")

        pattern = r'rgba\((\d+),\s*(\d+),\s*(\d+),\s*([0-9.]+)\)'
        color_values = RegExpUtils.match_and_return_group(background_colour, pattern, 3)

        return color_values

    def select_answer(self, answer_index: int):
        answer_element = super().driver.find_elements(*self.ANSWERS)[answer_index]
        answer_element.click()