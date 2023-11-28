"""
FOR_ITER 40 (to 50): 迭代循环的开始，当迭代完成之后将字节码的 counter 加上 40 ，也就是跳转到 50 的位置执行。跳出循环
"""
import marshal,dis
class A():
    def foo():
        self.x = 1

def func():
    a = 10
    b = 20
    c = a + b
    return c

def try_test():
    try:
        a = 1
    except Exception:
        b = 2
    finally:
        c = 3
# dis.dis(func)
# dis.dis(try_test)
# dis.dis(A)

code_to_inspect = """  
a, b = b, a  
"""  
  
dis.dis(code_to_inspect)  
