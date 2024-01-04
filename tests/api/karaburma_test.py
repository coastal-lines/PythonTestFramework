import json
import requests
from assertpy.assertpy import assert_that, soft_assertions

from core.utils import files_helper
from resources.api.api_resources_data_class import ApiResourcesData


KARABURMA_BASE_URL = "http://127.0.0.1:8900/api/v1"

def test_karaburma_server_available():
    x = ApiResourcesData.get_karaburma_xml_response()

    response = requests.get(url=KARABURMA_BASE_URL)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

def test_image_file_contains_any_button():
    payload = json.dumps({
        "image_file_path": f"{files_helper.read_resource(ApiResourcesData.karaburma_main_image)}",
        "type_element": "button",
        "is_read_text": False
    })

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url=f"{KARABURMA_BASE_URL}/file", headers=headers, data=payload)
    result = json.loads(response.text)

    with soft_assertions():
        assert_that(result["elements"]).is_not_empty().extracting("label").contains("button")