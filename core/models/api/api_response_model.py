from dataclasses import dataclass


@dataclass
class ApiResponseModel:
    status_code: int
    text: str
    headers: dict
    as_dict: object