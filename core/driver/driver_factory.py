from dataclasses import dataclass
import selenium.webdriver
from selenium import webdriver


@dataclass
class Browser:
    browser_name: str
    is_remote: bool
    is_headless: bool

class WebBrowser:
    firefox = Browser(browser_name="firefox", is_remote=False, is_headless=False)
    chrome = Browser(browser_name="chrome", is_remote=False, is_headless=False)

class DriverFactory:
    def init_web_driver(self, web_browser: Browser) -> webdriver:
        match web_browser.browser_name:
            case "firefox":
                return selenium.webdriver.Firefox()
            case "chrome":
                return selenium.webdriver.Chrome()
            case _:
                raise Exception(f"Browser {web_browser.browser_name} not supported.")
