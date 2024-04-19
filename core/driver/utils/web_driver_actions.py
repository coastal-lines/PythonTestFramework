from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def move_to_element(driver: WebDriver, element: WebElement):
    ActionChains(driver).move_to_element(element).perform()

def scroll_to_element(driver: WebDriver, element: WebElement):
    ActionChains(driver).scroll_to_element(element).perform()

def move_to_element_and_click(driver: WebDriver, x: int, y: int):
    ActionBuilder(driver).pointer_action.move_to_location(x, y).perform()