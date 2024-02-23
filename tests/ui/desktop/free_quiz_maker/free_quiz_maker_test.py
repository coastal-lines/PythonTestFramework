import pytest
from appium.webdriver.common.appiumby import AppiumBy

from pages.desktop.free_quiz_maker.toolbar_page import ToolbarPage


@pytest.mark.parametrize("desktop_driver", [{"application_name": "Free Quiz Maker"}], indirect=True)
def test_tc1_question_details_ui_correct(desktop_driver):
    toolbar_page = ToolbarPage(desktop_driver)

    # Step1
    # Check that toolbar buttons are displayed
    assert (toolbar_page.are_buttons_displayed() == True)

    # Step 2
    # Create new question
    # Check default text for elements


@pytest.mark.parametrize("desktop_driver", [{"application_name": "Free Quiz Maker"}], indirect=True)
def test_tc2_save_as_html(desktop_driver):
    label1 = desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'label1')
    print(label1.get_attribute("Name"))