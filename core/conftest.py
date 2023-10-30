"""
Module for fixtures for Web tests.
"""
import os
from pathlib import Path

import pytest
import selenium.webdriver
from selenium.webdriver import firefox
from selenium.webdriver.firefox.service import Service

from core.utils.read_config import ConfigUtils


@pytest.fixture
def browser():

    match ConfigUtils.get_config().default_browser:
        case 'Chrome':
            browser_driver = selenium.webdriver.Chrome()
        case 'Firefox':
            '''
            firefox_driver_path = os.path.join(Path(__file__).parent.parent, 'resources\\drivers\\win\\geckodriver.exe')

            firefox_service = firefox.service.Service()
            firefox_service.path = firefox_driver_path

            browser_driver = selenium.webdriver.Firefox(service=firefox_service)
            '''

            browser_driver = selenium.webdriver.Firefox()
        case _:
            raise Exception(f'Browser {ConfigUtils.get_config().default_browser:} not supported.')

    browser_driver.implicitly_wait(10)

    yield browser_driver

    browser_driver.quit()