# 1.启动 TestAdd.exe
# 2.python .\communication.py TestAdd.exe
# 注意驼峰命名 python处是 test_comm js是 testComm
import codecs
import frida
import sys

def on_message(message, data):
    if message['type'] == 'send':
        modules = message['payload']
        target = ""
        for mod in modules:
            if sys.argv[1] in mod['name']:
                target = str(mod)
            break
        script.post({'my_data': target})
    elif message['type'] == 'error':
        print(message['stack'])

session = frida.attach(sys.argv[1])
with codecs.open('./communication.ts', 'r', 'utf-8') as f:
    source = f.read()
script = session.create_script(source)
script.on('message', on_message)
script.load()
script.exports.test_comm()