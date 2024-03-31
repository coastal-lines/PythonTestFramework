from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def move_to_element(driver: WebDriver, element: WebElement):
    ActionChains(driver).move_to_element(element).perform()

def scroll_to_element(driver: WebDriver, element: WebElement):
    ActionChains(driver).scroll_to_element(element).perform()
