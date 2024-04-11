import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that, soft_assertions

from core.waiting_manager import WaitingManager
from core.driver.utils import windows_driver_actions
from resources.desktop.desktop_image_resources_data_class import DesktopImageResourcesData
from core.utils.files import files_helper, path_helper
from core.utils.screenshot_utils import screenshot_utils, screenshot_comparison_utils
from core.utils import karaburma_utils
from core.utils.config_manager import ConfigUtils


def pytest_configure():
    pytest.karaburma_result = None

@allure.description("TC11")
@pytest.mark.parametrize("desktop_driver_wrapper",
                         [{
                            "application_window_name": ConfigUtils.get_config().desktop.applications["karaburma_demoapp"].application_window_name,
                            "application_path": ConfigUtils.get_config().desktop.applications["karaburma_demoapp"].application_path,
                            "application_process_name": ConfigUtils.get_config().desktop.applications["karaburma_demoapp"].application_process_name
                         }],
                         indirect=True)
def test_karaburma_validate_ui_elements(desktop_driver_wrapper, karaburma):
    # Step 1
    # Try to find all elements on the screen by computer vision and machine learning
    response = karaburma.find_all_elements_and_read_text()
    karaburma_result = karaburma_utils.deserialize_karaburma_response_into_object(response)
    pytest.karaburma_result = karaburma_result

    # Step 2
    # Soft validation of found UI objects
    with (soft_assertions()):
        assert_that(karaburma_result.table_elements).is_not_empty()
        assert_that(karaburma_result.basic_elements).is_not_empty()

        assert_that(any(element.text.strip() == "Results" for element in karaburma_result.basic_elements)).is_true()
        assert_that(any(element.text.strip() == "Reset" for element in karaburma_result.basic_elements)).is_true()

        assert_that(len(list(filter(lambda element: element.label == "button", karaburma_result.basic_elements)))).described_as('number buttons').is_greater_than(2)
        assert_that(list(filter(lambda element: element.label == "checkbox", karaburma_result.basic_elements))).described_as('number checkboxes').is_length(2)
        assert_that(list(filter(lambda element: element.label == "radiobutton", karaburma_result.basic_elements))).described_as('number radiobutton').is_length(2)

        assert_that(karaburma_result.table_elements[0].cells).described_as('number table cells').is_length(69)

@allure.description("TC12")
@pytest.mark.parametrize("desktop_driver_wrapper",
                         [{
                            "application_window_name": ConfigUtils.get_config().desktop.applications["karaburma_demoapp"].application_window_name,
                            "application_path": ConfigUtils.get_config().desktop.applications["karaburma_demoapp"].application_path,
                            "application_process_name": ConfigUtils.get_config().desktop.applications["karaburma_demoapp"].application_process_name
                          }],
                         indirect=True)
def test_select_checkboxes_by_appium_and_karaburma(desktop_driver_wrapper, karaburma):
    # Step 1
    # Select checkbox by Karaburma
    response = karaburma.find_all_elements_and_read_text()
    karaburma_result = karaburma_utils.deserialize_karaburma_response_into_object(response)
    media_exams_checkbox = next((element for element in karaburma_result.basic_elements if element.label == "checkbox" and element.text == "Media exams"), None)
    x, y = karaburma_utils.get_element_centroid(media_exams_checkbox)
    windows_driver_actions.click_by_coordinates(x, y)

    # Step 2
    # Select checkbox by Appium
    offline_exams_checkbox = WaitingManager().force_wait_appium_element(desktop_driver_wrapper.driver, (AppiumBy.ACCESSIBILITY_ID, "OfflineExamsCheckbox"))
    offline_exams_checkbox.click()

    # Step 3
    # Compare screenshots
    expected_screenshot = files_helper.load_image_as_base64(
        path_helper.get_resource_path(DesktopImageResourcesData.karaburma_demoapp_image_1)
    )

    actual_screenshot = screenshot_utils.get_cropped_screenshot_of_windows_element_as_base64(
        desktop_driver_wrapper.get_container(ConfigUtils.get_config().desktop.applications["karaburma_demoapp"].application_window_name)
    )

    result = screenshot_comparison_utils.get_screenshots_similarity(desktop_driver_wrapper.driver, expected_screenshot, actual_screenshot)
    pytest.comparison_screenshots_result = result["visualization"]
    assert (result["score"] > 0.0)
    assert (len(result["visualization"]) > 0)
