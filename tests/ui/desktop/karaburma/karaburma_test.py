import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that, soft_assertions
import karaburma.api.models.response_model
from karaburma.api.models.response_model import RootKaraburmaResponse
from karaburma.main import Karaburma

from core.driver.desktop import appium_manager, desktop_driver_factory
from core.driver.desktop.desktop_driver_wrapper import DesktopDriverWrapper
from core.driver.utils import web_driver_actions
from core.utils.config_manager import ConfigUtils
from core.utils.logging_manager import desktop_logger
from core.utils.os import process_manager
from core.waiting_manager import WaitingManager
from driver.utils import windows_driver_actions

application_window_name = "KaraburmaDemoApp"
appium_service = None


def get_element_centroid(element: karaburma.api.models.response_model.Element) -> tuple[int, int]:
    x = element.x + (element.w // 2)
    y = element.y + (element.h // 2)
    return x, y

def deserialize_karaburma_response_into_object(response: dict) -> RootKaraburmaResponse:
    return RootKaraburmaResponse(response["w"],
                                 response["h"],
                                 response["elements"],
                                 response["listbox_elements"],
                                 response["table_elements"],
                                 response["debug_screenshot"])

@pytest.fixture()
def start_karaburma_demoapp():
    global application_window_name

    if (process_manager.check_process_existed(application_window_name)):
        process_manager.stop_process(application_window_name)

    process_manager.start_process_and_wait(ConfigUtils().get_config().desktop.karaburma_demoapp_path, application_window_name)

@pytest.fixture()
def desktop_driver_wrapper(start_karaburma_demoapp, request) -> DesktopDriverWrapper:
    global application_window_name

    driver_wrapper = desktop_driver_factory.init_desktop_driver(request)
    desktop_logger.info(f"Current test is: {request.node.name}.")

    yield driver_wrapper

    try:
        driver_wrapper.driver.quit()
    except Exception:
        desktop_logger.info("Driver was not stopped correctly.")

    process_manager.stop_process(application_window_name)

@pytest.fixture()
def karaburma() -> Karaburma:
    return Karaburma(ConfigUtils().get_config().karaburma.config_path, "screenshot", "default", False)

@allure.description("TC11")
@pytest.mark.parametrize("desktop_driver_wrapper", [{"application_window_name": application_window_name}], indirect=True)
def test_validate_ui_elements(desktop_driver_wrapper, karaburma):
    # Step 1
    # Try to find all elements on the screen by computer vision and machine learning
    response = karaburma.find_all_elements_and_read_text()
    karaburma_result = deserialize_karaburma_response_into_object(response)

    # Step 2
    # Soft validation of found UI objects
    with (soft_assertions()):
        assert_that(karaburma_result.table_elements).is_not_empty()
        assert_that(karaburma_result.basic_elements).is_not_empty()

        assert_that(any(element.text == "Results" for element in karaburma_result.basic_elements)).is_true()
        assert_that(any(element.text == "Reset" for element in karaburma_result.basic_elements)).is_true()

        assert_that(list(filter(lambda element: element.label == "button", karaburma_result.basic_elements))).described_as('number buttons').is_length(7)
        assert_that(list(filter(lambda element: element.label == "checkbox", karaburma_result.basic_elements))).described_as('number checkboxes').is_length(2)
        assert_that(list(filter(lambda element: element.label == "radiobutton", karaburma_result.basic_elements))).described_as('number radiobutton').is_length(2)

        assert_that(karaburma_result.table_elements[0].cells).described_as('number table cells').is_length(69)

@allure.description("TC12")
@pytest.mark.parametrize("desktop_driver_wrapper", [{"application_window_name": application_window_name}], indirect=True)
def test_select_checkboxes_by_appium_and_karaburma(desktop_driver_wrapper, karaburma):
    # Step 1
    # Select checkbox by Appium
    #offline_exams_checkbox = WaitingManager().force_wait_appium_element(desktop_driver_wrapper.driver, (AppiumBy.ACCESSIBILITY_ID, "OfflineExamsCheckbox"))
    #offline_exams_checkbox.click()

    # Step 2
    # Select checkbox by Karaburma
    response = karaburma.find_all_elements_and_read_text()
    karaburma_result = deserialize_karaburma_response_into_object(response)
    media_exams_checkbox = next((element for element in karaburma_result.basic_elements if element.label == "checkbox" and element.text == "Media exams"), None)
    x, y = get_element_centroid(media_exams_checkbox)
    windows_driver_actions.click_by_coordinates(x, y)
