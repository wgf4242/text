
import frida
with open('./tmp.js', 'r') as f:
  code = f.read()

# start 1
def start1():
  session = frida.attach('TestAdd.exe')
  # session.enable_debugger()

  script = session.create_script(code)
  script.load()
  input('Pause')


# --- Method2
def start2():
  pid = frida.spawn('./TestAdd.exe')
  session = frida.attach(pid)

  script = session.create_script(code)
  script.load()

  frida.resume(pid)
