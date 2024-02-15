from core.hooks import debuging_ui_hooks


"""
global UI conftest
"""

#Debugging and Interaction hooks
def pytest_exception_interact(node, call, report):
        if report.failed:
            debuging_ui_hooks.save_screenshot_if_test_falls(node, call, report)
