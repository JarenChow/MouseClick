# encoding=utf-8
import ctypes
import win32api
import time
import win32con
import pyhk
import thread

SLEEP_TIME = 0.05
CLICK_RUN = False
CLICK_POSITION_X = 550
CLICK_POSITION_Y = 400


def mouse_move(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)


def mouse_click():
    # mouse_move(380, 490)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def game_click():
    # mouse_move(CLICK_POSITION_X, CLICK_POSITION_Y)
    while 1:
        if CLICK_RUN:
            mouse_click()
        time.sleep(SLEEP_TIME)


def switch_status():
    global CLICK_RUN
    CLICK_RUN = not CLICK_RUN

print u"F8 启动与停止"
thread.start_new_thread(game_click, ())
hot = pyhk.pyhk()
hot.addHotkey(['F8'], switch_status)
hot.start()
