import pytest
import websocket

@pytest.fixture()
def wws_connection(request) -> websocket.WebSocket:
    uri = request.param.get("uri")
    ws = websocket.WebSocket()
    ws.connect(uri)
    ws.recv()
    yield ws
    ws.close()

@pytest.mark.parametrize("wws_connection", [{"uri": "wss://echo.websocket.org"}], indirect=True)
def test_connection_close(wws_connection):
    wws_connection.close()
    assert not wws_connection.connected

@pytest.mark.parametrize("wws_connection", [{"uri": "wss://echo.websocket.org"}], indirect=True)
def test_send_message_and_read_response(wws_connection):
    wws_connection.send("Echo Test")
    response = wws_connection.recv()
    assert response == "Echo Test"
    wws_connection.close()
