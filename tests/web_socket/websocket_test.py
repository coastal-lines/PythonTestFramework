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


