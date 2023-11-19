import inspect
import sys
from loguru import logger
import logging


def __prepare_callstack():
    current_callstack_list = []

    for frame_info in reversed(inspect.stack()):
        current_callstack_list.append(
            "Method '{}' was called from '{}'".format(frame_info.function, frame_info.filename.split("\\")[-1]))

    return current_callstack_list

def __prepare_callstack_message():
    current_callstack_list = __prepare_callstack()
    callstack_message = "Callstack: " + "\n".join(current_callstack_list)

    return callstack_message

def log_error(orig_error_message):
    callstack_message = __prepare_callstack_message()
    logger.error(orig_error_message + "\n" + callstack_message)

def make_filter(name):
    def filter_record(record):
        return record["extra"].get("name") == name
    return filter_record

#Logs for web
web_logger = logger.bind(type="web", name="web")
logger.add("web_tests.log", rotation="50 MB", level="DEBUG", filter=make_filter("web"))

#Logs for desktop
desktop_logger = logger.bind(type="desktop", name="desktop")
logger.add("desktop_tests.log", rotation="50 MB", level="DEBUG", filter=make_filter("desktop"))

'''
#Logs for the standart output
#Setup logger for messages from the console
app_logger = logger.bind(type="app")
app_logger.add("system_output.log", rotation="50 MB")
logging.basicConfig(handlers=[logging.StreamHandler(sys.stdout)], level=logging.INFO)
logging.getLogger().setLevel(logging.ERROR)

#Redirect messages from console into logger
@logger.catch
def redirect_logs(record):
    logging.getLogger().handle(record)

#Set handler for redirecting
#logger.configure(handlers=[{"sink": redirect_logs, "enqueue": True}])
'''

