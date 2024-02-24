import pytest
from appium.webdriver.common.appiumby import AppiumBy

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

    question_details_page.get_question_type_combobox_items()



@pytest.mark.parametrize("desktop_driver", [{"application_name": "Free Quiz Maker"}], indirect=True)
def test_tc2_save_as_html(desktop_driver):
    label1 = desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'label1')
    print(label1.get_attribute("Name"))