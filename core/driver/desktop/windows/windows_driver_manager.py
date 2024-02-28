import time

import win32gui
import appium
from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import WebDriverException

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

def get_windows_driver(**kwargs):
    global desktop_driver

    application_path = kwargs.get("application_path")
    application_name = kwargs.get("application_name")

    options = WindowsOptions()
    options.platform_name = "Windows"
    #options.new_command_timeout = 15
    #options.wait_for_app_launch = 15

    if application_path:
        options.app = application_path
    if application_name:
        options.app_top_level_window = __get_application_handle_hex_by_name(application_name)

    try:
        desktop_driver = appium.webdriver.Remote(
            command_executor=f"{ConfigUtils().get_config().desktop.winappdriver_url}"
                             f":"
                             f"{ConfigUtils().get_config().desktop.winappdriver_port}",
            options=options)
    except WebDriverException as ex:
        desktop_logger.exception(f"Desktop '{ConfigUtils().get_config().desktop.default_os}' driver was not started.")
        desktop_logger.exception(f"Try to close all 'winappdriver' sessions before.")
        desktop_logger.exception(ex.msg)

    return desktop_driver

def get_windows_driver_for_control(control_xpath_locator: str):# -> WebElement:
    global desktop_driver

    desktop_driver.quit()
    desktop_driver = None

    options = WindowsOptions()
    options.app = "Root"
    options.platform_name = "Windows"
    options.automation_name = "Windows"

    desktop_driver = appium.webdriver.Remote(
        command_executor=f"{ConfigUtils().get_config().desktop.winappdriver_url}"
                         f":"
                         f"{ConfigUtils().get_config().desktop.winappdriver_port}",
        options=options)

    time.sleep(3)

    control = desktop_driver.find_element(by=AppiumBy.XPATH, value=control_xpath_locator)

    return desktop_driver, control


