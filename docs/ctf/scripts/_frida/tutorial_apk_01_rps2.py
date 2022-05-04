# 提前启动 或 按返回，到桌面再启动 触发onCreate,
# https://github.com/ctfs/write-ups-2015/blob/master/seccon-quals-ctf-2015/binary/reverse-engineering-android-apk-1/rps.apk
# https://www.bilibili.com/video/BV15y4y1H7Px?spm_id_from=333.999.0.0
import frida, sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

jscode = """
Java.perform(function () {
  var main = Java.use('com.example.seccon2015.rock_paper_scissors.MainActivity');
  main.onCreate.implementation = function (a) {
    send("Hook Start...")
    send("SECCON(" + (1000 + this.calc()) * 107 + "1")
    send("Success!")
    this.onCreate(a)
  }
})
"""

process = frida.get_usb_device().attach('rock_paper_scissors')
# process = frida.get_usb_device().attach('com.example.seccon2015.rock_paper_scissors')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()
