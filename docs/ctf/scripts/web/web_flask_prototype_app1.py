# 第一届陕西大学生CTF  Web-PPP # https://mp.weixin.qq.com/s/5wS4oMPuME4loTxG0D4C-A
# https://tttang.com/archive/1876/ 
from flask import Flask,request
import json

app = Flask(__name__)

def merge(src, dst):
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)

def evilFunc(arg_1 , * , shell = False):
    if not shell:
        print(arg_1)
    else:
        
        print(__import__("os").popen(arg_1).read())

class Family:
    def __init__(self):
        pass  

family = Family()

@app.route('/',methods=['POST', 'GET'])
def index():
    print(request.data)
    if request.data:
        merge(json.loads(request.data), family)
        evilFunc("whoami")
    return "fun"

@app.route('/eval',methods=['GET'])
def eval():
    if request.args.get('cmd'):
        cmd = request.args.get('cmd')
        evilFunc(cmd)
    return "ok"


app.run(host="0.0.0.0",port= 3000,debug=False)