from core.utils.files import path_helper
from core.utils.logging_manager import web_logger


def save_screenshot_if_test_falls(node, call, report):
    """
    There are objects from 'pytest_exception_interact' hook:
        node - represent test that is being run
        call - contains information about raised exception
        report - contains test report for the current test
    """
    try:
        matched_driver_key = [key for key in node.funcargs if key.endswith("_driver")][0]
        browser_driver = node.funcargs[matched_driver_key]

        screenshot_path = path_helper.screenshot_path_for_logs(node)

        browser_driver.save_screenshot(screenshot_path)
        web_logger.exception(f"\n Error: \n {report.longreprtext}")
    except Exception as e:
        web_logger.exception(f"Screenshot was not saved for '{node.name}' test. \n Error: {e}")

