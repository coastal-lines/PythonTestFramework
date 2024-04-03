import allure
import pytest

from core.utils.files import path_helper, files_helper
from core.utils.screenshot_utils import screenshot_utils, screenshot_comparison_utils
from pages.desktop.free_quiz_maker.question_details_page import QuestionDetailsPage
from pages.desktop.free_quiz_maker.toolbar_page import ToolbarPage
from resources.api.api_image_resources_data_class import ApiImageResourcesData
from resources.desktop.desktop_image_resources_data_class import DesktopImageResourcesData


application_window_name = "Free Quiz Maker"

def pytest_configure():
    pytest.comparison_screenshots_result = None

@allure.description("TC5")
@pytest.mark.parametrize("desktop_driver_wrapper", [{"application_window_name": application_window_name}], indirect=True)
def test_tc1_question_details_ui_correct(desktop_driver_wrapper):
    combobox_name = "question_type_combobox"

    # Step1
    # Check that toolbar buttons are displayed
    toolbar_page = ToolbarPage(desktop_driver_wrapper.driver)
    assert (toolbar_page.are_buttons_displayed() == True)

    # Step 2
    # Create new question
    # Check default text for some elements
    question_details_page = toolbar_page.create_new_question()
    assert (question_details_page.get_question_details_title_text() == "New Question")
    assert (question_details_page.get_possible_answer_title_text() == "Possible Answer")

    # Step 3
    # Check items in the expanded combobox
    question_details_page.expand_question_type_combobox()
    desktop_driver_wrapper.find_element_and_add_as_container(combobox_name, "//List[@Name='Question:']")

    expected_text_items = ["Multiple Choice", "Multiple Response", "Subjective"]
    actual_text_items = question_details_page.get_question_type_combobox_items(desktop_driver_wrapper.get_container(combobox_name))

    assert (len(expected_text_items) == len(actual_text_items))
    assert (sorted(expected_text_items) == sorted(actual_text_items))

    # Step 4
    # Check number of possible answers
    question_details_page = QuestionDetailsPage(desktop_driver_wrapper.driver)
    assert (len(question_details_page.get_all_possible_answers_list()) == 4)

@allure.description("TC6")
@pytest.mark.parametrize("desktop_driver_wrapper", [{"application_window_name": application_window_name}], indirect=True)
def test_tc2_full_image_comparing_negative_scenario(desktop_driver_wrapper):
    # Step 1
    # Create new question
    toolbar_page = ToolbarPage(desktop_driver_wrapper.driver)
    toolbar_page.create_new_question()

    # Step 2
    # Upload image
    question_details_page = QuestionDetailsPage(desktop_driver_wrapper.driver, desktop_driver_wrapper.get_container(application_window_name))
    image_path = path_helper.get_resource_path(ApiImageResourcesData.karaburma_main_image).replace("/", "\\")
    question_details_page.upload_question_image(image_path)

    # Step 3
    # Compare actual screenshot of the application and expected screenshot
    expected_screenshot = files_helper.load_image_as_base64(path_helper.get_resource_path(DesktopImageResourcesData.free_quiz_image_1))
    actual_screenshot = screenshot_utils.get_element_screenshot_as_base64(desktop_driver_wrapper.get_container(application_window_name))
    result = screenshot_comparison_utils.compare_screenshots(desktop_driver_wrapper.driver, expected_screenshot, actual_screenshot)
    pytest.comparison_screenshots_result = result["visualization"]
    assert (len(result["visualization"]) < 0) is False

@allure.description("TC7")
@pytest.mark.parametrize("desktop_driver_wrapper", [{"application_window_name": application_window_name}], indirect=True)
def test_tc3_application_screenshot_contains_partial_image(desktop_driver_wrapper):
    # Step 1
    # Make a screenshot of the application
    actual_screenshot = screenshot_utils.get_cropped_screenshot_of_windows_element_as_base64(
        desktop_driver_wrapper.get_container(application_window_name)
    )

    # Step 2
    # Load expected partial screenshot
    expected_partial_screenshot = files_helper.load_image_as_base64(
        path_helper.get_resource_path(DesktopImageResourcesData.free_quiz_add_question_button)
    )

    # Step 3
    # Check that 'actual_screenshot' contains 'expected_partial_screenshot'
    result = screenshot_comparison_utils.check_that_screenshot_contains_partial_image(desktop_driver_wrapper.driver, expected_partial_screenshot, actual_screenshot)
    pytest.comparison_screenshots_result = result["visualization"]
    assert (len(result["visualization"]) > 0)

@allure.description("TC8")
@pytest.mark.parametrize("desktop_driver_wrapper", [{"application_window_name": application_window_name}], indirect=True)
def test_tc4_application_screenshot_correct(desktop_driver_wrapper):
    # Step 1
    # Create new question
    toolbar_page = ToolbarPage(desktop_driver_wrapper.driver)
    toolbar_page.create_new_question()

    # Step 2
    # Make a screenshot of the application
    actual_screenshot = screenshot_utils.get_cropped_screenshot_of_windows_element_as_base64(
        desktop_driver_wrapper.get_container(application_window_name)
    )

    # Step 3
    # Load expected screenshot
    expected_screenshot = files_helper.load_image_as_base64(
        path_helper.get_resource_path(DesktopImageResourcesData.free_quiz_image_2)
    )

    # Step 4
    # Compare similarity of actual screenshot and expected
    result = screenshot_comparison_utils.get_screenshots_similarity(desktop_driver_wrapper.driver, expected_screenshot, actual_screenshot)
    pytest.comparison_screenshots_result = result["visualization"]
    assert (result["score"] > 0.0)
    assert (len(result["visualization"]) > 0)

@allure.description("TC9")
@pytest.mark.parametrize("desktop_driver_wrapper", [{"application_window_name": application_window_name}], indirect=True)
def test_tc5_validate_add_question_button_by_image_template(desktop_driver_wrapper):
    # Step 1
    # Try to find button element by image pattern
    toolbar_page = ToolbarPage(desktop_driver_wrapper.driver)
    new_question_button = toolbar_page.get_new_question_button_as_image_pattern()

    # Step 2
    # Validate some button properties
    assert len(new_question_button.get_attribute("visual")) > 0
    assert (new_question_button.is_displayed(), "Element 'new question' button was not found as image pattern.")
    assert 30 < new_question_button.size["width"] < 40
    assert 30 < new_question_button.size["height"] < 40
    assert new_question_button.location["x"] > 0
    assert new_question_button.location["y"] > 0
    assert new_question_button.location_in_view["x"] > 220
    assert new_question_button.location_in_view["y"] > 81
