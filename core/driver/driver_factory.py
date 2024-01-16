from collections import namedtuple


class WebBrowser:

    __FirefoxBrowser = namedtuple('browser', ['browser_name', 'is_remote', 'is_headless'])
    firefox = __FirefoxBrowser(browser_name="firefox", is_remote="False", is_headless="False")

    def __init__(self):
        pass