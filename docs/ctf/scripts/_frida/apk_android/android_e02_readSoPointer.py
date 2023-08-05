# 2015阿里移动安全挑战赛第二题AliCrackme_2
# https://mp.weixin.qq.com/s/X5B3TABoV8nQ1BHHlQHAZg
# https://blog.csdn.net/weixin_42011443/article/details/105897429
import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


# jscode = open('android_e02_readSoPointer.js', 'r', encoding='utf8').read()
jscode = open('android_e02_readSoPointer1.js', 'r', encoding='utf8').read()

device = frida.get_usb_device()
pid = device.spawn('com.yaotong.crackme')
print(pid)
session = device.attach(pid)
device.resume(pid)

# 当前这个要先继续后加载脚本
script = session.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')

script.load()
# device.resume(pid)
input()
