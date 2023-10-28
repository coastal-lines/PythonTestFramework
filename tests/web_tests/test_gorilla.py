'''
Tests for 'TestGorilla' service.
'''
from core.conftest import browser
from pages.web.gorilla_exam_page import GorillaExamPage


def test_exam_title(browser):

    EXPECTED_QUESTION_TEXT = 'What type of dependency should you set between these two tasks?'
    EXPECTED_ANSWER_COLOUR = ('70', '169', '151')

    gorilla_exam_page = GorillaExamPage(browser)

    #step 1 - navigate into Exam Gorrila page
    gorilla_exam_page.load()

    #step 2 - check question text
    assert(EXPECTED_QUESTION_TEXT, gorilla_exam_page.get_question_text())

    #step 3 - select the last question
    gorilla_exam_page.select_answer(-1)

    #step 4 - check answered item colour
    assert(gorilla_exam_page.get_answer_rgb_colour() == EXPECTED_ANSWER_COLOUR)