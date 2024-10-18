import pytest

from core.models.api.kucoin.token_response_model import PublicTokenResponse
from core.wrappers.api.api_requests_wrapper import ApiRequestsWrapper


@pytest.fixture
def kucoin_service(request) -> PublicTokenResponse:
    api_request_wrapper = ApiRequestsWrapper(request.param.get("url"))
    api_response = api_request_wrapper.post(request.param.get("end_point"), None, None)
    response_data = PublicTokenResponse.from_json(api_response.text)
    return response_data