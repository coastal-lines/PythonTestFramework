import appium
from appium.webdriver.common.touch_action import TouchAction


def swipe_right(driver: appium.webdriver, start_x=900, end_x=100):
    TouchAction(driver).press(x=start_x, y=500).wait(1000).move_to(x=end_x, y=500).release().perform()