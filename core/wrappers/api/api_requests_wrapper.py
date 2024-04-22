import requests

from core.models.api.api_response_model import ApiResponseModel


class ApiRequestsWrapper:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, url="/", payload=None, headers=None, auth=None) -> ApiResponseModel:
        response = requests.get(url=self.base_url + url, data=payload, headers=headers, auth=auth)
        return self.__prepare_response(response)

    def post(self, url, auth=None, payload=None, headers=None, files=None) -> ApiResponseModel:
        response = requests.post(url=self.base_url + url, auth=auth, data=payload, headers=headers, files=files)
        return self.__prepare_response(response)

    def patch(self, url="/", payload=None, headers=None, auth=None) -> ApiResponseModel:
        response = requests.patch(url=self.base_url + url, auth=auth, data=payload, headers=headers)
        return self.__prepare_response(response)

    def __prepare_response(self, response: requests.Response) -> ApiResponseModel:
        try:
            orig_repsonse = response.json()
        except Exception:
            orig_repsonse = {}

        return ApiResponseModel(response.status_code, response.text, dict(response.headers), dict(response.cookies.items()), orig_repsonse)