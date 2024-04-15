import pytest

from core.utils import generators_helper
from core.models.api.kucoin.response_connected_model import MainResponseModel
from core.wrappers.api.api_requests_wrapper import ApiRequestsWrapper
from core.wrappers.web_socket.async_web_socket_client import AsyncWebSocketClient
from core.models.api.kucoin.token_response_model import PublicTokenResponse


@pytest.mark.parametrize("wss_client", [{"url":"https://api.kucoin.com/", "end_point":"api/v1/bullet-public"}], indirect=True)
def test_validate_welcome_connection_response(wss_client):
    response_connected = wss_client.receive_message()
    response_connected_model = MainResponseModel.from_json(response_connected)

    assert response_connected_model.id is not None
    assert response_connected_model.type == "welcome"

@pytest.mark.parametrize("wss_client", [{"url":"https://api.kucoin.com/", "end_point":"api/v1/bullet-public"}], indirect=True)
def test_ping_pong(wss_client):
    response = wss_client.receive_message()
    response_connected = MainResponseModel.from_json(response)

    request_payload = str({
        "id": response_connected.id,
        "type": "ping"
    })

    wss_client.send_message(request_payload)
    ping_response = wss_client.receive_message()
    response_model = MainResponseModel.from_json(ping_response)

    assert response_model.type == "pong"

@pytest.mark.parametrize("wss_client", [{"url":"https://api.kucoin.com/", "end_point":"api/v1/bullet-public"}], indirect=True)
def test_subscribe_response(wss_client):
    request_payload = str({
        "id": generators_helper.generate_int(),
        "type": "subscribe",
        "topic": "/market/ticker:BTC-USDT,ETH-USDT",
        "privateChannel": "false",
        "response": "true"
    })

    wss_client.receive_message()
    wss_client.send_message(request_payload)
    response = wss_client.receive_message()
    response_model = MainResponseModel.from_json(response)

    assert response_model.type == "ack"
