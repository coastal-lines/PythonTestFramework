import pytest

from core.models.api.kucoin.token_response_model import TokenResponseData
from core.wrappers.api.api_requests_wrapper import ApiRequestsWrapper


@pytest.fixture
def kucoin_service():
    api_request_wrapper = ApiRequestsWrapper("https://api.kucoin.com/")
    api_response = api_request_wrapper.post("api/v1/bullet-public", None, None)
    response_data = TokenResponseData.from_json(api_response.text)