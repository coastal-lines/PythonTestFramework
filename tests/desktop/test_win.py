import appium
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from core.conftest import desktop_driver


def test_desktop(desktop_driver: appium.webdriver.Remote):

    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'num1Button').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'plusButton').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'num2Button').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equalButton').click()

    result = desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'CalculatorResults').text

    assert 'Display is 3' == result