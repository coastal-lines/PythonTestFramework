from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_web_page import BaseWebPage
from pages.web.test_gorilla.codding_exam_pages.codding_tests_fragment import CoddingTestsFragment


class GorillaCoddingExamPage(BaseWebPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__codding_tests_fragment = CoddingTestsFragment(driver)

    @property
    def codding_tests_fragment(self) -> CoddingTestsFragment:
        return self.__codding_tests_fragment

    def run_tests_with_user_values(self, input_text: str, output_text: str):
        """
            :input_text - user text for checking the most frequent char
            :output_text - expected the most frequent char
        """

        self.__codding_tests_fragment.open_codding_exam()
        super().driver.maximize_window()
        self.__codding_tests_fragment.click_add_test_case()
        self.__codding_tests_fragment.insert_text_into_input(input_text)
        self.__codding_tests_fragment.insert_text_into_expected_output(output_text)
        self.__codding_tests_fragment.click_run_tests_button()