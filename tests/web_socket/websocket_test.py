import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize("wss_client", [{"uri": "wss://echo.websocket.org"}], indirect=True)
async def test_connection_status_101(wss_client):
    async for client in wss_client:
        status_code = await client.get_connection_status()
        assert status_code == 101

@pytest.mark.asyncio
@pytest.mark.parametrize("wss_client", [{"uri": "wss://echo.websocket.org"}], indirect=True)
async def test_connection_close(wss_client):
    async for client in wss_client:
        await client.close()
        assert not client.websocket.connected

@pytest.mark.asyncio
@pytest.mark.parametrize("wss_client", [{"uri": "wss://echo.websocket.org"}], indirect=True)
async def test_send_message_and_read_response(wss_client):
    async for client in wss_client:
        await client.send_message("{'value': 'Echo Test'}")
        response = await client.receive_message()
        assert response == "{'value': 'Echo Test'}"

@pytest.mark.asyncio
@pytest.mark.parametrize("wss_client", [{"uri": "wss://echo.websocket.org"}], indirect=True)
async def test_validate_response_headers(wss_client):
    async for client in wss_client:
        handshake_response = await client.get_connection_handshake()

        assert handshake_response.upgrade == "websocket"
        assert handshake_response.connection == "Upgrade"
        assert handshake_response.via == "1.1 fly.io"
        assert "2024" in handshake_response.date
        assert "2024" in handshake_response.server
        assert handshake_response.fly_request_id is not None
        assert handshake_response.sec_websocket_accept is not None


async def test_ping_pong():
    api = ApiRequestsWrapper("https://api.kucoin.com/")
    resp_ = api.post("api/v1/bullet-public", None, None)
    response_data = ResponseData.from_json(resp_.text)
