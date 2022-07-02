import frida
with open('./a.js', 'r', encoding='utf8') as f:
  code = f.read()



# 20050  MobileB  com.example.mobileb

# pid = frida.spawn('./Newbie_calculations.exe')
device = frida.get_device_manager().enumerate_devices()[-1]
# then attach to your process: session = device.attach('1741')
print(device)
print(frida.get_usb_device())
print(dir(frida))
d = frida.get_device_manager()
oneplus = d.get_device('458f4aa5')
session = oneplus.attach("MobileB")
# session = device.attach("MobileB")
script = session.create_script(code)
script.load()
input()
# frida.resume(pid)
