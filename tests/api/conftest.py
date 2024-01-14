import json
import pytest
from requests import Response

from core.api.clients.karaburma_client import KaraburmaClient
from core.utils.files import path_helper
from resources.api.api_image_resources_data_class import ApiImageResourcesData


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