import pytest

from core.driver.web.web_driver_factory import init_web_driver
from core.utils.config_manager import ConfigUtils
from core.utils.logging_manager import web_logger

@pytest.fixture
def web_driver(request):
    web_logger.info(f"Current test is: {request.node.name}.")
    browser_driver = init_web_driver(ConfigUtils().get_config().web.default_browser)
    yield browser_driver
    browser_driver.quit()
