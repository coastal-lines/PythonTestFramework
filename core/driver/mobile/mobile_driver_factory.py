import appium
from appium import webdriver

from core.utils.config_manager import ConfigUtils
from core.utils.logging_manager import mobile_logger
from driver.mobile.android import android_driver_manager


def init_mobile_driver(request):
    """
    :request - reserved name for pytest.
    """

    mobile_driver: appium.webdriver = None

    match ConfigUtils().get_config().mobile.default_platform:
        case "Android":
            if request.param.get("default_mode"):
                return android_driver_manager.get_android_emulator_driver(application_name=request.param.get("application_name"))
        case _:
            mobile_logger.exception(f"Mobile '{ConfigUtils().get_config().mobile.default_platform}' driver was not started.")
            raise Exception(f"Mobile driver for {ConfigUtils().get_config().mobile.default_platform} OS not supported. \n Please try to use 'Android' for 'default_platform' parameter.")

