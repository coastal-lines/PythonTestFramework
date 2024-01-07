"""
Module for tests fixtures
"""
import os
import time
import appium
import pytest
import selenium.webdriver
from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.appium_service import AppiumService

from core.utils.os import process_manager
from core.utils.config_manager import ConfigUtils
from core.utils.logging_manager import desktop_logger, web_logger

#Module variables:
appium_service = None
#browser_driver = None

@pytest.fixture
def web_driver(request):

    #global browser_driver

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
        appium_service.start(args=["--address", ConfigUtils().get_config().desktop.appium_url,
                                   "-p", ConfigUtils().get_config().desktop.appium_port])
        assert appium_service.is_running
        assert appium_service.is_listening

    driver = None

    #desktop_logger.info(f"Current test is: {request.node.name}.")

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
    global browser_driver

    yield
    if (request.node.path.name == "desktop"):
        try:
            appium_service.stop()
        except AttributeError:
            process_manager.stop_process("node")

#Debugging and Interaction hooks
def pytest_exception_interact(node, call, report):
    if report.failed:
        try:
            if (node.path.name == "desktop"):
                pass
            elif (node.path.name == "web_tests"):
                browser_driver = node.funcargs['web_driver']

                log_files_path = os.path.join(os.path.dirname(__file__), "resources\\logs\\web\\screenshots")
                screenshot_path = f"{log_files_path}\\{node.name}.png"

                browser_driver.save_screenshot(screenshot_path)
                web_logger.exception(f"\n Error: \n {report.longreprtext}")
        except Exception as e:
            web_logger.exception(f"Screenshot was not saved for '{node.name}' test. \n Error: {e}")