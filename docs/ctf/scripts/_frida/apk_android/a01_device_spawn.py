# https://github.com/ctfs/write-ups-2015/blob/master/seccon-quals-ctf-2015/binary/reverse-engineering-android-apk-1/rps.apk
# https://github.com/OWASP/owasp-mastg/blob/master/Crackmes/Android/Level_01/UnCrackable-Level1.apk
# 读取同名js文件
package_name = 'owasp.mstg.uncrackable1'

from pathlib import Path
import frida


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


js_file = Path(__file__).stem + '.js'
jscode = open(js_file, 'r', encoding='utf8').read()

# device = frida.get_device_manager().enumerate_devices()[-1]
device = frida.get_usb_device()
pid = device.spawn(package_name)
print(pid)
session = device.attach(pid)

script = session.create_script(jscode)

script.on('message', on_message)
print('[*] Running CTF')

script.load()
device.resume(pid)

# sys.stdin.read()
input()
