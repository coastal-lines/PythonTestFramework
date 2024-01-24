import time
import appium
from appium import webdriver
from appium.options.windows import WindowsOptions

from core.utils.config_manager import ConfigUtils
from core.utils.logging_manager import desktop_logger


def init_desktop_driver(request) -> appium.webdriver:
    """
    :request - reserved name for pytest.
    """

    match ConfigUtils().get_config().desktop.default_os:
        case "Windows":
            options = WindowsOptions()
            options.app = request.param
            options.platform_name = "Windows"

            desktop_driver = appium.webdriver.Remote(
                command_executor= f"{ConfigUtils().get_config().desktop.winappdriver_url}"
                                  f":"
                                  f"{ConfigUtils().get_config().desktop.winappdriver_port}",
                options=options)

            #wait few seconds for starting winappdriver
            time.sleep(3)

            return desktop_driver
        case _:
            desktop_logger.exception(f"Desktop '{ConfigUtils().get_config().desktop.default_os}' driver was not started.")
            raise Exception(f"Desktop driver for {ConfigUtils().get_config().desktop.default_os} OS not supported. \n Please try to use 'Windows' for 'default_os' parameter.")