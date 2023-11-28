import inspect
import os
from loguru import logger


#Module variables:
log_files_path = os.path.join(os.path.dirname(__file__), "../../resources/logs")
web_logs_path = os.path.join(log_files_path, "web_tests.json")
desktop_logs_path = os.path.join(log_files_path, "desktop_tests.json")

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
logger.add(web_logs_path, rotation="50 MB", level="DEBUG", filter=make_filter("web"))
#logger.add(web_logs_path, rotation="50 MB", level="DEBUG", filter=make_filter("web"), format="{\"time\":\"{time:YYYY-MM-DD HH:mm:ss.SSS}\", \"level\":\"{level}\", \"message\":\"{message}\"}")

#Logs for desktop
desktop_logger = logger.bind(type="desktop", name="desktop")
logger.add(desktop_logs_path, rotation="50 MB", level="DEBUG", filter=make_filter("desktop"))
#logger.add(desktop_logs_path, rotation="50 MB", level="DEBUG", filter=make_filter("desktop"), format="{\"time\":\"{time:YYYY-MM-DD HH:mm:ss.SSS}\", \"level\":\"{level}\", \"message\":\"{message}\"}")

