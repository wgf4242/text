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
dis.dis(try_test)
# dis.dis(A)