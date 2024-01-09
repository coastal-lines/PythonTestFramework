import json
import pytest
import requests

from core.utils.files import path_helper
from resources.api.api_image_resources_data_class import ApiImageResourcesData


KARABURMA_BASE_URL = "http://127.0.0.1:8900/api/v1"

@pytest.fixture
def karaburma_file_mode_buttons_only_response():
    payload = json.dumps({
        "image_file_path": f"{path_helper.get_resource_path(ApiImageResourcesData.karaburma_main_image)}",
        "type_element": "button",
        "is_read_text": False
    })

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url=f"{KARABURMA_BASE_URL}/file", headers=headers, data=payload)

    yield response