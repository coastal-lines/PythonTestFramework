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


application_window_name = ConfigUtils.get_config().desktop.applications["karaburma_demoapp"].application_window_name
application_path = ConfigUtils.get_config().desktop.applications["karaburma_demoapp"].application_path
application_process_name = ConfigUtils.get_config().desktop.applications["karaburma_demoapp"].application_process_name

def pytest_configure():
    pytest.karaburma_result = None

@allure.step("Karaburma debug image")
def attach_debug_image(request, karaburma_result: RootKaraburmaResponse):
    image_base64 = karaburma_result.debug_screenshot
    scr_path = path_helper.screenshot_path_for_logs(request.node, f"_debug_image")
    files_helper.save_base64_as_png_image(image_base64, scr_path)
    allure.attach(base64.b64decode(image_base64), attachment_type=allure.attachment_type.PNG)

@allure.step("Karaburma full table image")
def attach_full_table_image(request, karaburma_result: RootKaraburmaResponse):
    image_base64 = karaburma_result.table_elements[0].full_table["orig_img_base64"]
    scr_path = path_helper.screenshot_path_for_logs(request.node, f"_debug_full_table_image")
    files_helper.save_base64_as_png_image(image_base64, scr_path)
    allure.attach.file(scr_path, attachment_type=allure.attachment_type.PNG)

@pytest.fixture()
def karaburma(request) -> Karaburma:
    karaburma = Karaburma(ConfigUtils().get_config().karaburma.config_path, "screenshot", "default", False)

    yield karaburma

    if (pytest.karaburma_result is not None):
        attach_debug_image(request, pytest.karaburma_result)

@pytest.fixture()
def desktop_driver_wrapper(start_desktop_application, request) -> DesktopDriverWrapper:
    driver_wrapper = desktop_driver_factory.init_desktop_driver(request)
    desktop_logger.info(f"Current test is: {request.node.name}.")

    yield driver_wrapper

    try:
        driver_wrapper.driver.quit()
    except Exception:
        desktop_logger.info("Driver was not stopped correctly.")

@allure.description("Demo Visual Test - Find application elements by Machine Learning")
@pytest.mark.parametrize("desktop_driver_wrapper",
                         [{
                            "application_window_name": application_window_name,
                            "application_path": application_path,
                            "application_process_name": application_process_name
                         }],
                         indirect=True)
def test_demo_karaburma_validate_ui_elements(desktop_driver_wrapper, karaburma):
    # Step 1
    # Try to find all elements on the screen by computer vision and machine learning
    response = karaburma.find_all_elements_and_read_text()
    karaburma_result = karaburma_utils.convert_karaburma_response_into_object(response)
    pytest.karaburma_result = karaburma_result

    # Step 2
    # Soft validation of found UI objects
    with (soft_assertions()):
        assert_that(karaburma_result.table_elements).is_not_empty()
        assert_that(karaburma_result.basic_elements).is_not_empty()

        assert_that(any(element.text.strip() == "Results" for element in karaburma_result.basic_elements)).is_true()
        assert_that(any(element.text.strip() == "Reset" for element in karaburma_result.basic_elements)).is_true()

        assert_that(len(list(filter(lambda element: element.label == "button", karaburma_result.basic_elements)))).described_as('number buttons').is_greater_than(2)
        assert_that(list(filter(lambda element: element.label == "radiobutton", karaburma_result.basic_elements))).described_as('number radiobutton').is_length(2)

        assert_that(karaburma_result.table_elements[0].cells).described_as('number table cells').is_length(69)

    # Step 3
    # Interaction with the table
    first_column_cells = [cell for cell in karaburma_result.table_elements[0].cells if cell["address"][0] == 0]
    for i in range(1, len(first_column_cells), 1):
        windows_driver_actions.click_by_coordinates(first_column_cells[i]["centre_x"], first_column_cells[i]["centre_y"])

@allure.description("Demo Visual Test - Find table element by Machine Learning")
@pytest.mark.parametrize("desktop_driver_wrapper",
                         [{
                            "application_window_name": application_window_name,
                            "application_path": application_path,
                            "application_process_name": application_process_name
                         }],
                         indirect=True)
def test_karaburma_validate_table_the_latest_cell_element(desktop_driver_wrapper, karaburma):
    # Step 1
    # Attempt to find the first table on the screen by Karaburma
    # Fully expanding this table
    # Reading text from all cells
    response = karaburma.find_table_and_expand(table_index=0, read_text_from_cells=True)
    karaburma_result = karaburma_utils.convert_karaburma_response_into_object(response)
    pytest.karaburma_result = karaburma_result

    # Step 2
    # Check text of the latest table cell
    temp_cell = next(cell for cell in karaburma_result.table_elements[0].full_table["cells"] if cell["address"] == [2, 29])
    assert temp_cell is not None
    assert "hello" in temp_cell["text"]
