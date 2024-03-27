from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_web_page import BaseWebPage
from pages.web.test_gorilla.codding_exam_pages.codding_tests_fragment import CoddingTestsFragment


class GorillaCoddingExamPage(BaseWebPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__codding_tests_fragment = CoddingTestsFragment(driver)

    @property
    def codding_tests_fragment(self):
        return self.__codding_tests_fragment