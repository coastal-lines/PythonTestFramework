from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class GorillaExamPage():

    PAGE_URL = "https://app.testgorilla.com/preview/7aee275a-8df7-469f-98b2-68ea44c994e4?language=en"

    QUESTION = (By.CSS_SELECTOR, 'p strong')
    ANSWERS = (By.CSS_SELECTOR, 'app-tgo-choice tgo-quill-view')

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def load(self):
        self.browser.get(self.PAGE_URL)

    def get_question_text(self) -> str:
        question_element = self.browser.find_element()

        return self.QUESTION.text