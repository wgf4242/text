import frida


# 新版本不用包名 用App标题

def get_pid(name = 'Uncrackable1'):
    device = frida.get_device_manager().enumerate_devices()[-1]
    processes = device.enumerate_processes()
    for process in processes:
        print(process)
        if process.name == name:
            return process.pid

