import base64
import time
import requests

from core.wrappers.api.api_requests_wrapper import ApiRequestsWrapper


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

def encode_basic_auth(username, password) -> str:
    credentials = f"{username}:{password}"
    credentials_bytes = credentials.encode('utf-8')
    base64_credentials = base64.b64encode(credentials_bytes)

    return "Authorization: Basic " + base64_credentials.decode('utf-8')