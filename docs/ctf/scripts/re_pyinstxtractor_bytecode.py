# -*- coding:utf-8 -*-
# 要使用对应的python版本
# 例删除2条指令, 3字节/条指令
# len(code.co_code) 如果27 修改为 27-6=21
import dis, marshal

filename = '1.pyc'
f =open(filename, 'rb').read()

# code = marshal.loads(f[8:]) # python2
code = marshal.loads(f[16:])
dis.dis(code)
print(code)
print(len(code.co_code))
