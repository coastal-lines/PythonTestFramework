import requests
from json import dumps
from assertpy.assertpy import assert_that


KARABURMA_BASE_URL = "http://127.0.0.1:8900/api/v1/"

def test_karaburma_server_available():
    response = requests.get(KARABURMA_BASE_URL)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)