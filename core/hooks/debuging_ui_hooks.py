from core.utils.files import path_helper, files_helper
from core.utils.image_processing import screenshot_utils
from core.utils.logging_manager import web_logger, desktop_logger


def save_screenshot_if_test_falls(node, call, report):
    """
    There are objects from 'pytest_exception_interact' hook:
        node - represent test that is being run
        call - contains information about raised exception
        report - contains test report for the current test
    """

    driver_items = [key for key in node.funcargs if key.endswith("_driver")]
    if (len(driver_items) > 0):
        try:
            matched_driver_key = [key for key in node.funcargs if key.endswith("_driver")][0]
            browser_driver = node.funcargs[matched_driver_key]

            screenshot_path = path_helper.screenshot_path_for_logs(node)
            browser_driver.save_screenshot(screenshot_path)

            web_logger.exception(f"\n Error: \n {report.longreprtext}")
        except Exception as e:
            web_logger.exception(f"Screenshot was not saved for '{node.name}' test. \n Error: {e}")

def save_screenshot_if_test_fo_windows_application_falls(node, call, report, application_container_name: str):
    """
    There are objects from 'pytest_exception_interact' hook:
        node - represent test that is being run
        call - contains information about raised exception
        report - contains test report for the current test
    """

    driver_items = [key for key in node.funcargs if key.endswith("desktop_driver_wrapper")]
    if (len(driver_items) > 0):
        try:
            driver_wrapper = node.funcargs["desktop_driver_wrapper"]
            screenshot_path = path_helper.screenshot_path_for_logs(node)

            application_container = driver_wrapper.get_container(application_container_name)
            screenshot_utils.save_cropped_screenshot_of_windows_element(application_container, screenshot_path)

            desktop_logger.exception(f"\n Error: \n {report.longreprtext}")
        except Exception as e:
            desktop_logger.exception(f"Screenshot was not saved for '{node.name}' test. \n Error: {e}")

def save_result_of_comparison_screenshots(comparison_screenshots_result, node):
    try:
        file_path = path_helper.screenshot_path_for_logs(node, "comparison_screenshots_result")
        files_helper.save_bytes_as_png_image(comparison_screenshots_result, file_path)
    except Exception as e:
        desktop_logger.exception(f"Screenshot was not saved for '{node.name}' test. \n Error: {e}")



