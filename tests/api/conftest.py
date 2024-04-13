import json

import pytest
from requests import Response

from wrappers.api.api_requests_wrapper import ApiRequestsWrapper
from wrappers.api.clients.karaburma_client import KaraburmaClient
from core.utils import rest_utils
from core.utils.config_manager import ConfigUtils
from core.utils.files import path_helper
from core.utils.os import process_manager
from resources.api.api_image_resources_data_class import ApiImageResourcesData

KARABURMA_SERVICE_PARAMETERS = [
        '--host', ConfigUtils().get_config().api.karaburma_host,
        '--port', ConfigUtils().get_config().api.karaburma_port,
        '--source_mode', 'file',
        '--detection_mode', 'default',
        '--logging', 'False'
    ]

@pytest.fixture(scope="session", autouse=True)
def start_karaburma_as_api_service():
    process_manager.start_python_application_with_venv(work_dir=ConfigUtils().get_config().api.karaburma_work_dir,
                                                             main_script_path=ConfigUtils().get_config().api.karaburma_main_script_path,
                                                             args=KARABURMA_SERVICE_PARAMETERS)
    rest_utils.wait_until_service_available(host="127.0.0.1", port=8900, end_point="api/v1", timeout=30)
    yield
    try:
        ApiRequestsWrapper(f'{ConfigUtils().get_config().api.karaburma_base_url}').get(f'/shutdown')
    except:
        print("Karaburma was completed as a service.")

@pytest.fixture
def karaburma_client() -> KaraburmaClient:
    client = KaraburmaClient()
    yield client

@pytest.fixture
def karaburma_file_mode_buttons_only_response(karaburma_client) -> Response:
    payload = json.dumps({
        "image_file_path": f"{path_helper.get_resource_path(ApiImageResourcesData.karaburma_main_image)}",
        "type_element": "button",
        "is_read_text": False
    })

    response = karaburma_client.request.post("/file", payload, karaburma_client.headers)
    yield response