from re import match

import win32api
import win32con


def apply_scroll(direction: str):
    match(direction):
        case "down":
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -120)
        case "up":
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 120)
        case "left":
            win32api.mouse_event(win32con.MOUSEEVENTF_HWHEEL, 0, 0, -120)
        case "right":
            win32api.mouse_event(win32con.MOUSEEVENTF_HWHEEL, 0, 0, 120)

def _scroll_down_menu_settings(self, distance=400):
    action = ActionChains(self.driver)
    window_size = self.driver.get_window_size()
    x, y = window_size['width'] / 6, window_size['height'] / 2
    action.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
    action.w3c_actions.pointer_action.move_to_location(x, y)
    action.w3c_actions.pointer_action.click_and_hold()
    action.w3c_actions.pointer_action.move_to_location(x, y - distance)
    action.w3c_actions.pointer_action.release()
    action.w3c_actions.perform()