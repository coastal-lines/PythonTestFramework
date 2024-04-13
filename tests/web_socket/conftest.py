import pytest

from core.wrappers.web_socket.web_socket_client import AsyncWebSocketClient


@pytest.fixture()
@pytest.mark.asyncio
async def wss_client(request) -> AsyncWebSocketClient:
    websocket_client = AsyncWebSocketClient(request.param.get("uri"))

    await websocket_client.connect()
    await websocket_client.receive_message()

    yield websocket_client

    await websocket_client.close()