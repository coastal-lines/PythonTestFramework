from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def run_script(driver: WebDriver, script: str, element: WebElement) -> str:
    return str(driver.execute_script(script, element))

def scroll_to_element(driver: WebDriver, element: WebElement):
    return run_script(driver, "return arguments[0].scrollIntoView(true);", element)