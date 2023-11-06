"""
Module for fixtures for Web tests.
"""
import os
import pytest
import selenium.webdriver
from pathlib import Path
from selenium.webdriver import firefox
from selenium.webdriver.firefox.service import Service

from core.utils.read_config import ConfigUtils


@pytest.fixture
def web_driver():

    match ConfigUtils.get_config().default_browser:
        case 'Chrome':
            browser_driver = selenium.webdriver.Chrome()
        case 'Firefox':
            browser_driver = selenium.webdriver.Firefox()
        case _:
            raise Exception(f'Browser {ConfigUtils.get_config().default_browser:} not supported.')

    browser_driver.implicitly_wait(10)

    yield browser_driver

    browser_driver.quit()

@pytest.fixture
def desktop_driver():
    pass