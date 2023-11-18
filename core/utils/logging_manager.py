import inspect
import sys
from loguru import logger


class LoggingManager():

    def __init__(self):
        logger.add("app.log")

    def __prepare_callstack(self):

        current_callstack_list = []

        for frame_info in reversed(inspect.stack()):
            current_callstack_list.append("Method '{}' was called from '{}'".format(frame_info.function, frame_info.filename.split("\\")[-1]))

        return current_callstack_list

    def __prepare_callstack_message(self):

        current_callstack_list = LoggingManager().__prepare_callstack()
        callstack_message = "Callstack: " + "\n".join(current_callstack_list)

        return callstack_message

    @staticmethod
    def log_number_arguments_error(excpected_value, actual_value):

        current_callstack_list = LoggingManager().__prepare_callstack()
        callstack_message = LoggingManager().__prepare_callstack_message()

        error_message = f"Method {current_callstack_list[-1]} expects {excpected_value} arguments but was {actual_value}"
        logger.error(error_message + "\n" + callstack_message)

        return error_message

    @staticmethod
    def log_error(orig_error_message):

        callstack_message = LoggingManager().__prepare_callstack_message()
        logger.error(orig_error_message  + "\n" + callstack_message)

    @staticmethod
    def log_information(message):
        logger.info(message)

    @staticmethod
    def handle_unhandled_exception(exc_type, exc_value, exc_traceback):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        logger.critical("Unhandled exception", exc_info=(exc_type, exc_value, exc_traceback))