from re import match

import win32api
import win32con


def windows_scroll(direction: str):
    match(direction):
        case "down":
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -120)
        case "up":
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 120)
        case "left":
            win32api.mouse_event(win32con.MOUSEEVENTF_HWHEEL, 0, 0, -120)
        case "right":
            win32api.mouse_event(win32con.MOUSEEVENTF_HWHEEL, 0, 0, 120)