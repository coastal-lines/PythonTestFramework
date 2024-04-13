import requests

from wrappers.api.api_response_wrapper import ApiResponseWrapper


class ApiRequestsWrapper:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, url="/"):
        response = requests.get(url=self.base_url + url)
        return self.__prepare_response(response)

    def post(self, url, payload, headers):
        response = requests.post(url=self.base_url + url, data=payload, headers=headers)
        return self.__prepare_response(response)

    def __prepare_response(self, response):
        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        return ApiResponseWrapper(response.status_code, response.text, response.headers, as_dict)