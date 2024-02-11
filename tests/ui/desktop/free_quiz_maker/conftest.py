import pytest

from core.driver import desktop_driver_factory
from core.utils.logging_manager import desktop_logger


@pytest.fixture()
def desktop_driver(request):
    driver = desktop_driver_factory.init_desktop_driver(request)
    desktop_logger.info(f"Current test is: {request.node.name}.")
    yield driver
    driver.quit()