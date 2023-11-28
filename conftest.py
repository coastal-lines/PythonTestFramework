"""
Module for tests fixtures
"""

import time
import appium
import pytest
import selenium.webdriver
from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.appium_service import AppiumService

from core.utils import process_manager
from core.utils.read_config import ConfigUtils
from core.utils.logging_manager import desktop_logger, web_logger


#Module variables:
appium_service = None

@pytest.fixture
def web_driver(request):

    web_logger.info(f"Current test is: {request.node.name}.")

    match ConfigUtils.get_config().web.default_browser:
        case "Chrome":
            browser_driver = selenium.webdriver.Chrome()
        case "Firefox":
            browser_driver = selenium.webdriver.Firefox()
        case _:
            raise Exception(f"Browser {ConfigUtils.get_config().web.default_browser:} not supported.")

    yield browser_driver

    browser_driver.quit()

"""
"request" - reserved name for pytest.
"""
@pytest.fixture()
def desktop_driver(request):

    if not process_manager.check_process_existed("node"):
        appium_service = AppiumService()
        appium_service.start(args=["--address", "127.0.0.1", "-p", str(4723)])
        assert appium_service.is_running
        assert appium_service.is_listening

    driver = None

    desktop_logger.info(f"Current test is: {request.node.name}.")

    match ConfigUtils().get_config().desktop.default_os:
        case "Windows":
            options = WindowsOptions()
            options.app = request.param
            options.platform_name = "Windows"

            driver = appium.webdriver.Remote(
                command_executor= f"{ConfigUtils().get_config().desktop.winappdriver_url}"
                                  f":"
                                  f"{ConfigUtils().get_config().desktop.winappdriver_port}",
                options=options
            )

            #wait few seconds for starting winappdriver
            time.sleep(3)
        case _:
            desktop_logger.exception(f"Desktop '{ConfigUtils().get_config().desktop.default_os}' driver was not started.")

    yield driver

    driver.quit()

@pytest.fixture(scope="session", autouse=True)
def tear_down(request):

    global appium_service

    yield
    if (request.node.path.name == "desktop"):
        try:
            appium_service.stop()
        except AttributeError:
            process_manager.stop_process("node")