import sys
from loguru import logger
import logging

#Logs for web
web_logger = logger.bind(type="web")
web_logger.add("web_tests.log", rotation="50 MB")

#Logs for desktop
desktop_logger = logger.bind(type="desktop")
desktop_logger.add("desktop_tests.log", rotation="50 MB")

#Logs for the standart output
#Setup logger for messages from the console
logging.basicConfig(handlers=[logging.StreamHandler(sys.stdout)], level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)
logger.add("system_output.log", rotation="50 MB")

#Redirect messages from console into logger
@logger.catch
def redirect_logs(record):
    logging.getLogger().handle(record)

#Set handler for redirecting
logger.configure(handlers=[{"sink": redirect_logs, "enqueue": True}])