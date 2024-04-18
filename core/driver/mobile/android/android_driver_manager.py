import appium.webdriver.webdriver

from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_android_emulator_driver(emulator_device_name: str, default_platform: str, appium_url: str, appium_port: str) -> appium.webdriver.webdriver.WebDriver:
    options = UiAutomator2Options()
    options.device_name = emulator_device_name
    options.platform_name = default_platform
    options.automation_name = "UIAutomator2"

    #return webdriver.Remote(f'{appium_url}:{int(appium_port)}', options=options)
    return webdriver.Remote("127.0.0.1:4723", options=options)