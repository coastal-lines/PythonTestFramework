import time
import pytest

from core.driver import desktop_driver_factory
from core.utils.logging_manager import desktop_logger
from core.utils.os import process_manager


@pytest.fixture()
def start_free_quiz_maker():
    if (process_manager.check_process_existed("FreeQuizMaker")):
        process_manager.stop_process("FreeQuizMaker")

    process_manager.start_process(r"c:\Program Files (x86)\Media Freeware\Free Quiz Maker\run.bat")
    time.sleep(12)

@pytest.fixture()
def desktop_driver(start_free_quiz_maker, request):
    driver = desktop_driver_factory.init_desktop_driver(request)
    desktop_logger.info(f"Current test is: {request.node.name}.")
    yield driver
    driver.quit()
    process_manager.stop_process("FreeQuizMaker")
