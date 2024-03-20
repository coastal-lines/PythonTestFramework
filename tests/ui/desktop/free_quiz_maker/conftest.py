import time

import pytest

from core.driver.desktop import desktop_driver_factory, appium_manager
from core.driver.desktop.desktop_driver_wrapper import DesktopDriverWrapper
from core.utils.config_manager import ConfigUtils
from core.utils.logging_manager import desktop_logger
from core.utils.os import process_manager


desktop_application_name = "FreeQuizMaker"

@pytest.fixture()
def start_free_quiz_maker():
    global desktop_application_name

    if (process_manager.check_process_existed(desktop_application_name)):
        process_manager.stop_process(desktop_application_name)

    process_manager.start_process_and_wait(ConfigUtils().get_config().desktop.application_exe_path, desktop_application_name)

@pytest.fixture()
def desktop_driver(start_free_quiz_maker, request):
    global desktop_application_name

    driver = desktop_driver_factory.init_desktop_driver(request)
    desktop_logger.info(f"Current test is: {request.node.name}.")
    yield driver
    try:
        driver.quit()
    except Exception:
        desktop_logger.info("Driver was not stopped correctly.")

    process_manager.stop_process(desktop_application_name)

@pytest.fixture()
def desktop_root_driver(start_free_quiz_maker, request):
    global desktop_application_name

    driver = desktop_driver_factory.init_desktop_driver(request)
    desktop_logger.info(f"Current test is: {request.node.name}.")
    yield driver
    try:
        driver.quit()
    except Exception:
        desktop_logger.info("Driver was not stopped correctly.")

    process_manager.stop_process(desktop_application_name)

@pytest.fixture()
def desktop_driver_wrapper(start_free_quiz_maker, request) -> DesktopDriverWrapper:
    global desktop_application_name

    driver_wrapper = desktop_driver_factory.init_desktop_driver(request)
    desktop_logger.info(f"Current test is: {request.node.name}.")

    yield driver_wrapper

    try:
        driver_wrapper.driver.quit()
    except Exception:
        desktop_logger.info("Driver was not stopped correctly.")

    process_manager.stop_process(desktop_application_name)
