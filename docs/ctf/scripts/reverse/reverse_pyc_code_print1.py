# 生成pyc python -m py_compile main.py
import dis, marshal, sys


def print_code(filename):
    import marshal
    f = open(filename, 'rb')
    print(f)
    code = marshal.loads(f.read()[16:])
    print(dis.dis(code))

def test_bytecode():
    import dis
    def f(x):print('hello',x)

    print(type(f.__code__)) # <class 'code'>
    f.__code__.co_code
    b't\x00d\x01|\x00\x83\x02\x01\x00d\x00S\x00'
    dis.dis(f)

def compile_pyc(filename)
    import py_compile
    py_compile.compile(filename)

print_code(r'ezPYC.pyc')
