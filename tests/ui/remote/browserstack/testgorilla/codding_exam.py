from pages.web.test_gorilla.codding_exam_pages.gorilla_codding_exam_page import GorillaCoddingExamPage


def test_positive_values(driver):
    gorilla_codding_exam_page = GorillaCoddingExamPage(driver)
    gorilla_codding_exam_page.codding_tests_fragment.click_add_test_case()