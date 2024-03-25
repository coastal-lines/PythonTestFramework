from pytest_bdd import scenarios, parsers, given, when, then

from pages.web.test_gorilla.gorilla_exam_page import GorillaExamPage
from tests.ui.web_tests.testgorilla.conftest import web_driver


@given(parsers.parse("open browser"), target_fixture='open_browser_step')
def open_browser_step(web_driver) -> GorillaExamPage:
    gorilla_exam_page = GorillaExamPage(web_driver)
    return gorilla_exam_page