from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from core.web_element_object import WebElementObject
from pages.base_web_page import BaseWebPage
from pages.web.test_gorilla.codding_exam_pages.codding_tests_fragment import CoddingTestsFragment


class GorillaCoddingExamPage(BaseWebPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__codding_tests_fragment = CoddingTestsFragment(driver)

        self.__GOT_IT_BUTTON = WebElementObject((By.CLASS_NAME, "cc-compliance"), super().driver)
        self.__HELP_CHAT_IFRAME = WebElementObject((By.XPATH, "//iframe[@title='Close message']"), super().driver)
        self.__CLOSE_HELP_CHAT_BUTTON = WebElementObject((By.XPATH, "//button[@aria-label='Close message']"), super().driver)

    @property
    def codding_tests_fragment(self) -> CoddingTestsFragment:
        return self.__codding_tests_fragment

    def close_help_chat(self):
        super().driver.switch_to.frame(self.__HELP_CHAT_IFRAME.element())
        self.__CLOSE_HELP_CHAT_BUTTON.element().click()
        super().driver.switch_to.default_content()

    def apply_cookies(self):
        self.__GOT_IT_BUTTON.element().click()

    def run_tests_with_user_values(self, input_text: str, output_text: str):
        """
            :input_text - user text for checking the most frequent char
            :output_text - expected the most frequent char
        """

        self.__codding_tests_fragment.open_codding_exam()
        super().web_driver_helper.maximize_window()
        self.apply_cookies()
        self.close_help_chat()
        self.__codding_tests_fragment.click_add_test_case()
        self.__codding_tests_fragment.insert_text_into_input(input_text)
        self.__codding_tests_fragment.insert_text_into_expected_output(output_text)
        self.__codding_tests_fragment.click_run_tests_button()
        self.__codding_tests_fragment.click_run_tests_button()
        self.__codding_tests_fragment.click_run_tests_button()
        self.__codding_tests_fragment.click_run_tests_button()
        self.__codding_tests_fragment.click_run_tests_button()