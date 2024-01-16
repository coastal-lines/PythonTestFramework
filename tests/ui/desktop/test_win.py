from datetime import time
from time import sleep

import appium
import pytest
from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

from core.utils.config_manager import ConfigUtils


def test_m():
    try:
        appium_service = AppiumService()
        appium_service.start(args=["--address", ConfigUtils().get_config().desktop.appium_url,
                                   "-p", ConfigUtils().get_config().desktop.appium_port])
    except Exception as ex:
        print("Appium was not started.")
        print("Please check that Appium installed.")
        print(ex)

    sleep(10)

    # set up appium
    options = WindowsOptions()
    options.app = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    options.platform_name = "Windows"

    driver = appium.webdriver.Remote(
        command_executor=f"{ConfigUtils().get_config().desktop.winappdriver_url}"
                         f":"
                         f"{ConfigUtils().get_config().desktop.winappdriver_port}",
        options=options
    )

    sleep(2)

    driver.find_element(AppiumBy.NAME, "One").click()
    driver.find_element(AppiumBy.NAME, "Plus").click()
    driver.find_element(AppiumBy.NAME, "Two").click()
    driver.find_element(AppiumBy.NAME, "Equals").click()
    sleep(2)
    result = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CalculatorResults").text
    assert result == "Display is 3"

    #appium_service = AppiumService()
    #appium_service.start(args=["--address", ConfigUtils().get_config().desktop.appium_url, "-p", ConfigUtils().get_config().desktop.appium_port])

@pytest.mark.desktop
@pytest.mark.nonparallel
@pytest.mark.parametrize("desktop_driver", ["Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"], indirect=True)
def test_desktop(desktop_driver: appium.webdriver.Remote):

    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'num1Button').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'plusButton').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'num2Button').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equalButton').click()

    result = desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'CalculatorResults').text

    assert 'Display is 3' == result