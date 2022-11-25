import frida
import sys


def frida_attach():
    def on_message(message, data):
        if message['type'] == 'send':
            print("[*] {0}".format(message['payload']))
        else:
            print(message)

    with open("./frida-hook.js", "r", encoding="utf-8") as fp:
        hook_string = fp.read()

    # 方式一：attach 模式，已经启动的 APP
    process = frida.get_usb_device(-1).attach("Uncrackable1")
    script = process.create_script(hook_string)
    script.on("message", on_message)
    script.load()
    sys.stdin.read()


def frida_spawn():
    def on_message(message, data):
        if message['type'] == 'send':
            print("[*] {0}".format(message['payload']))
        else:
            print(message)

    with open("./frida-hook.js", "r", encoding="utf-8") as fp:
        hook_string = fp.read()

    # 方式二，spawn 模式，重启 APP
    device = frida.get_usb_device(-1)
    pid = device.spawn(["owasp.mstg.uncrackable1"])
    process = device.attach(pid)
    script = process.create_script(hook_string)
    script.on("message", on_message)
    script.load()
    device.resume(pid)
    sys.stdin.read()


# 新版本不用包名 用App标题

def get_pid(name='Uncrackable1'):
    device = frida.get_device_manager().enumerate_devices()[-1]
    processes = device.enumerate_processes()
    for process in processes:
        print(process)
        if process.name == name:
            return process.pid
