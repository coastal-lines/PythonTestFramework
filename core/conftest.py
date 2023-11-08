"""
Module for tests fixtures
"""
import time
import appium
import pytest
import selenium.webdriver
from appium import webdriver
from appium.options.windows import WindowsOptions

from core.utils.read_config import ConfigUtils


@pytest.fixture
def web_driver():

    match ConfigUtils.get_config().web.default_browser:
        case 'Chrome':
            browser_driver = selenium.webdriver.Chrome()
        case 'Firefox':
            browser_driver = selenium.webdriver.Firefox()
        case _:
            raise Exception(f'Browser {ConfigUtils.get_config().web.default_browser:} not supported.')

    yield browser_driver

    browser_driver.quit()

@pytest.fixture
def desktop_driver():

    driver = None

    match ConfigUtils().get_config().desktop.default_os:
        case 'Windows':
            options = WindowsOptions()
            options.app = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
            options.platform_name = "Windows"

            driver = appium.webdriver.Remote(
                #command_executor='http://127.0.0.1:4723',
                command_executor= f'{ConfigUtils().get_config().desktop.winappdriver_url}'
                                  f':'
                                  f'{ConfigUtils().get_config().desktop.winappdriver_port}',
                options=options
            )

            #wait few seconds for starting winappdriver
            time.sleep(3)
        case _:
            raise Exception(f'Desktop {ConfigUtils().get_config().desktop.default_os} driver was not started.')

    yield driver

    driver.quit()
