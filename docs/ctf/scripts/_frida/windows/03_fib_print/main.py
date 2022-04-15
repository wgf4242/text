import frida
with open('./optimize_fib.js', 'r') as f:
  code = f.read()

session = frida.attach('fib_print.exe')
# session.enable_debugger()
session.enable_debugger()
script = session.create_script(code)
script.load()
input('Pause')
