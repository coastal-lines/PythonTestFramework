from selenium import webdriver

from core.models.browserstack.session_log_model import BrowserstackSessionLogModel
from core.utils.logging_manager import web_logger


def get_current_test_session_logs(driver: webdriver) -> BrowserstackSessionLogModel:
    try:
        response = driver.execute_script('browserstack_executor: {"action": "getSessionDetails"}')
        return BrowserstackSessionLogModel(**response)
    except:
        web_logger.exception(f"Impossible to get logs from browserstack server.")