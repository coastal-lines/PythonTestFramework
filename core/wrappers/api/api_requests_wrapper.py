import requests

from core.models.api.api_response_model import ApiResponseModel


class ApiRequestsWrapper:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, url="/", payload=None, headers=None) -> ApiResponseModel:
        response = requests.get(url=self.base_url + url, data=payload, headers=headers)
        return self.__prepare_response(response)

    def post_without_any_data(self, url) -> ApiResponseModel:
        response = requests.post(url=self.base_url + url)
        return self.__prepare_response(response)

    def post(self, url, payload, headers) -> ApiResponseModel:
        response = requests.post(url=self.base_url + url, data=payload, headers=headers)
        return self.__prepare_response(response)

    def __prepare_response(self, response: requests.Response) -> ApiResponseModel:
        try:
            orig_repsonse = response.json()
        except Exception:
            orig_repsonse = {}

        return ApiResponseModel(response.status_code, response.text, response.headers, list(response.cookies.items()), orig_repsonse)