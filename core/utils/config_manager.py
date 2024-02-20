import json
import os
import threading
from typing import Any
from attr import dataclass


@dataclass
class Api:
    karaburma_base_url: str

    def from_dict(obj: Any) -> "Api":
        _karaburma_base_url = str(obj.get("karaburma_base_url"))
        return Api(_karaburma_base_url)

@dataclass
class Desktop:
    default_os: str
    winappdriver_url: str
    winappdriver_port: str
    appium_url: str
    appium_port: str
    application_exe_path: str

    @staticmethod
    def from_dict(obj: Any) -> "Desktop":
        _default_os = str(obj.get("default_os"))
        _winappdriver_url = str(obj.get("winappdriver_url"))
        _winappdriver_port = str(obj.get("winappdriver_port"))
        _appium_url = str(obj.get("appium_url"))
        _appium_port = str(obj.get("appium_port"))
        _application_exe_path = str(obj.get("application_exe_path"))

        return Desktop(_default_os, _winappdriver_url, _winappdriver_port, _appium_url, _appium_port, _application_exe_path)

@dataclass
class Web:
    default_browser: str
    wait_timeout: int

    '''
    'Web' - IDE reads string 'Web' as link to class. 
     Web  - IDE reads object 'Web' as link to initialized object.
    '''
    @staticmethod
    def from_dict(obj: Any) -> "Web":
        _default_browser = str(obj.get("default_browser"))
        _wait_timeout = int(obj.get("wait_timeout"))

        return Web(_default_browser, _wait_timeout)

@dataclass
class Configuration:
    api: Api
    web: Web
    desktop: Desktop

    @staticmethod
    def from_dict(obj: Any) -> "Configuration":
        _api = Api.from_dict(obj.get("api"))
        _web = Web.from_dict(obj.get("web"))
        _desktop = Desktop.from_dict(obj.get("desktop"))

        return Configuration(_api, _web, _desktop)

class ConfigUtilsThreadSafe:

    _instance = None
    _lock = threading.Lock()

    @staticmethod
    def get_config():
        if not ConfigUtilsThreadSafe._instance:
            with ConfigUtilsThreadSafe._lock:
                if not ConfigUtilsThreadSafe._instance:
                    ConfigUtilsThreadSafe._instance = ConfigUtilsThreadSafe._load_config()

        return ConfigUtilsThreadSafe._instance

    @staticmethod
    def _load_config() -> Configuration:
        config_path = os.path.join(os.path.dirname(__file__), "../../config.json")
        with open(config_path) as config_file:
            config_json = json.load(config_file)

        return Configuration.from_dict(config_json)

class ConfigUtils:

    _initialized = False
    _instance = None
    _config_data = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    @staticmethod
    def _load_config():
        if not ConfigUtils._initialized:
            config_path = os.path.join(os.path.dirname(__file__), "../../config.json")
            with open(config_path) as config_file:
                ConfigUtils._config_data = Configuration.from_dict(json.load(config_file))
            ConfigUtils._initialized = True

    @staticmethod
    def get_config():
        if not ConfigUtils._initialized:
            ConfigUtils._load_config()

        return ConfigUtils._config_data