import websocket as ws


class AsyncWebSocketClient:
    def __init__(self, uri: str, is_trace_enabled=True):
        self.uri = uri

        if is_trace_enabled:
            ws.enableTrace(True)

        self.websocket = ws.WebSocket()

    async def connect(self):
        self.websocket.connect(self.uri)

    async def send_message(self, message):
        self.websocket.send(message)

    async def receive_message(self):
        return self.websocket.recv()

    async def get_connection_status(self):
        return self.websocket.getstatus()

    async def close(self):
        self.websocket.close()