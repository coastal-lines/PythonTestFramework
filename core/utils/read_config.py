import json
import os


class Configuration:

    def __init__(self, default_browser, wait_timeout):
        self.default_browser = default_browser
        self.wait_timeout = wait_timeout

class ConfigUtils:

    @staticmethod
    def get_config() -> Configuration:

        config_path = os.path.join(os.path.dirname(__file__), '../../config.json')
        with open(config_path) as config_file:
            config = json.load(config_file)

        return Configuration(config['default_browser'], config['wait_timeout'])