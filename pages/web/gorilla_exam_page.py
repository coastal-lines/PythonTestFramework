import time

import selenium
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.element_object import Element
from core.utils.config_manager import ConfigUtils
from core.utils.regexp_utils import RegExpUtils


class BaseWebPage:

    def __init__(self, driver: selenium.webdriver):
        self._driver = driver

    @property
    def driver(self):
        return self._driver

class GorillaExamPage(BaseWebPage):

    PAGE_URL = "https://app.testgorilla.com/preview/7aee275a-8df7-469f-98b2-68ea44c994e4?language=en"

    QUESTION = (By.CSS_SELECTOR, 'p strong')
    ANSWERS = (By.CSS_SELECTOR, 'app-tgo-choice tgo-quill-view')
    ANSWERED_ITEM = Element((By.XPATH, '//div[@class="tgo-choice tgo-choice--selected"]'))

    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    def load(self):
        super().driver.get(self.PAGE_URL)

    def get_question_text(self) -> str:
        #self.force_wait()

        time.sleep(6)

        WebDriverWait(super().driver, ConfigUtils.get_config().web.wait_timeout).until(
            EC.element_to_be_clickable(super().driver.find_element(*self.QUESTION)))

        question_element = super().driver.find_element(*self.QUESTION)

        return question_element.text

    def get_answer_rgb_colour(self) -> tuple:
        background_colour = self.ANSWERED_ITEM.value_of_css_property(super().driver, "background-color", "rgba")

        pattern = r'rgba\((\d+),\s*(\d+),\s*(\d+),\s*([0-9.]+)\)'
        color_values = RegExpUtils.match_and_return_group(background_colour, pattern, 3)

        return color_values

    def select_answer(self, answer_index: int):
        answer_element = super().driver.find_elements(*self.ANSWERS)[answer_index]
        answer_element.click()

    '''
    def force_wait(self):
        wait_time = 60
        start_time = time.time()

        el = None

        while True:
            current_time = time.time()

            if current_time - start_time >= wait_time:
                break

            try:
                el = WebDriverWait(super().driver, ConfigUtils.get_config().web.wait_timeout).until(EC.element_to_be_clickable(super().driver.find_element(*self.QUESTION)))
                if (el != None):
                    break
            except (Exception) as ex:
                print("Waiting element.")
                time.sleep(3)

        if (el == None):
            raise NoSuchElementException("Element was not found.")
    '''