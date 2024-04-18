import time
import requests
from appium.webdriver.appium_service import AppiumService

from core.wrappers.api.api_requests_wrapper import ApiRequestsWrapper
from core.utils.config_manager import ConfigUtils
from core.utils.logging_manager import desktop_logger
from core.utils.os import process_manager


def check_appium_server(host="127.0.0.1", port="4723") -> bool:
    try:
        response = ApiRequestsWrapper(f'http://{host}:{port}').get(f'/status')
        if response.status_code == 200:
            return True
    except Exception:
        return False

def wait_appium_server_available(host="127.0.0.1", port="4723", timeout=30):
    start_time = time.time()
    while True:
        try:
            is_service_available = check_appium_server(host, port)
            if is_service_available is True:
                print("Appium service is ready")
                break
        except requests.ConnectionError:
            pass

        if time.time() - start_time >= timeout:
            print(f"Appium was not started after {timeout} seconds.")
            break

        time.sleep(1)

def start_appium_service_as_process(host="127.0.0.1", port="4723"):
    process_manager.start_process(f"appium --address {host} --port {port}")
    wait_appium_server_available(host, port)

def start_appium_service(uri: str, port: str):
    try:
        appium_service = AppiumService()
        appium_service.start(args=["--address", uri, "-p", port, "--use-plugins", "images"])
        wait_appium_server_available(uri, port)

        desktop_logger.info(f"Appium server is running. Appium server url is {uri, port}.")

        return appium_service

    except Exception as ex:
        print("Appium was not started. \n Please check that Appium installed.")
        print(ex)

