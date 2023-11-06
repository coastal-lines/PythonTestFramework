from typing import Any
from attr import dataclass


@dataclass
class Desktop:
    default_os: str

    @staticmethod
    def from_dict(obj: Any) -> 'Desktop':
        _default_os = str(obj.get("default_os"))
        return Desktop(_default_os)

'''
@dataclass
class Web:
    default_browser: str
    wait_timeout: int

    @staticmethod
    def from_dict(obj: Any) -> 'Web':
        _default_browser = str(obj.get("default_browser"))
        _wait_timeout = int(obj.get("wait_timeout"))
        return Web(_default_browser, _wait_timeout)
'''

@dataclass
class Root:

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _web = Web(from_dict(obj.get("web")))
        _desktop = Desktop.from_dict(obj.get("desktop"))
        return Root(_web, _desktop)

    class Web:
        default_browser: str
        wait_timeout: int

        def __init__(self, obj: Any) -> 'Web':
            _default_browser = str(obj.get("default_browser"))
            _wait_timeout = int(obj.get("wait_timeout"))
            return Web(_default_browser, _wait_timeout)

'''
class Configuration:

    def __init__(self, web_config, desktop_config):
        self.web_config = default_browser
        self.desktop_config = wait_timeout


class ConfigUtils:

    @staticmethod
    def get_config() -> Configuration:

        config_path = os.path.join(os.path.dirname(__file__), '../../config.json')
        with open(config_path) as config_file:
            config = json.load(config_file)

        return Configuration(config['default_browser'], config['wait_timeout'])
'''
