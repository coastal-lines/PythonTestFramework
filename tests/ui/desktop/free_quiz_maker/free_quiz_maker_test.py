import pytest


@pytest.mark.parametrize("desktop_driver", [{"application_name": "FreeQuizMaker"}], indirect=True)
def test_tc1_question_details_ui_correct(desktop_driver):
    print("")
    # text = desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'txtQuestion').text()
    pass

def test_tc2_save_as_html():
    pass