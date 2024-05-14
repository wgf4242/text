# https://github.com/ctfs/write-ups-2015/blob/master/seccon-quals-ctf-2015/binary/reverse-engineering-android-apk-1/rps.apk
# 读取同名js文件
from pathlib import Path

import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
        # script.unload(); exit(0)
    else:
        print(message)


js_file = Path(__file__).stem + '.js'
jscode = open(js_file, 'r', encoding='utf8').read()
# jscode = """
# Java.perform(function () {
#         send("hook start");
#         send("hook end");
# });
# """
device = frida.get_usb_device()
pid = device.spawn('owasp.mstg.uncrackable1')
session = device.attach(pid)

"""# attach 运行的程序
app = device.get_frontmost_application()
session = device.attach(app.pid)
"""
script = session.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()
