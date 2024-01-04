import json
import requests
from assertpy import soft_assertions, assert_that
from pytest_mock import mocker

from core.utils import files_helper
from resources.api.api_resources_data_class import ApiResourcesData

KARABURMA_BASE_URL = "http://127.0.0.1:8900/api/v1"

def test_image_file_contains_any_button():
    # Create mock-server for requests
    mocker.patch.object(requests, 'post', return_value=MockResponse())

    payload = json.dumps({
        "image_file_path": f"{files_helper.read_resource(ApiResourcesData.karaburma_main_image)}"
    })

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Response will be from mock sever instead of real one
    response = requests.post(url=f"{KARABURMA_BASE_URL}/file", headers=headers, data=payload)

    result = json.loads(response.text)

    with soft_assertions():
        assert_that(result["elements"]).is_not_empty()


class MockResponse:
    def __init__(self):
        self.text = '{"elements": [{"type": "button", "label": "Submit"}]}'  # Заданный вами JSON-документ
        self.status_code = 200  # Код состояния HTTP-ответа
