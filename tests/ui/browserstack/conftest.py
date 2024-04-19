import pytest
import pytest
from selenium.webdriver.chrome import webdriver

from core.driver.web import web_driver_factory
from core.driver.web.web_driver_factory import init_web_driver
from core.utils.config_manager import ConfigUtils
from core.utils.logging_manager import web_logger


def get_vivo_v21_portrait_chrome_options() -> webdriver.Options:
    options = webdriver.Options()
    options.set_capability('deviceName', 'Vivo V21')
    options.set_capability('osVersion', '11.0')
    options.set_capability('browserName', 'chrome')
    options.set_capability('deviceOrientation', 'portrait')
    options.set_capability('bstack:options', {
        "projectName": "BrowserStack Project",
        "buildName": "bstack-webtests",
        "sessionName": "Codding Exam tests",
        "userName": ConfigUtils().get_config().browserstack.username,
        "accessKey": ConfigUtils().get_config().browserstack.access_key
    })

    return options

def get_samsung_s22_portrait_chrome_options() -> webdriver.Options:
    options = webdriver.Options()
    options.set_capability('deviceName', 'Samsung Galaxy S22')
    options.set_capability('osVersion', '12.0')
    options.set_capability('browserName', 'chrome')
    options.set_capability('deviceOrientation', 'portrait')
    options.set_capability('bstack:options', {
        "projectName": "BrowserStack Project",
        "buildName": "bstack-webtests-samsung",
        "sessionName": "Codding Exam tests",
        "userName": ConfigUtils().get_config().browserstack.username,
        "accessKey": ConfigUtils().get_config().browserstack.access_key
    })

    return options

@pytest.fixture
def browserstack_web_driver(request) -> webdriver:
    web_logger.info(f"Current test is: {request.node.name}.")
    remote_browser_driver = web_driver_factory.init_remote_web_driver(
        "BROWSERSTACK",
        ConfigUtils().get_config().browserstack.url,
        get_samsung_s22_portrait_chrome_options()
    )
    yield remote_browser_driver
    remote_browser_driver.quit()

@pytest.fixture
def web_driver(request):
    web_logger.info(f"Current test is: {request.node.name}.")
    browser_driver = init_web_driver(ConfigUtils().get_config().web.default_browser)
    yield browser_driver
    browser_driver.quit()
