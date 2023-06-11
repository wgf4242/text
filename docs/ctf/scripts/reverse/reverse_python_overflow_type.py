class Num:
    def __init__(self, n):
        self.n = (n % 256)

    def __repr__(self):
        return repr(self.n)

    def __add__(self, other):
        return Num(self.n + int(other))

    # transform ourselves into an int, so
    # int-expecting methods can use us
    def __int__(self):
        return self.n

def method2():
    import ctypes
    from ctypes import *
    ctypes.c_ubyte(255)
    print(c_ubyte(255))
    print(ctypes.c_ubyte(255 + 1))

def method3_signed_bytes():
    # signed types:
    ctypes.c_byte(127 + 1) # c_byte(-128)
    ctypes.c_byte(127 + 1).value # -128

a = Num(257) # 1
print(a+258) # 3
