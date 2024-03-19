import inspect
import pytest
from core.hooks import debuging_ui_hooks


"""
global UI conftest
"""

#Debugging and Interaction hooks
def pytest_exception_interact(node, call, report):
        if report.failed:
            if ("desktop" in node.location[0]):
                application_container_name = node.callspec.params["desktop_driver_wrapper"]["application_window_name"]
                debuging_ui_hooks.save_screenshot_if_test_fo_windows_application_falls(node, call, report, application_container_name)
            elif ("web_tests" in node.location[0]):
                debuging_ui_hooks.save_screenshot_if_test_falls(node, call, report)

            if (pytest.comparison_screenshots_result is not None):
                debuging_ui_hooks.save_result_of_comparison_screenshots(pytest.comparison_screenshots_result, node)

