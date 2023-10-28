import json
import os


class Configuration:
    def __init__(self, default_browser, implicit_wait):
        self.default_browser = default_browser
        self.implicit_wait = implicit_wait

class ConfigUtils:

    @staticmethod
    def get_config() -> Configuration:

        config_path = os.path.join(os.path.dirname(__file__), '../../config.json')
        with open(config_path) as config_file:
            config = json.load(config_file)

        return Configuration(config['default_browser'], config['implicit_wait'])