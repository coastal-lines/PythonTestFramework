from core.api.clients.base_client import BaseClient
from core.utils.config_manager import ConfigUtils


class KaraburmaClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.base_url = ConfigUtils().get_config().api.karaburma_base_url