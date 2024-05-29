import frida
import sys
 
 
def main(target_process):
    session = frida.attach(target_process)

    script = session.create_script('''
    ...
    ''')

    script.load()
    print("Process attached successfully!")
    sys.stdin.read()

if __name__ == '__main__':
    target_process = 'WeChat.exe'
    main(target_process)