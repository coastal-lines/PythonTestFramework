import appium
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from core.driver.utils import mobile_driver_actions
from core.driver.utils.waiting_manager import WaitingManager


class BaseMobilePage:
    def __init__(self, driver: appium.webdriver):
        self._driver = driver

    @property
    def driver(self) -> appium.webdriver:
        return self._driver

    def open_application(self):
        mobile_driver_actions.swipe_right(self._driver)

        WaitingManager().force_wait_appium_element(
            self._driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Aptitude Test']")
        ).click()