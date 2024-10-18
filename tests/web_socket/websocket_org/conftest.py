import pytest

from core.wrappers.web_socket.async_web_socket_client import AsyncWebSocketClient


@pytest.fixture()
@pytest.mark.asyncio
async def wss_client(request) -> AsyncWebSocketClient:
    websocket_client = AsyncWebSocketClient(request.param.get("uri"))
    await websocket_client.connect()

    # The first message should be received and skipped. Contains information about connection
    await websocket_client.receive_message()

    yield websocket_client

    await websocket_client.close()
