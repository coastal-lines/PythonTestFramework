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
from core.utils.logging_manager import desktop_logger


@pytest.fixture(scope="session", autouse=True)
def global_teardown():

    print("\nGlobal teardown - this runs after all tests")

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

"""
"request" - reserved name for pytest.
"""

@pytest.fixture
def desktop_driver(request):

    driver = None

    desktop_logger.info(f"Current test is: {request.node.name}.")

    match ConfigUtils().get_config().desktop.default_os:
        case 'Windows':
            options = WindowsOptions()
            options.app = request.param
            options.platform_name = "Windows"

            driver = appium.webdriver.Remote(
                command_executor= f'{ConfigUtils().get_config().desktop.winappdriver_url}'
                                  f':'
                                  f'{ConfigUtils().get_config().desktop.winappdriver_port}',
                options=options
            )

            #wait few seconds for starting winappdriver
            time.sleep(3)
        case _:
            desktop_logger.exception(f'Desktop "{ConfigUtils().get_config().desktop.default_os}" driver was not started.')

    yield driver

    driver.quit()
