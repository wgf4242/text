# 支持剪贴版操作，复制到剪贴版直接运行
import string
from pathlib import Path

import win32api
import win32clipboard
import win32con
import time

time.sleep(0.5)

keys = {"shift": win32con.MOD_SHIFT, "control": win32con.MOD_CONTROL, "ctrl": win32con.MOD_CONTROL, "alt": win32con.VK_MENU, "win": win32con.MOD_WIN, "up": win32con.VK_UP, "down": win32con.VK_DOWN, "left": win32con.VK_LEFT, "right": win32con.VK_RIGHT, "pgup": win32con.VK_PRIOR,
        "pgdown": win32con.VK_NEXT, "home": win32con.VK_HOME, "end": win32con.VK_END, "insert": win32con.VK_INSERT, "enter": win32con.VK_RETURN, "return": win32con.VK_RETURN, "tab": win32con.VK_TAB, "space": win32con.VK_SPACE, "backspace": win32con.VK_BACK, "delete": win32con.VK_DELETE,
        "del": win32con.VK_DELETE, "apps": win32con.VK_APPS, "popup": win32con.VK_APPS, "escape": win32con.VK_ESCAPE, "npmul": win32con.VK_MULTIPLY, "npadd": win32con.VK_ADD, "npsep": win32con.VK_SEPARATOR, "npsub": win32con.VK_SUBTRACT, "npdec": win32con.VK_DECIMAL, "npdiv": win32con.VK_DIVIDE,
        "np0": win32con.VK_NUMPAD0, "numpad0": win32con.VK_NUMPAD0, "np1": win32con.VK_NUMPAD1, "numpad1": win32con.VK_NUMPAD1, "np2": win32con.VK_NUMPAD2, "numpad2": win32con.VK_NUMPAD2, "np3": win32con.VK_NUMPAD3, "numpad3": win32con.VK_NUMPAD3, "np4": win32con.VK_NUMPAD4,
        "numpad4": win32con.VK_NUMPAD4, "np5": win32con.VK_NUMPAD5, "numpad5": win32con.VK_NUMPAD5, "np6": win32con.VK_NUMPAD6, "numpad6": win32con.VK_NUMPAD6, "np7": win32con.VK_NUMPAD7, "numpad7": win32con.VK_NUMPAD7, "np8": win32con.VK_NUMPAD8, "numpad8": win32con.VK_NUMPAD8,
        "np9": win32con.VK_NUMPAD9, "numpad9": win32con.VK_NUMPAD9, "f1": win32con.VK_F1, "f2": win32con.VK_F2, "f3": win32con.VK_F3, "f4": win32con.VK_F4, "f5": win32con.VK_F5, "f6": win32con.VK_F6, "f7": win32con.VK_F7, "f8": win32con.VK_F8, "f9": win32con.VK_F9, "f10": win32con.VK_F10,
        "f11": win32con.VK_F11, "f12": win32con.VK_F12, "f13": win32con.VK_F13, "f14": win32con.VK_F14, "f15": win32con.VK_F15, "f16": win32con.VK_F16, "f17": win32con.VK_F17, "f18": win32con.VK_F18, "f19": win32con.VK_F19, "f20": win32con.VK_F20, "f21": win32con.VK_F21, "f22": win32con.VK_F22,
        "f23": win32con.VK_F23, "f24": win32con.VK_F24}

dicc = string.ascii_uppercase + string.digits
for c in dicc:
    keys.update({c.lower(): ord(c)})


def check_key(key_lst):
    lst = key_lst.split('+')
    return all(win32api.GetAsyncKeyState(keys.get(x)) != 0 for x in lst)


# get clipboard data
win32clipboard.OpenClipboard()
clip = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

fname = clip.split('\n')[0].strip('\r\n')
fname = fname.strip('题目名称：').replace(':', '_').replace('?', '_')


def create_hint(category=None):
    if not category:
        p = Path(fname)
        if not p.is_dir():
            p.mkdir()
        return open(parent / f'{fname}/hint.txt', 'w')
    fp = Path('.').joinpath(category, fname)
    if not fp.is_dir():
        fp.mkdir()
    f = open(parent / f'{category}/{fname}/hint.txt', 'w')
    return f


if __name__ == '__main__':
    parent = Path('.')
    if check_key('c'):
        f = create_hint('Crypto')
    elif check_key('m'):
        f = create_hint('Misc')
    elif check_key('p'):
        f = create_hint('pwn')
    elif check_key('w'):
        f = create_hint('Web')
    elif check_key('r'):
        f = create_hint('Reverse')
    else:
        f = create_hint()
    f.write(clip)
    f.close()
