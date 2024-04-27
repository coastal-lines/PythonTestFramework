import pytest
import appium.webdriver.webdriver
from appium.webdriver.appium_service import AppiumService

from core.utils.config_manager import ConfigUtils
from core.driver import appium_manager
from core.utils.logging_manager import mobile_logger
from core.utils.os import process_manager
from core.driver.mobile.android import android_driver_manager
from core.emulator import emulator_manager


appium_service = None
uri = ConfigUtils().get_config().mobile.appium_url
port = ConfigUtils().get_config().mobile.appium_port

@pytest.fixture(scope="session", autouse=True)
def start_emulator():
    emulator_manager.start_emulator(
        "emulator -avd pixel_2_-_api_28 -memory 2048 -gpu host -prop 'persist.demo.screen_off_timeout=30000' -prop 'logd.buffer.size=4M'"
    )

    emulator_manager.waiting_android_emulator_is_ready_for_test(
        ConfigUtils().get_config().mobile.emulator_process_name,
        ConfigUtils().get_config().mobile.emulator_port_number
    )

    yield
    emulator_manager.stop_emulator()
    process_manager.stop_process("adb")

@pytest.fixture(scope="session", autouse=True)
def start_appium_service() -> AppiumService:
    global appium_service, uri, port

    if (appium_manager.check_appium_server() == False):
        appium_service = appium_manager.start_appium_service(uri, port)
        mobile_logger.info("Appium server starts.")

    yield appium_service

    if (appium_service is not None):
        appium_service.stop()

    process_manager.stop_process("node")
    mobile_logger.info("Appium server stops.")

@pytest.fixture
def mobile_driver_wrapper() -> appium.webdriver.webdriver.WebDriver:
    mobile_driver = android_driver_manager.get_android_emulator_driver(
        ConfigUtils().get_config().mobile.emulator_device_name,
        ConfigUtils().get_config().mobile.default_platform,
        ConfigUtils().get_config().mobile.appium_url,
        ConfigUtils().get_config().mobile.appium_port
    )

    yield mobile_driver
    mobile_driver.quit()

