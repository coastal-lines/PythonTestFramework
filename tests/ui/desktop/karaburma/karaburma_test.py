import allure
import pytest
from assertpy import assert_that
from karaburma.api.models.response_model import RootKaraburmaResponse
from karaburma.main import Karaburma

from core.driver.desktop import appium_manager, desktop_driver_factory
from core.driver.desktop.desktop_driver_wrapper import DesktopDriverWrapper
from core.utils.config_manager import ConfigUtils
from core.utils.logging_manager import desktop_logger
from core.utils.os import process_manager

application_window_name = "KaraburmaDemoApp"
appium_service = None

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

def deserialize_karaburma_response_into_object(response: dict) -> RootKaraburmaResponse:
    return RootKaraburmaResponse(response["w"], response["h"], response["elements"], response["listbox_elements"], response["table_elements"], response["debug_screenshot"])

@allure.description("TC11")
@pytest.mark.parametrize("desktop_driver_wrapper", [{"application_window_name": application_window_name}], indirect=True)
def test_kar_1(desktop_driver_wrapper):
    karaburma = Karaburma(r"c:\Repos\MyGit\Karaburma\karaburma\config.json", "screenshot", "default", False)
    response = karaburma.find_all_elements_and_read_text()
    karaburma_result = deserialize_karaburma_response_into_object(response)

    assert_that(karaburma_result.table_elements).is_not_empty()
    assert_that(karaburma_result.basic_elements).is_not_empty()

    assert_that(any(element.text == "TextBox" for element in karaburma_result.basic_elements)).is_true()
    assert_that(any(element.text == "Reset" for element in karaburma_result.basic_elements)).is_true()

    assert(len(list(filter(lambda element: element.label == "button", karaburma_result.basic_elements)))) == 7
    assert(len(list(filter(lambda element: element.label == "checkbox", karaburma_result.basic_elements)))) == 2

    print(karaburma_result)