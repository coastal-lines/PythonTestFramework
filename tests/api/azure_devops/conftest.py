import pytest

from core.wrappers.api.api_requests_wrapper import ApiRequestsWrapper


@pytest.fixture
def api_client(request) -> ApiRequestsWrapper:
    api_request_wrapper = ApiRequestsWrapper(request.param.get("url"))
    yield api_request_wrapper