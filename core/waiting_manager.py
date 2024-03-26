import time
from typing import Tuple

import appium
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from core.utils.config_manager import ConfigUtils


class WaitingManager:

    @classmethod
    def wait_element_displayed(self, driver: WebDriver, locator: Tuple[str, str]):
        return WebDriverWait(driver, ConfigUtils.get_config().web.wait_timeout).until(EC.presence_of_element_located(locator))

    @classmethod
    def wait_css_value_in_css_property(self, driver: WebDriver, element: WebElement, property: str, value: str):
        return WebDriverWait(driver, ConfigUtils.get_config().web.wait_timeout).until(
            lambda drv: value in element.value_of_css_property(property))

    @classmethod
    def force_wait_appium_element(self, driver: appium.webdriver, locator: Tuple[str, str]):
        """
        appium webdriver doesn't support 'EC.element_to_be_clickable', etc.
        """
        wait_time = ConfigUtils.get_config().web.wait_timeout
        start_time = time.time()

        el = None

        while True:
            current_time = time.time()

            if current_time - start_time >= ConfigUtils.get_config().web.wait_timeout:
                break

            try:
                wait = WebDriverWait(driver, wait_time)
                el = wait.until(EC.presence_of_element_located(locator))
                if (el is not None):
                    return el
            except Exception as ex:
                print("Waiting appium element.")
                time.sleep(3)

        if (el == None):
            raise NoSuchElementException("Appium element was not found.")

    @classmethod
    def force_wait_element(self, driver, locator: Tuple[str, str]):
        wait_time = ConfigUtils.get_config().web.wait_timeout
        start_time = time.time()

        el = None

        while True:
            current_time = time.time()

            if current_time - start_time >= ConfigUtils.get_config().web.wait_timeout:
                break

            try:
                wait = WebDriverWait(driver, wait_time)
                el = wait.until(EC.presence_of_element_located(locator))
                if (el is not None):
                    return el
            except Exception as ex:
                print("Waiting element.")
                time.sleep(3)

        if (el == None):
            raise NoSuchElementException("Element was not found.")

    @classmethod
    def force_wait_element_in_container(self, driver: WebDriver, container: WebElement, locator: tuple):
        wait_time = ConfigUtils.get_config().web.wait_timeout
        start_time = time.time()

        el = None

        while True:
            current_time = time.time()

            if current_time - start_time >= ConfigUtils.get_config().web.wait_timeout:
                break

            try:
                wait = WebDriverWait(driver, wait_time)
                el = wait.until(EC.element_to_be_clickable(container.find_element(*locator)))
                if (el != None):
                    return el
            except Exception as ex:
                print("Waiting element.")
                time.sleep(3)

        if (el == None):
            raise NoSuchElementException("Element was not found.")