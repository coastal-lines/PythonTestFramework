import json
import os
from typing import Any
from attr import dataclass

@dataclass
class Desktop:
    default_os: str
    winappdriver_url: str
    winappdriver_port: str

    @staticmethod
    def from_dict(obj: Any) -> 'Desktop':
        _default_os = str(obj.get("default_os"))
        _winappdriver_url = str(obj.get("winappdriver_url"))
        _winappdriver_port = str(obj.get("winappdriver_port"))
        return Desktop(_default_os, _winappdriver_url, _winappdriver_port)

@dataclass
class Web:
    default_browser: str
    wait_timeout: int

    '''
    'Web' - IDE reads string 'Web' as link to class. 
     Web  - IDE reads object 'Web' as link to initialized object.
    '''
    @staticmethod
    def from_dict(obj: Any) -> 'Web':
        _default_browser = str(obj.get("default_browser"))
        _wait_timeout = int(obj.get("wait_timeout"))
        return Web(_default_browser, _wait_timeout)

@dataclass
class Configuration:
    web: Web
    desktop: Desktop

    @staticmethod
    def from_dict(obj: Any) -> 'Configuration':
        _web = Web.from_dict(obj.get("web"))
        _desktop = Desktop.from_dict(obj.get("desktop"))
        return Configuration(_web, _desktop)


class ConfigUtils:

    @staticmethod
    def get_config() -> Configuration:

        config_path = os.path.join(os.path.dirname(__file__), '../../config.json')
        with open(config_path) as config_file:
            config_json = json.load(config_file)

        #return Configuration(config['default_browser'], config['wait_timeout'])
        return Configuration.from_dict(config_json)

