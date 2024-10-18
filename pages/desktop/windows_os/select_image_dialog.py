import appium
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from core.elements.desktop.desktop_element_object import DesktopElementObject
from pages.base_desktop_page import BaseDesktopPage


class SelectImageDialog(BaseDesktopPage):
    def __init__(self, driver: appium.webdriver, container):
        super().__init__(driver)
        self.__container = container

        self.__FILE_NAME_COMBOBOX = DesktopElementObject(locator=(AppiumBy.XPATH, "//Window[@Name='Select Image']//ComboBox[@Name='File name:']//Edit[@Name='File name:']"), driver=driver, container=self.__container)
        self.__OPEN_BUTTON = DesktopElementObject(locator=(AppiumBy.XPATH, "//Window[@Name='Select Image']//Button[@AutomationId='1']"), driver=driver, container=self.__container)

    def load_file(self, file_path: str):
        self.__FILE_NAME_COMBOBOX.element_in_container().click()
        self.__FILE_NAME_COMBOBOX.element_in_container().send_keys(file_path)
        self.__OPEN_BUTTON.element_in_container().click()
