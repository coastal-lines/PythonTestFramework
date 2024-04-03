import base64
import io
from io import BytesIO
from typing import Tuple

import allure
import pyautogui
from PIL import Image
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

    allure.attach(element.screenshot_as_base64, name="screenshot", attachment_type=allure.attachment_type.PNG)

    return element_screenshot

def get_cropped_screenshot_of_windows_element_as_base64(element: WebElement) -> str:
    x, y, width, height = __get_element_rect(element)
    element_screenshot = __do_screenshot_and_get_cropped_image(x, y, width, height)

    img_byte_array = io.BytesIO()
    element_screenshot.save(img_byte_array, format='PNG')
    element_screenshot_base64 = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')

    allure.attach(element.screenshot_as_base64, name="screenshot", attachment_type=allure.attachment_type.TEXT)

    return element_screenshot_base64

def get_element_screenshot(element: WebElement) -> Image:
    allure.attach(element.screenshot_as_base64, name="screenshot", attachment_type=allure.attachment_type.PNG)
    return Image.open(BytesIO(element.screenshot_as_png))

def get_element_screenshot_as_bytearray(element: WebElement) -> bytearray:
    return bytearray(element.screenshot_as_png)

def get_element_screenshot_as_base64(element: WebElement) -> str:
    allure.attach(element.screenshot_as_base64, name="screenshot", attachment_type=allure.attachment_type.TEXT)
    return element.screenshot_as_base64

