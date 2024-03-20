import time
import requests

from core.api.api_requests_wrapper import ApiRequestsWrapper


def wait_until_service_available(host="127.0.0.1", port="4723", end_point="status", timeout=30):
    start_time = time.time()
    while True:
        try:
            response = ApiRequestsWrapper(f'http://{host}:{port}').get(f'/{end_point}')
            if response.status_code == 200:
                print("Service is ready")
                break
        except requests.ConnectionError:
            pass

        if time.time() - start_time >= timeout:
            print(f"Service was not started after {timeout} seconds.")
            break

        time.sleep(1)