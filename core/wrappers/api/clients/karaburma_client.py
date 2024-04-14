from core.wrappers.api.api_requests_wrapper import ApiRequestsWrapper
from core.wrappers.api.clients.base_client import BaseClient
from core.utils.config_manager import ConfigUtils


class KaraburmaClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.base_url = ConfigUtils().get_config().api.karaburma_base_url
        self.request = ApiRequestsWrapper(self.base_url)
