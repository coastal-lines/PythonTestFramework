import time
from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.utils.read_config import ConfigUtils
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

        self.force_wait()

        WebDriverWait(self.browser, ConfigUtils.get_config().web.wait_timeout).until(
            EC.element_to_be_clickable(self.browser.find_element(*self.QUESTION)))

        question_element = self.browser.find_element(*self.QUESTION)
        return question_element.text

    def get_answer_rgb_colour(self) -> tuple:

        WebDriverWait(self.browser, ConfigUtils.get_config().web.wait_timeout).until(
            lambda driver: "rgba" in self.browser.find_element(*self.ANSWERED_ITEM).value_of_css_property("background-color")
        )

        background_colour = self.browser.find_element(*self.ANSWERED_ITEM).value_of_css_property("background-color")

        pattern = r'rgba\((\d+),\s*(\d+),\s*(\d+),\s*([0-9.]+)\)'
        color_values = RegExpUtils.match_and_return_group(background_colour, pattern, 3)

        return color_values

    def select_answer(self, answer_index: int):
        answer_element = self.browser.find_elements(*self.ANSWERS)[answer_index]
        answer_element.click()

    def force_wait(self):

        wait_time = 60
        start_time = time.time()

        el = None

        while True:
            current_time = time.time()

            if current_time - start_time >= wait_time:
                break

            try:
                el = WebDriverWait(self.browser, ConfigUtils.get_config().web.wait_timeout).until(EC.element_to_be_clickable(self.browser.find_element(*self.QUESTION)))
                if (el != None):
                    break
            except (Exception) as ex:
                print("Waiting element.")
                time.sleep(3)

        if (el == None):
            raise NoSuchElementException("Element was not found.")