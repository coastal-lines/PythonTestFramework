from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class InstanceServer:
    endpoint: str
    encrypt: bool
    protocol: str
    pingInterval: int
    pingTimeout: int

@dataclass_json
@dataclass
class Data:
    token: str
    instanceServers: List[InstanceServer]

@dataclass_json
@dataclass
class PublicTokenResponse:
    code: str
    data: Data