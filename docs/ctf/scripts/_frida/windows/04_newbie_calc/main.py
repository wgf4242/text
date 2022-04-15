import frida
with open('./main.js', 'r', encoding='utf8') as f:
  code = f.read()

pid = frida.spawn('./Newbie_calculations.exe')
session = frida.attach(pid)

script = session.create_script(code)
script.load()

frida.resume(pid)
