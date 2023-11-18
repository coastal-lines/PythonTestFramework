import appium
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from loguru import logger

from core.conftest import desktop_driver
from core.utils.logging_manager import LoggingManager

@logger.catch
@pytest.mark.nonparallel
@pytest.mark.parametrize("desktop_driver", ["Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"], indirect=True)
def test_desktop(desktop_driver: appium.webdriver.Remote):

    #LoggingManager().log_information("Microsoft.WindowsCalculator_8wekyb3d8bbwe!App")

    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_I, 'num1Button').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'plusButton').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'num2Button').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equalButton').click()

    result = desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'CalculatorResults').text

    assert 'Display is 3' == result