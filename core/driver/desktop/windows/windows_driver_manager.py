import win32gui
import appium
from appium import webdriver
from appium.options.windows import WindowsOptions

from core.utils.config_manager import ConfigUtils


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
    application_path = kwargs.get("application_path")
    application_name = kwargs.get("application_name")

    options = WindowsOptions()

    if application_path:
        options.app = application_path
    if application_name:
        options.app_top_level_window = __get_application_handle_hex_by_name(application_name)

    options.platform_name = "Windows"

    desktop_driver = appium.webdriver.Remote(
        command_executor=f"{ConfigUtils().get_config().desktop.winappdriver_url}"
                         f":"
                         f"{ConfigUtils().get_config().desktop.winappdriver_port}",
        options=options)

    return desktop_driver