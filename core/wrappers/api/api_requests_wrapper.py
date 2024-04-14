import requests

from core.models.api.api_response_model import ApiResponseModel


class ApiRequestsWrapper:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, url="/") -> ApiResponseModel:
        response = requests.get(url=self.base_url + url)
        return self.__prepare_response(response)

    def post_without_any_data(self, url) -> ApiResponseModel:
        response = requests.post(url=self.base_url + url)
        return self.__prepare_response(response)

    def post(self, url, payload, headers) -> ApiResponseModel:
        response = requests.post(url=self.base_url + url, data=payload, headers=headers)
        return self.__prepare_response(response)

    def __prepare_response(self, response: requests.Response) -> ApiResponseModel:
        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        return ApiResponseModel(response.status_code, response.text, response.headers, as_dict)