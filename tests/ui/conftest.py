import pytest
from core.hooks import debuging_ui_hooks
from core.utils.logging_manager import web_logger

"""
global UI conftest
"""

'''
#Debugging and Interaction hooks
def pytest_exception_interact(node, call, report):
        if report.failed:
            try:
                if(hasattr(node, "location")):
                    if ("desktop" in node.location[0]):
                        application_container_name = node.callspec.params["desktop_driver_wrapper"]["application_window_name"]
                        debuging_ui_hooks.save_screenshot_if_test_fo_windows_application_falls(node, call, report, application_container_name)
                    elif ("web" in node.location[0]):
                        debuging_ui_hooks.save_screenshot_if_test_falls(node, call, report)


                    if hasattr(pytest, 'comparison_screenshots_result'):
                        try:
                            if (pytest.__getattr__("comparison_screenshots_result") is not None):
                                if (pytest.comparison_screenshots_result is not None):
                                    debuging_ui_hooks.save_result_of_comparison_screenshots(
                                        pytest.comparison_screenshots_result, node)
                        except:
                            web_logger.exception("Screenshot was not saved.")
                    else:
                        print("Объект не имеет атрибут 'attribute'.")
            except:
                web_logger.exception("No resources for saving into logs.")
'''


