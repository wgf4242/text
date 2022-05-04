"""
爆破前，需要打开程序并随便输入东西点下按钮，不然就会出现这个报错(踩坑++
https://www.52pojie.cn/thread-1163598-1-1.html
1. 根据Wrong定位到 0x0040173A
2. x32dbg调试，F7,F8跟一下，到sub_401CE7就有返回结果了，可hook此处返回值，
"""

import frida
import sys
 
 
def on_message(message, data):
    print("[%s] => %s" % (message, data))
 
session = frida.attach('CTF.exe')
script = session.create_script('''
 
    var number = 720000;
    var needAdd = true;
      
    var enter=new NativeFunction(ptr('0x0040173a'), 'void',[]);
    rpc.exports={
        once:function(){
            enter();
        }
    };
    var input = ptr('0x00401CE7');//函数入口
    Interceptor.attach(input,{
        onLeave:function(result)//hook返回值
        {
            Memory.writeAnsiString(ptr(result.toInt32()),number.toString())
            if(needAdd){
                number=number+1;
                needAdd=false;
            }
            else{
                needAdd=true;
            }
 
        }
    });
 
''')
script.on('message', on_message)
script.load()
while (1):
    script.exports.once()
sys.stdin.read()
session.deatch()