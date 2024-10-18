import base64

import allure
import pytest
from assertpy import soft_assertions, assert_that
from karaburma.api.models.response_model import RootKaraburmaResponse
from karaburma.main import Karaburma

from core.utils import karaburma_utils
from core.utils.config_manager import ConfigUtils
from core.utils.files import files_helper, path_helper
from core.utils.logging_manager import desktop_logger
from core.driver.desktop import desktop_driver_factory
from core.driver.desktop.desktop_driver_wrapper import DesktopDriverWrapper
from core.driver.utils import windows_driver_actions
from core.utils.files import json_helper

application_window_name = ConfigUtils.get_config().desktop.applications["karaburma_demoapp"].application_window_name
application_path = ConfigUtils.get_config().desktop.applications["karaburma_demoapp"].application_path
application_process_name = ConfigUtils.get_config().desktop.applications["karaburma_demoapp"].application_process_name

DATETIME_TEMPLATE_PATH = r"C:\Repos\MyGit\Karaburma\tests\test_images\datetimepicker.png"

def pytest_configure():
    pytest.karaburma_result = None

@allure.step("JSON response")
def attach_response_json(response: str):
    response = json_helper.convert_object_into_text(response)
    allure.attach(response, name="JSON Response", attachment_type=allure.attachment_type.TEXT)

@allure.step("Debug screenshot")
def attach_debug_image(karaburma_result):
    image_base64 = karaburma_result.debug_screenshot
    scr_path = r"C:\Repos\MyGit\PythonTestFramework\logs\desktop\screenshots\degub_screenshot.png"
    files_helper.save_base64_as_png_image(image_base64, scr_path)
    allure.attach(base64.b64decode(image_base64), attachment_type=allure.attachment_type.PNG)

@allure.step("Full table screenshot")
def attach_full_table_image(karaburma_result: RootKaraburmaResponse):
    image_base64 = karaburma_result.table_elements[0].full_table["orig_img_base64"]
    #image_base64 = karaburma_result.debug_screenshot

    scr_path = r"C:\Repos\MyGit\PythonTestFramework\logs\desktop\screenshots\full_table_screenshot.png"
    files_helper.save_base64_as_png_image(image_base64, scr_path)
    allure.attach(base64.b64decode(image_base64), attachment_type=allure.attachment_type.PNG)

def attach_screenshot(karaburma_result, name: str):
    karaburma_result = karaburma_utils.convert_karaburma_response_into_object(karaburma_result)
    if (name == "debug"):
        attach_debug_image(karaburma_result)
    else:
        attach_full_table_image(karaburma_result)


@pytest.fixture()
def karaburma(request) -> Karaburma:
    karaburma = Karaburma(ConfigUtils().get_config().karaburma.config_path, "screenshot", "default", False)

    yield karaburma

    #if (pytest.karaburma_result is not None):
    #    attach_debug_image(request, pytest.karaburma_result)

@pytest.fixture()
def desktop_driver_wrapper(start_desktop_application, request) -> DesktopDriverWrapper:
    driver_wrapper = desktop_driver_factory.init_desktop_driver(request)
    desktop_logger.info(f"Current test is: {request.node.name}.")

    yield driver_wrapper

    try:
        driver_wrapper.driver.quit()
    except Exception:
        desktop_logger.info("Driver was not stopped correctly.")


@allure.description("Demo Visual Test - Find table element and read the latest cell")
@pytest.mark.parametrize("desktop_driver_wrapper",
                         [{
                            "application_window_name": application_window_name,
                            "application_path": application_path,
                            "application_process_name": application_process_name
                         }],
                         indirect=True)
def test_karaburma_demo(desktop_driver_wrapper, karaburma):
    with allure.step("Step 1: Try to find all elements"):
        response_all_elements = karaburma.find_all_elements_including_patterns([DATETIME_TEMPLATE_PATH], "normal", 0.8, "datetime")
        attach_screenshot(response_all_elements, "debug")

    with allure.step("Step 2: Try to find table, automatically expand it and read the lates cell"):
        response_full_table = karaburma.find_table_and_expand(table_index=0, read_text_from_cells=True)
        attach_response_json(response_full_table)
        attach_screenshot(response_full_table, "full_table")

        karaburma_result = karaburma_utils.convert_karaburma_response_into_object(response_full_table)
        the_latest_cell = next(cell for cell in karaburma_result.table_elements[0].full_table["cells"] if cell["address"] == [2, 29])
        assert "hello" in the_latest_cell["text"]
























