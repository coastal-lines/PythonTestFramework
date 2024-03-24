from pytest_bdd import scenarios, parsers, given, when, then

from core.utils.logging_manager import web_logger


# Hooks methods

# Handle steps errors
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    web_logger.exception(f"Scenario '{scenario.name}' was failed because of failed step '{step}'.")
