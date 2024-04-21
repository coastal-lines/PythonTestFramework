from dataclasses import dataclass

from requests.cookies import RequestsCookieJar


@dataclass
class ApiResponseModel:
    status_code: int
    text: str
    headers: object
    cookies: list
    as_dict: dict