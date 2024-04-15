import pytest

from core.utils import generators_helper
from core.wrappers.api.api_requests_wrapper import ApiRequestsWrapper
from core.models.api.kucoin.token_response_model import PublicTokenResponse
from core.wrappers.web_socket.web_socket_client import WebSocketClient


def get_public_token(request):
    api_request_wrapper = ApiRequestsWrapper(request.param.get("url"))
    api_response = api_request_wrapper.post(request.param.get("end_point"), None, None)
    public_token_obj = PublicTokenResponse.from_json(api_response.text)
    return public_token_obj

@pytest.fixture
def wss_client(request) -> WebSocketClient:
    public_token_obj = get_public_token(request)

    token = generators_helper.generate_uid()
    uri = f"wss://ws-api-spot.kucoin.com/?token={public_token_obj.data.token}&[connectId={token}]"

    websocket_client = WebSocketClient(uri, False)
    websocket_client.connect()
    yield websocket_client
    websocket_client.close()