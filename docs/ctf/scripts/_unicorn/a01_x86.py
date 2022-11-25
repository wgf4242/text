from __future__ import print_function
from unicorn import *
from unicorn.x86_const import *

# 要模拟执行的指令
X86_CODE32 = b"\x41\x4a" # INC ecx; DEC edx

# 模拟执行的起始地址
ADDRESS = 0x1000000

print("Emulate i386 code")
try:
    # 初始化模拟X86-32模式
    mu = Uc(UC_ARCH_X86, UC_MODE_32)

    # 为模拟执行申请2MB的空间
    mu.mem_map(ADDRESS, 2 * 1024 * 1024)

    # 向内存写入执行的指令
    mu.mem_write(ADDRESS, X86_CODE32)

    # 初始化寄存器的值，方便执行后观察结果
    mu.reg_write(UC_X86_REG_ECX, 0x1234)
    mu.reg_write(UC_X86_REG_EDX, 0x7890)

    # 在无限时间和无限指令中模拟代码
    mu.emu_start(ADDRESS, ADDRESS + len(X86_CODE32))

    # 现在打印执行后寄存器中的结果
    print("Emulation done. Below is the CPU context")

    r_ecx = mu.reg_read(UC_X86_REG_ECX)
    r_edx = mu.reg_read(UC_X86_REG_EDX)
    print(">>> ECX = 0x%x" %r_ecx)
    print(">>> EDX = 0x%x" %r_edx)

except UcError as e:
    print("ERROR: %s" % e)