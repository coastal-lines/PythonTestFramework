from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy
import time



options = WindowsOptions()
options.app = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
options.platform_name = "Windows"

# Создание драйвера Appium для подключения к WinAppDriver
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723',
    options=options
)

# Ожидание запуска приложения
time.sleep(3)

# Пример взаимодействия с калькулятором
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "num1Button").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "plusButton").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "num2Button").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "equalButton").click()

# Получение результата
result = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CalculatorResults").text
print("Результат: ", result)

# Закрытие приложения и завершение сеанса
#driver.quit()
# Desired capabilities for Windows Calculator

class MyClass():
    def my_method(self):
        pass


    @classmethod
    def my_class_method(self):
        pass