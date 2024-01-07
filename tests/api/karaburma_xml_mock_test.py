import json
import requests
from assertpy import soft_assertions, assert_that

from core.utils.files import path_helper
from resources.api.api_image_resources_data_class import ApiImageResourcesData
from resources.api.api_xml_resources_data_class import ApiXmlResourceData


KARABURMA_BASE_URL = "http://127.0.0.1:8900/api/v1"

def test_image_file_height_is_correct(mocker):
    """
    :mocker - fixture from pytest_mock.
    """

    # Create mock-server for requests
    mocker.patch.object(requests, 'post', return_value=MockResponse())

    payload = json.dumps({
        "image_file_path": f"{path_helper.get_resource_path(ApiImageResourcesData.karaburma_main_image)}"
    })

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Response will be from mock sever instead of real.
    response = requests.post(url=f"{KARABURMA_BASE_URL}/file", headers=headers, data=payload)

    with soft_assertions():
        assert_that(response.text.xpath("//root/h")[0].text).is_equal_to("1079")

class MockResponse:
    def __init__(self):
        self.text = ApiXmlResourceData.karaburma_xml_response
        self.status_code = 200
