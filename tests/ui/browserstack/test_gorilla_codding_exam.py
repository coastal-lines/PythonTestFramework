import pytest
from assertpy import assert_that

from pages.web.test_gorilla.codding_exam_pages.gorilla_codding_exam_page import GorillaCoddingExamPage


@pytest.mark.parametrize("input_text, output_text", [("selenium", "e")])
def test_positive_test_values(input_text, output_text, browserstack_web_driver):
    # Step 1
    # Navigate into codding page and maximize window
    gorilla_codding_exam_page = GorillaCoddingExamPage(browserstack_web_driver)
    gorilla_codding_exam_page.codding_tests_fragment.open_codding_exam()
    gorilla_codding_exam_page.driver.maximize_window()

    # Step 2
    # Enable new test case
    gorilla_codding_exam_page.codding_tests_fragment.click_add_test_case()

    # Step 3
    # Input text and expected the most frequent char
    gorilla_codding_exam_page.codding_tests_fragment.insert_text_into_input(input_text)
    gorilla_codding_exam_page.codding_tests_fragment.insert_text_into_expected_output(output_text)

    # Step 4
    # Run test for user values set
    gorilla_codding_exam_page.codding_tests_fragment.click_run_tests_button()

    # Step 5
    # Validate result label
    assert gorilla_codding_exam_page.codding_tests_fragment.is_test_passed() is True

@pytest.mark.parametrize("input_text, output_text", [("selenium", "s")])
def test_negative_test_values(input_text, output_text, web_driver):
    # Step 1
    # Input user values and run tests
    gorilla_codding_exam_page = GorillaCoddingExamPage(web_driver)
    gorilla_codding_exam_page.run_tests_with_user_values(input_text, output_text)

    # Step 2
    # Validate status of tests items
    expected_list_items_status = ["Passed", "Passed", "Passed", "Error"]
    actual_list_items_status = gorilla_codding_exam_page.codding_tests_fragment.get_status_list_of_tests_items()
    assert_that(sorted(actual_list_items_status)).is_equal_to(sorted(expected_list_items_status))

    # Step 3
    # Validate result label
    assert gorilla_codding_exam_page.codding_tests_fragment.is_test_failed() is True