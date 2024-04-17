import json
import os
import threading
from typing import Any
from attr import dataclass


@dataclass
class Api:
    karaburma_host: str
    karaburma_port: str
    karaburma_base_url: str
    karaburma_work_dir: str
    karaburma_main_script_path: str

    def from_dict(obj: Any) -> "Api":
        _karaburma_base_url = str(obj.get("karaburma_base_url"))
        _karaburma_host = str(obj.get("karaburma_host"))
        _karaburma_port = str(obj.get("karaburma_port"))
        _karaburma_work_dir = str(obj.get("karaburma_work_dir"))
        _karaburma_main_script_path = str(obj.get("karaburma_main_script_path"))
        return Api(_karaburma_host, _karaburma_port, _karaburma_base_url, _karaburma_work_dir, _karaburma_main_script_path)

@dataclass
class Application:
    application_path: str
    application_process_name: str
    application_window_name: str

    @staticmethod
    def from_dict(obj: Any) -> "Application":
        return Application(
            application_path=str(obj.get("application_path")),
            application_process_name=str(obj.get("application_process_name")),
            application_window_name=str(obj.get("application_window_name"))
        )

@dataclass
class Desktop:
    default_os: str
    winappdriver_url: str
    winappdriver_port: str
    appium_url: str
    appium_port: str
    applications: Application

    @staticmethod
    def from_dict(obj: Any) -> "Desktop":
        _default_os = str(obj.get("default_os"))
        _winappdriver_url = str(obj.get("winappdriver_url"))
        _winappdriver_port = str(obj.get("winappdriver_port"))
        _appium_url = str(obj.get("appium_url"))
        _appium_port = str(obj.get("appium_port"))
        _applications = {
                app_name: Application.from_dict(app_data) for app_name, app_data in obj.get("applications", {}).items()
            }
        return Desktop(_default_os, _winappdriver_url, _winappdriver_port, _appium_url, _appium_port, _applications)

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
class Mobile:
    default_platform: str
    default_mode: str
    appium_url: str
    appium_port: str
    emulator_port_number: str
    emulator_device_name: str
    emulator_process_name: str

    @staticmethod
    def from_dict(obj: Any) -> "Mobile":
        _default_platform = str(obj.get("default_platform"))
        _default_mode = str(obj.get("default_mode"))
        _appium_url = str(obj.get("appium_url"))
        _appium_port = str(obj.get("appium_port"))
        _emulator_port_number = str(obj.get("emulator_port_number"))
        _emulator_device_name = str(obj.get("emulator_device_name"))
        _emulator_process_name = str(obj.get("emulator_process_name"))
        return Mobile(_default_platform, _default_mode, _appium_url, _appium_port, _emulator_port_number, _emulator_device_name, _emulator_process_name)

@dataclass
class Browserstack:
    username: str
    access_key: str
    url: str

    def from_dict(obj: Any) -> "Browserstack":
        _username = str(obj.get("username"))
        _access_key = str(obj.get("access_key"))
        _url = str(obj.get("url"))
        return Browserstack(_username, _access_key, _url)

@dataclass
class Karaburma:
    config_path: str

    def from_dict(obj: Any) -> "Karaburma":
        _config_path = str(obj.get("config_path"))
        return Karaburma(_config_path)

@dataclass
class Configuration:
    api: Api
    web: Web
    desktop: Desktop
    mobile: Mobile
    browserstack: Browserstack
    karaburma: Karaburma

    @staticmethod
    def from_dict(obj: Any) -> "Configuration":
        _api = Api.from_dict(obj.get("api"))
        _web = Web.from_dict(obj.get("web"))
        _desktop = Desktop.from_dict(obj.get("desktop"))
        _mobile = Mobile.from_dict(obj.get("mobile"))
        _browserstack = Browserstack.from_dict(obj.get("browserstack"))
        _karaburma = Karaburma.from_dict(obj.get("karaburma"))
        return Configuration(_api, _web, _desktop, _mobile, _browserstack, _karaburma)

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