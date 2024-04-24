import requests

from core.models.api.api_response_model import ApiResponseModel
from core.models.api.azure_devops.response_factory import AzureResponseFactory


class ApiRequestsWrapper:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, url="/", payload=None, headers=None, auth=None) -> ApiResponseModel:
        response = requests.get(url=self.base_url + url, data=payload, headers=headers, auth=auth)
        return self.__prepare_response(response)

    def post(self, url, auth=None, payload=None, headers=None, files=None) -> ApiResponseModel:
        response = requests.post(url=self.base_url + url, auth=auth, data=payload, headers=headers, files=files)
        return self.__prepare_response(response)

    def patch(self, url, payload=None, headers=None, auth=None, response_model=None) -> ApiResponseModel:
        response = requests.patch(url=self.base_url + url, auth=auth, data=payload, headers=headers)
        return self.__prepare_response(response, response_model=response_model)

    def __prepare_response(self, response: requests.Response, response_model=None) -> ApiResponseModel:
        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        model = None
        if response_model is not None:
            model = AzureResponseFactory.create_response_object(response_model, as_dict)

        return ApiResponseModel(response.status_code, response.text, dict(response.headers), dict(response.cookies.items()), as_dict, model)
