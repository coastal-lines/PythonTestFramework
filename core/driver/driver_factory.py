import enum
from dataclasses import dataclass
import selenium.webdriver
from selenium import webdriver


'''
@dataclass
class Browser:
    browser_name: str
    is_remote: bool
    is_headless: bool

class WebBrowser:
    firefox = Browser(browser_name="firefox", is_remote=False, is_headless=False)
    chrome = Browser(browser_name="chrome", is_remote=False, is_headless=False)
'''


def init_web_driver(web_browser: str) -> webdriver:
    match web_browser:
        case "FIREFOX":
            return selenium.webdriver.Firefox()
        case "CHROME":
            return selenium.webdriver.Chrome()
        case _:
            raise Exception(f"Browser {web_browser} not supported.")
