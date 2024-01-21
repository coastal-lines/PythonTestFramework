"""
Module for tests fixtures
"""
import os
import time
import appium
import pytest
import selenium.webdriver
from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.appium_service import AppiumService

from core.driver.driver_factory import init_web_driver
from core.hooks import debuging_ui_hooks
from core.utils.files import path_helper
from core.utils.os import process_manager
from core.utils.config_manager import ConfigUtils
from core.utils.logging_manager import desktop_logger, web_logger

"""
global UI conftest
"""

#Debugging and Interaction hooks
def pytest_exception_interact(node, call, report):
        if report.failed:
            debuging_ui_hooks.save_screenshot_if_test_falls(node, call, report)