from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ApiResponseModel:
    status_code: int
    text: str
    headers: dict
    cookies: dict
    as_dict: dict
    response_model: object = None
