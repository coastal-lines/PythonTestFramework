import pytest

from core.driver import appium_manager
from core.utils.logging_manager import desktop_logger
from core.utils.os import process_manager
from core.driver.desktop import desktop_driver_factory
from core.driver.desktop.desktop_driver_wrapper import DesktopDriverWrapper
from core.utils.config_manager import ConfigUtils

appium_service = None
uri = ConfigUtils().get_config().desktop.appium_url
port = ConfigUtils().get_config().desktop.appium_port

@pytest.fixture(scope="session", autouse=True)
def appium_service_fixture(request):
    global appium_service, uri, port

    if (appium_manager.check_appium_server() == False):
        appium_service = appium_manager.start_appium_service(uri, port)

    yield appium_service

    if (appium_service is not None):
        appium_service.stop()
    process_manager.stop_process("node")

    desktop_logger.info("Appium server stops.")

@pytest.fixture()
def start_desktop_application(request):
    application_process_name = request.node.callspec.params["desktop_driver_wrapper"]["application_process_name"]
    application_path = request.node.callspec.params["desktop_driver_wrapper"]["application_path"]

    if (process_manager.check_process_existed(application_process_name)):
        process_manager.stop_process(application_process_name)

    process_manager.start_process_and_wait(application_path, application_process_name)
    yield
    process_manager.stop_process(application_process_name)

@pytest.fixture()
def desktop_driver_wrapper(start_desktop_application, request) -> DesktopDriverWrapper:
    driver_wrapper = desktop_driver_factory.init_desktop_driver(request)
    desktop_logger.info(f"Current test is: {request.node.name}.")

    yield driver_wrapper

    try:
        driver_wrapper.driver.quit()
    except Exception:
        desktop_logger.info("Driver was not stopped correctly.")