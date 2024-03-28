from pages.web.test_gorilla.codding_exam_pages.gorilla_codding_exam_page import GorillaCoddingExamPage


def test_positive_values(web_driver):
    gorilla_codding_exam_page = GorillaCoddingExamPage(web_driver)
    gorilla_codding_exam_page.codding_tests_fragment.open_codding_exam()
    gorilla_codding_exam_page.codding_tests_fragment.click_add_test_case()
    gorilla_codding_exam_page.codding_tests_fragment.insert_text_into_input("ttttt")
    gorilla_codding_exam_page.codding_tests_fragment.insert_text_into_expected_output("t")
    gorilla_codding_exam_page.codding_tests_fragment.click_run_tests_button()
    gorilla_codding_exam_page.codding_tests_fragment.is_test_passed()
    print("")
