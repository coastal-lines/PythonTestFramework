import sys

import win32gui
import appium
from appium import webdriver
from appium.options.windows import WindowsOptions
from selenium.common import WebDriverException
from urllib3.exceptions import MaxRetryError

from core.driver.desktop.desktop_driver_wrapper import DesktopDriverWrapper
from core.utils.config_manager import ConfigUtils
from core.utils.logging_manager import desktop_logger


desktop_driver = None

def __get_application_handle_hex_by_name(app_name):
    handle = None
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == app_name:
            hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    if hwnds:
        handle = hwnds[0]
    else:
        raise Exception(f"Handle for '{app_name}' application was not found.")

    return hex(handle)

def __get_driver(options: WindowsOptions) -> appium.webdriver:
    global desktop_driver

    try:
        desktop_driver = appium.webdriver.Remote(
            command_executor=f"{ConfigUtils().get_config().desktop.winappdriver_url}"
                             f":"
                             f"{ConfigUtils().get_config().desktop.winappdriver_port}",
            options=options)

        return desktop_driver
    except WebDriverException as ex:
        desktop_logger.exception(f"Desktop '{ConfigUtils().get_config().desktop.default_os}' driver was not started.")
        desktop_logger.exception(f"Try to close all 'winappdriver' sessions before.")
        desktop_logger.exception(ex.msg)
        raise WebDriverException
    except MaxRetryError:
        desktop_logger.exception(f"Desktop '{ConfigUtils().get_config().desktop.default_os}' driver was not started.")
        desktop_logger.exception(f"Please check that Appium Service was started correctly.")
        raise MaxRetryError

def get_windows_driver(**kwargs):
    application_path = kwargs.get("application_path")
    application_name = kwargs.get("application_name")

    options = WindowsOptions()
    options.platform_name = "Windows"

    if application_path:
        options.app = application_path
    if application_name:
        options.app_top_level_window = __get_application_handle_hex_by_name(application_name)

    return __get_driver(options)

def get_windows_driver_for_root() -> appium.webdriver:
    global desktop_driver

    options = WindowsOptions()
    options.app = "Root"
    options.platform_name = "Windows"
    options.automation_name = "Windows"

    driver = __get_driver(options)

    return driver

def get_windows_driver_wrapper(application_window_name: str) -> DesktopDriverWrapper:
    desktop_driver = get_windows_driver_for_root()

    wrapper = DesktopDriverWrapper(desktop_driver)
    wrapper.find_new_window_and_add_as_container(application_window_name)

    return wrapper
