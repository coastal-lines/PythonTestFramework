import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class WaitingManager:

    def __init__(self, driver):
        self.__driver = driver

    def force_wait(self):
        wait_time = 60
        start_time = time.time()

        el = None

        while True:
            current_time = time.time()

            if current_time - start_time >= wait_time:
                break

            try:
                el = WebDriverWait(super().driver, ConfigUtils.get_config().web.wait_timeout).until(
                    EC.element_to_be_clickable(super().driver.find_element(*self.QUESTION)))
                if (el != None):
                    break
            except (Exception) as ex:
                print("Waiting element.")
                time.sleep(3)

        if (el == None):
            raise NoSuchElementException("Element was not found.")