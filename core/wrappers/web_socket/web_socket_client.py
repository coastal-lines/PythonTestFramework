from typing import Union, Any
from typing_extensions import Dict
import websocket as ws
from websocket import WebSocketAddressException

from core.models.web_socket.web_socket_handshake_model import WebSocketHandshakeModel
from models.api.kucoin.response_connected_model import MainResponseModel


class WebSocketClient:
    def __init__(self, uri: str, is_trace_enabled=True):
        self.uri = uri

        if is_trace_enabled:
            ws.enableTrace(True)

        self.websocket = ws.WebSocket()

    def connect(self):
        try:
            self.websocket.connect(self.uri)
        except WebSocketAddressException:
            print(f"Wrong URI. Please check Websocket Uri: {self.uri}")

    def send_message(self, message: str):
        self.websocket.send(message)

    def receive_message(self) -> Union[str, bytes]:
        return self.websocket.recv()

    def get_connection_status(self) -> int:
        return self.websocket.getstatus()

    def get_connection_handshake_headers(self) -> Dict[str, Any]:
        return self.websocket.handshake_response.headers

    def get_connection_handshake(self) -> WebSocketHandshakeModel:
        handshake_response = self.get_connection_handshake_headers()
        return WebSocketHandshakeModel(handshake_response)

    def close(self):
        self.websocket.close()