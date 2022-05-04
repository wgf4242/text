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
  main.onClick.implementation = function (v) {
    send("Hook Start...")
    this.onClick(v);
    send(this.cnt);
    send(this.m);
    send(this.n);
    this.cnt.value = 999;
    this.m.value = 0;
    this.n.value = 1;
    send("Success!")
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
