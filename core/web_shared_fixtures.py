"""
Module for fixtures for Web tests.
"""

import pytest
import selenium.webdriver

@pytest.fixture
def chrome_browser():
    chrome_browser_driver = selenium.webdriver.Chrome()

    chrome_browser_driver.implicitly_wait(10)

    yield chrome_browser_driver

    chrome_browser_driver.quit()