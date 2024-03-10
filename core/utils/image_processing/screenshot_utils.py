from typing import Tuple

import pyautogui
from PIL.Image import Image
from appium.webdriver import WebElement

def __get_element_rect(element: WebElement) -> Tuple[int, int, int, int]:
    element_rectangle = element.rect
    x, y, width, height = element_rectangle['x'], element_rectangle['y'], element_rectangle['width'], element_rectangle['height']
    return x, y, width, height

def __do_screenshot_and_get_cropped_image(x: int, y: int, width: int, height: int) -> Image:
    screenshot = pyautogui.screenshot()
    element_screenshot = screenshot.crop((x, y, x + width, y + height))
    return element_screenshot

def save_cropped_screenshot_of_windows_element(element: WebElement, image_path: str):
    x, y, width, height = __get_element_rect(element)
    element_screenshot = __do_screenshot_and_get_cropped_image(x, y, width, height)
    element_screenshot.save(image_path)

def get_cropped_screenshot_of_windows_element(element: WebElement) -> Image:
    x, y, width, height = __get_element_rect(element)
    element_screenshot = __do_screenshot_and_get_cropped_image(x, y, width, height)
    return element_screenshot

#def get_element_screenshot():
#    im = Image.open(BytesIO(data))
