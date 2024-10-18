from dataclasses import dataclass
from typing import Dict, Any

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ResponsePostAttachment:
    id: str
    url: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            id = data.get("id"),
            url = data.get("url")
        )
