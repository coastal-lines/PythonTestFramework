from dataclasses import dataclass


@dataclass
class ApiResponseWrapper:
    status_code: int
    text: str
    headers: dict
    as_dict: object