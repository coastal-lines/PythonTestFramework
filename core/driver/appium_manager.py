import time
import requests
from appium.webdriver.appium_service import AppiumService

from core.utils.config_manager import ConfigUtils
from core.utils.logging_manager import desktop_logger
from core.utils.os import process_manager


def check_appium_server(host="127.0.0.1", port="4723") -> bool:
    try:
        response = requests.get(f'http://{host}:{port}/status')
        if response.status_code == 200:
            return True
    except Exception:
        return False

def wait_appium_server_available(host="127.0.0.1", port="4723", timeout=30):
    start_time = time.time()
    while True:
        try:
            response = requests.get(f'http://{host}:{port}/status')
            if response.status_code == 200:
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

def start_appium_service():
    host = ConfigUtils().get_config().desktop.appium_url
    port = ConfigUtils().get_config().desktop.appium_port

    appium_service = AppiumService()
    appium_service.start(args=["--address", host, "-p", port])

    try:
        appium_service = AppiumService()
        appium_service.start(args=["--address", ConfigUtils().get_config().desktop.appium_url,
                                   "-p", ConfigUtils().get_config().desktop.appium_port]
                             )
        wait_appium_server_available(host, port)

        desktop_logger.info(f"Appium server is running. Appium server url is {host, port}.")

        return appium_service

    except Exception as ex:
        print("Appium was not started. \n Please check that Appium installed.")
        print(ex)
