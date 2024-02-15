import time
import appium
from appium import webdriver

from core.driver import windows_driver_manager
from core.utils.config_manager import ConfigUtils
from core.utils.logging_manager import desktop_logger


def init_desktop_driver(request) -> appium.webdriver:
    """
    :request - reserved name for pytest.
    """

    desktop_driver = None

    match ConfigUtils().get_config().desktop.default_os:
        case "Windows":
            if request.param.get("application_path"):
                desktop_driver = windows_driver_manager.get_windows_driver(application_path=request.param.get("application_path"))
            if request.param.get("application_name"):
                desktop_driver = windows_driver_manager.get_windows_driver(application_name=request.param.get("application_name"))

            #desktop_driver = windows_driver_manager.get_windows_driver(application_path=request.param)

            #wait few seconds for starting winappdriver
            time.sleep(3)

            return desktop_driver
        case _:
            desktop_logger.exception(f"Desktop '{ConfigUtils().get_config().desktop.default_os}' driver was not started.")
            raise Exception(f"Desktop driver for {ConfigUtils().get_config().desktop.default_os} OS not supported. \n Please try to use 'Windows' for 'default_os' parameter.")