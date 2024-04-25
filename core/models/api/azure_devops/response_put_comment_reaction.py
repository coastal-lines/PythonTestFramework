from dataclasses import dataclass
from typing import Dict, Any

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ResponsePutCommentReaction:
    type: str
    count: int
    isCurrentUserEngaged: bool
    commentId: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            type=data.get("type"),
            count=data.get("count"),
            isCurrentUserEngaged=data.get("isCurrentUserEngaged"),
            commentId=data.get("commentId")
        )
