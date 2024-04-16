import pytest

from core.utils.logging_manager import web_logger


# Hooks methods

# Handle steps errors
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    web_logger.exception(f"Scenario '{scenario.name}' was failed because of failed step '{step}'.")

# Before each scenario
@pytest.hookimpl
def pytest_bdd_before_scenario(request, feature, scenario):
    web_logger.info(f"Scenario '{scenario.name}' was started.")

# Before each step
@pytest.hookimpl
def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    pass

# After each scenario
@pytest.hookimpl
def pytest_bdd_after_scenario(request, feature, scenario):
    web_logger.info(f"Scenario '{scenario.name}' was completed.")

# After each step
@pytest.hookimpl
def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    pass