import pytest

from core.utils.files import path_helper, files_helper
from core.utils.image_processing import screenshot_utils
from pages.desktop.free_quiz_maker.question_details_page import QuestionDetailsPage
from pages.desktop.free_quiz_maker.toolbar_page import ToolbarPage
from resources.api.api_image_resources_data_class import ApiImageResourcesData
from resources.desktop.desktop_image_resources_data_class import DesktopImageResourcesData


@pytest.mark.parametrize("desktop_driver_wrapper", [{"application_window_name": "Free Quiz Maker"}], indirect=True)
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

@pytest.mark.parametrize("desktop_driver_wrapper", [{"application_window_name": "Free Quiz Maker"}], indirect=True)
def test_tc2_image_comparing(desktop_driver_wrapper):
    # Step 1
    # Create new question
    toolbar_page = ToolbarPage(desktop_driver_wrapper.driver)
    toolbar_page.create_new_question()

    # Step 2
    # Upload image
    question_details_page = QuestionDetailsPage(desktop_driver_wrapper.driver, desktop_driver_wrapper.get_container("Free Quiz Maker"))
    image_path = path_helper.get_resource_path(ApiImageResourcesData.karaburma_main_image).replace("/", "\\")
    question_details_page.upload_question_image(image_path)

    # Step 3
    # Compare actual screenshot of the application and expected screenshot
    expected_screenshot = files_helper.load_image_as_base64(path_helper.get_resource_path(DesktopImageResourcesData.free_quiz_image_1))
    actual_screenshot = screenshot_utils.get_element_screenshot_as_base64(desktop_driver_wrapper.get_container("Free Quiz Maker"))

    options = {
        "visualize": True,
        "detectorName": "ORB",
        "matchFunc": "BruteForce",
        "goodMatchesFactor": 40
    }
    result = desktop_driver_wrapper.driver.match_images_features(expected_screenshot, actual_screenshot, **options)

    assert (len(result["visualization"]) > 0)


"""
@pytest.mark.parametrize("desktop_driver", [{"application_name": "Free Quiz Maker"}], indirect=True)
def test_tc_save_as_html(desktop_driver):
    label1 = desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'label1')
    print(label1.get_attribute("Name"))
"""
