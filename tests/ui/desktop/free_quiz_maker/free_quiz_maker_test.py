import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy


@pytest.mark.parametrize("desktop_driver", [{"application_name": "Free Quiz Maker"}], indirect=True)
def test_tc1_question_details_ui_correct(desktop_driver):
    print("")
    time.sleep(2)
    label1 = desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'label1')
    print(label1.get_attribute("Name"))
    pass

def test_tc2_save_as_html():
    pass