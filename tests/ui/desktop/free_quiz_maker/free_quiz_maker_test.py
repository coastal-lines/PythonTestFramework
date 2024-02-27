import pytest
from appium.webdriver.common.appiumby import AppiumBy

from core.driver.desktop.windows import windows_driver_manager
from pages.desktop.free_quiz_maker.toolbar_page import ToolbarPage


@pytest.mark.parametrize("desktop_driver", [{"application_name": "Free Quiz Maker"}], indirect=True)
def test_tc1_question_details_ui_correct(desktop_driver):
    # Step1
    # Check that toolbar buttons are displayed
    toolbar_page = ToolbarPage(desktop_driver)
    assert (toolbar_page.are_buttons_displayed() == True)

    # Step 2
    # Create new question
    # Check default text for some elements
    question_details_page = toolbar_page.create_new_question()
    assert (question_details_page.get_question_details_title_text() == "New Question")
    assert (question_details_page.get_possible_answer_title_text() == "Possible Answer")

    # Step 3
    # Check items in the expanded combobox
    # We have to have new driver because of switching into 'root'
    # So re-create desktop driver again because desired element outside of the application tree
    #driver_for_combobox = windows_driver_manager.get_windows_driver_for_control("//List[@Name='Question:']")
    expected_text_items = ["Multiple Choice", "Multiple Response", "Subjective"]
    actual_text_items = question_details_page.get_question_type_combobox_items()
    assert (len(expected_text_items) == len(actual_text_items))
    assert (sorted(expected_text_items) == sorted(actual_text_items))

@pytest.mark.parametrize("desktop_driver", [{"application_name": "Free Quiz Maker"}], indirect=True)
def test_tc2_save_as_html(desktop_driver):
    label1 = desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'label1')
    print(label1.get_attribute("Name"))