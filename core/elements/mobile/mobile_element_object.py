from typing import List, Tuple

import appium
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy

from core.utils.files import files_helper, path_helper
from core.driver.utils.waiting_manager import (WaitingManager)


class MobileElementObject:
    def __init__(self, locator: Tuple[str, str], driver: appium.webdriver, container: WebElement=None):
        self.__driver = driver
        self.__locator = locator
        self.__container = container
        self.__initialized_element: WebElement = None
        self.__initialized_elements: List[WebElement] = None

    def __init(self, isList = False) -> WebElement:
        if (self.__initialized_element is None):
            if (isList):
                WaitingManager.wait_element_displayed(self.__driver, self.__locator)
                self.__initialized_element = self.__driver.find_elements(*self.__locator)
            else:
                WaitingManager.wait_element_displayed(self.__driver, self.__locator)
                self.__initialized_element = self.__driver.find_element(*self.__locator)
        else:
            return self.__initialized_element

    def __init_force(self) -> WebElement:
        if (self.__initialized_element is None):
            WaitingManager.force_wait_element(self.__driver, self.__locator)
            self.__initialized_element = self.__driver.find_element(*self.__locator)

        return self.__initialized_element

    def __init_list(self) -> List[WebElement]:
        if (self.__initialized_elements is None):
            WaitingManager.force_wait_element(self.__driver, self.__locator)
            WaitingManager.wait_element_displayed(self.__driver, self.__locator)
            self.__initialized_elements = self.__driver.find_elements(*self.__locator)
        else:
            return self.__initialized_elements

    def element(self) -> WebElement:
        if (self.__initialized_element is None):
            self.__init_force()
        return self.__initialized_element

    def element_as_image_pattern(self) -> WebElement:
        self.__driver.update_settings({'imageMatchThreshold': 0.8})  # strong search
        self.__driver.update_settings({'fixImageFindScreenshotDims': False})
        self.__driver.update_settings({'fixImageTemplateSize': False})
        self.__driver.update_settings({'fixImageTemplateScale': False})
        self.__driver.update_settings({'defaultImageTemplateScale': 1.0})
        self.__driver.update_settings({'checkForImageElementStaleness': True})
        self.__driver.update_settings({'autoUpdateImageElementPosition': False})
        self.__driver.update_settings({'imageElementTapStrategy': "w3cActions"})
        self.__driver.update_settings({'getMatchedImageResult': True})

        if (self.__initialized_element is None):
            base64_img = files_helper.load_image_as_base64(
                path_helper.get_resource_path(self.__locator[1])
            )
            self.__locator = (AppiumBy.IMAGE, base64_img)
            self.__init_force()

        return self.__initialized_element

    def elements(self) -> List[WebElement]:
        if (self.__initialized_elements is None):
            self.__init_list()
        return self.__initialized_elements

    def element_in_container(self):
        if (self.__initialized_element is None):
            WaitingManager.force_wait_element_in_container(self.__driver, self.__container, self.__locator)
            self.__initialized_element = self.__container.find_element(*self.__locator)

        return self.__initialized_element

