import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core.driver.utils import javascript_helper
from core.web_element_object import WebElementObject
from pages.base_web_page import BaseWebPage
from resources.web.testgorilla.gorilla_data_constants import GorillaDataConstants


class CoddingTestsFragment(BaseWebPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.__RUN_TEST_BUTTON_ELEMENT = WebElementObject((By.XPATH, "//button//span[contains(text(), 'Run tests')]"), super().driver)
        self.__ADD_TESTCASE_BUTTON_ELEMENT = WebElementObject((By.XPATH, "//button//span[contains(text(), 'Add Test Case')]"), super().driver)
        self.__EXPECTED_OUTPUT_TEXTAREA_ELEMENT = WebElementObject((By.XPATH, "//mat-label[contains(text(), 'Expected output')]/ancestor-or-self::div[contains(@class, 'mat-form-field-infix')]/textarea"), super().driver)
        self.__INPUT_TEXTAREA_ELEMENT = WebElementObject((By.XPATH, "//mat-label[contains(text(), 'Input')]/ancestor-or-self::div[contains(@class, 'mat-form-field-infix')]/textarea"), super().driver)
        self.__PASSED_RESULT_STATUS_LABEL = WebElementObject((By.XPATH, "//div[@class='custom-tests-log-heading']//span[contains(text(), 'Passed')]"), super().driver)
        self.__ERROR_RESULT_STATUS_LABEL = WebElementObject((By.XPATH, "//div[@class='custom-tests-log-heading']//span[contains(text(), 'Error')]"), super().driver)

    def open_codding_exam(self):
        super().navigate_into_page(GorillaDataConstants.codding_exam_page_url)

    def click_add_test_case(self):
        self.__ADD_TESTCASE_BUTTON_ELEMENT.element().click()

    def click_run_tests_button(self):
        self.__RUN_TEST_BUTTON_ELEMENT.element().click()

    def insert_text_into_input(self, text: str):
        self.__INPUT_TEXTAREA_ELEMENT.element().click()
        self.__INPUT_TEXTAREA_ELEMENT.element().send_keys(text)

    def insert_text_into_expected_output(self, text: str):
        self.__EXPECTED_OUTPUT_TEXTAREA_ELEMENT.element().click()
        self.__EXPECTED_OUTPUT_TEXTAREA_ELEMENT.element().send_keys(text)

    def is_test_passed(self) -> bool:
        return self.__PASSED_RESULT_STATUS_LABEL.element().is_displayed()

    def is_test_failed(self) -> bool:
        el = self.__ERROR_RESULT_STATUS_LABEL.element()
        self.__ERROR_RESULT_STATUS_LABEL.scroll_to_element_and_get_coordinates()
        return self.__ERROR_RESULT_STATUS_LABEL.element().is_displayed()