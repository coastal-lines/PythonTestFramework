import appium
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy

from core.desktop_element_page import DesktopElementPage
from pages.base_desktop_page import BaseDesktopPage


class SelectImageDialog(BaseDesktopPage):
    def __init__(self, driver: appium.webdriver, container):
        super().__init__(driver)
        self.__container = container

        self.FILE_NAME_COMBOBOX = DesktopElementPage(locator=(AppiumBy.XPATH, "//Window[@Name='Select Image']//ComboBox[@Name='File name:']//Edit[@Name='File name:']"), driver=driver, container=self.__container)
        self.OPEN_BUTTON = DesktopElementPage(locator=(AppiumBy.XPATH, "//Window[@Name='Select Image']//Button[@AutomationId='1']"), driver=driver, container=self.__container)

    def load_file(self, file_path: str):
        self.FILE_NAME_COMBOBOX.test_container().click()
        self.FILE_NAME_COMBOBOX.test_container().send_keys(file_path)
        self.OPEN_BUTTON.test_container().click()
