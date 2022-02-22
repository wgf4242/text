# pip install PyExecJS

import execjs
ctx = execjs.compile("""
       function add(x, y) {
               return x + y;
          }
""") # 获取代码编译完成后的对象
print(ctx.call("add", 1, 2)) # 3
# print(ctx.eval("add({0},{1})").format(1,2)) # 报错
print(ctx.eval('add("{0}", "{1}")').format("1","2")) # 12
