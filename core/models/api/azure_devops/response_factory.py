from typing import Dict, Any


class AzureResponseFactory:
    @staticmethod
    def create_response_object(response_type: Any, as_dict: Dict[str, Any]):
        if response_type is not None:
            return response_type.from_dict(as_dict)
        else:
            return None