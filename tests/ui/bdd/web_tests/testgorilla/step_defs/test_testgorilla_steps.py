from typing import Tuple
from pytest_bdd import scenarios, parsers, given, when, then

from pages.web.test_gorilla.gorilla_exam_page import GorillaExamPage
from tests.ui.web_tests.testgorilla.conftest import web_driver


# This method ia a glue between feature file and current steps definition file
scenarios("../features/testgorilla.feature")

@given("open browser")
def open_browser_step(web_driver) -> GorillaExamPage:
    gorilla_exam_page = GorillaExamPage(web_driver)
    return gorilla_exam_page

@given("navigate into exam page")
def navigate_into_exam_page(open_browser_step: GorillaExamPage):
    open_browser_step.load()

@given("maximize browser window")
def maximize_browser_window_step(open_browser_step: GorillaExamPage):
    open_browser_step.driver.maximize_window()

@when(parsers.cfparse("select item number {item_number:Number}", extra_types={"Number": int}))
def select_item_number_step(open_browser_step, item_number):
    open_browser_step.select_answer(item_number)

@then(parsers.cfparse("answered item has {answered_item_colour:Tuple} colour}", extra_types={"Tuple": Tuple[str,str,str]}))
def answered_item_has_expected_colour(open_browser_step, answered_item_colour):
    assert (open_browser_step.get_answer_rgb_colour() == answered_item_colour)

@then(parsers.cfparse("question text is {question_text: String}", extra_types={"String": str}))
def step_impl(open_browser_step, question_text):
    assert (open_browser_step.get_question_text() == question_text)
