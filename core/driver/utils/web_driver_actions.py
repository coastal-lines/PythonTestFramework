from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def move_to_element(driver: WebDriver, element: WebElement):
    ActionChains(driver).move_to_element(element).perform()

def scroll_to_element(driver: WebDriver, element: WebElement):
    ActionChains(driver).scroll_to_element(element).perform()

def move_to_element_and_click(driver: WebDriver, x: int, y: int):
    actions = ActionBuilder(driver)
    actions.pointer_action.move_to_location(x, y)
    actions.pointer_action.click()
    actions.perform()

def move_to_element_in_container_and_click(driver: WebDriver, container: WebElement, x: int, y: int):
    ActionChains(driver).move_to_element(container).move_by_offset(x, y).click().perform()

    # Reset moving actions
    ActionChains(driver).move_to_element_with_offset(container, 0, 0)

