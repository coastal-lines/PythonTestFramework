import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

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

    QUESTION_ELEMENT = Element((By.CSS_SELECTOR, 'p strong'))
    ANSWERS_ELEMENT = Element((By.CSS_SELECTOR, 'app-tgo-choice tgo-quill-view'))
    ANSWERED_ITEM_ELEMENT = Element((By.XPATH, '//div[@class="tgo-choice tgo-choice--selected"]'))

    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    def load(self):
        super().driver.get(self.PAGE_URL)

    def get_question_text(self) -> str:
        return self.QUESTION_ELEMENT.init_force(super().driver).text

    def get_answer_rgb_colour(self) -> tuple:
        #background_colour = self.ANSWERED_ITEM_ELEMENT.value_of_css_property(super().driver, "background-color", "rgba")

        driver = super().driver
        WebDriverWait(driver, ConfigUtils.get_config().web.wait_timeout).until(
            lambda drv: "rgba" in driver.find_element(By.XPATH, '//div[@class="tgo-choice tgo-choice--selected"]').value_of_css_property("background-color")
        )

        background_colour = super().driver.find_element(By.XPATH, '//div[@class="tgo-choice tgo-choice--selected"]').value_of_css_property("background-color")
        print(background_colour)

        pattern = r'rgba\((\d+),\s*(\d+),\s*(\d+),\s*([0-9.]+)\)'
        color_values = RegExpUtils.match_and_return_group(background_colour, pattern, 3)

        return color_values

    def select_answer(self, answer_index: int):
        answers_list_element = self.ANSWERS_ELEMENT.init(super().driver, True)
        #answer_element = super().driver.find_elements(*self.ANSWERS)[answer_index]
        #answer_element.click()
        answers_list_element[answer_index].click()