from selenium.webdriver.remote.webdriver import WebDriver


class WebDriverHelper:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def maximize_window(self):
        self.__driver.maximize_window()

    def set_window_size(self, width: int, height: int, windowHandle: str = "current"):
        self.__driver.set_window_size(width, height, windowHandle)

