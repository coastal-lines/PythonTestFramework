import requests

from core.api.api_response_wrapper import ApiResponseWrapper


class ApiRequestsWrapper:
    def get(self, url):
        response = requests.get(url=url)
        return self.__prepare_response(response)

    def post(self, url, headers, payload):
        response = requests.post(url=url, headers=headers, data=payload)
        return self.__prepare_response(response)

    def __prepare_response(self, response):
        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        return ApiResponseWrapper(response.status_code, response.text, response.headers, as_dict)