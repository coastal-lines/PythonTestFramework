from dataclasses import dataclass
from typing import Dict, Any

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class WebSocketHandshakeModel:
    def __init__(self, response_data: Dict[str, Any]):
        self.upgrade = response_data["upgrade"]
        self.connection = response_data["connection"]
        self.sec_websocket_accept = response_data["sec-websocket-accept"]
        self.date = response_data["date"]
        self.server = response_data["server"]
        self.via = response_data["via"]
        self.fly_request_id = response_data["fly-request-id"]

