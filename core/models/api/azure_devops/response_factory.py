from typing import Dict, Any


class AzureResponseFactory:
    @staticmethod
    def create_response_object(response_type: Any, as_dict: Dict[str, Any]):
        if response_type is not None:
            return response_type.from_dict(as_dict)
        else:
            return None

class User:
    def __init__(userId: int, id: int, title: str, body: str):
        userId = userId
        id = id
        title = title
        body = body

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {}
headers = {
  'Authorization': 'Basic YW55X3ZhbHVlOnl1c2htd2N2ZXhtM2t2bW5tZ3o0cHMycXduZXpsa3RxNmdnczNibTJxa2p4cW5iYnh3b2E='
}

response = requests.request("GET", url, headers=headers, data=payload)


print(response.text)