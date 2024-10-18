from core.utils.config_manager import ConfigUtils


class AzureDTO:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.organization = ConfigUtils().get_config().azure_dev_ops.organization
            self.project = ConfigUtils().get_config().azure_dev_ops.project
            self.basic_authorization = ("any_user", ConfigUtils().get_config().azure_dev_ops.token_for_full_access)
            self.initialized = True
