from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy
import time


options = WindowsOptions()
options.app = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
options.platform_name = "Windows"

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723',
    options=options
)

time.sleep(3)

driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'num1Button').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'plusButton').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'num2Button').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equalButton').click()

result = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'CalculatorResults').text