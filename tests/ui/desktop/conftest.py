import pytest

from core.driver.desktop import appium_manager
from core.utils.logging_manager import desktop_logger
from core.utils.os import process_manager


#Module variables:
appium_service = None

@pytest.fixture(scope="session", autouse=True)
def check_appium_server():
    global appium_service

    if (appium_manager.check_appium_server() == False):
        appium_service = appium_manager.start_appium_service()

    yield appium_service

@pytest.fixture(scope="session", autouse=True)
def tear_down(request):
    global appium_service

    yield
    if (appium_service is not None):
        appium_service.stop()
    process_manager.stop_process("node")

    desktop_logger.info(f"Appium server stops.")