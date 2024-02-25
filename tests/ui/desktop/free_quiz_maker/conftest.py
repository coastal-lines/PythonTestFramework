import pytest

from core.driver.desktop import desktop_driver_factory
from core.utils.config_manager import ConfigUtils
from core.utils.logging_manager import desktop_logger
from core.utils.os import process_manager


desktop_application_name = "FreeQuizMaker"

@pytest.fixture()
def start_free_quiz_maker():
    global desktop_application_name

    if (process_manager.check_process_existed(desktop_application_name)):
        process_manager.stop_process(desktop_application_name)

    process_manager.start_process_and_wait(ConfigUtils().get_config().desktop.application_exe_path, desktop_application_name)

@pytest.fixture()
def desktop_driver(start_free_quiz_maker, request):
    global desktop_application_name

    driver = desktop_driver_factory.init_desktop_driver(request)
    desktop_logger.info(f"Current test is: {request.node.name}.")
    yield driver
    driver.quit()
    process_manager.stop_process(desktop_application_name)
