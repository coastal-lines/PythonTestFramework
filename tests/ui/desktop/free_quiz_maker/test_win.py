import pytest
from appium.webdriver.common.appiumby import AppiumBy


#@pytest.mark.desktop
@pytest.mark.parametrize("desktop_driver", ["Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"], indirect=True)
def test_desktop(desktop_driver):

    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'num1Button').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'plusButton').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'num2Button').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equalButton').click()

    result = desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'CalculatorResults').text

    assert 'Display is 3' == result

@pytest.mark.parametrize("desktop_driver", ["Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"], indirect=True)
def test_desktop2(desktop_driver):

    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'num1Button').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'plusButton').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'num2Button').click()
    desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equalButton').click()

    result = desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'CalculatorResults').text

    assert 'Display is 3' == result


@pytest.mark.parametrize("desktop_driver", ["C:\\Program Files (x86)\\Media Freeware\\Free Quiz Maker\\run.bat"], indirect=True)
def test_free_quiz(desktop_driver):
    pass
    #text = desktop_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'txtQuestion').text()
