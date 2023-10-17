# https://zhuanlan.zhihu.com/p/140896045 网鼎杯-武为止戈

# import ida_bytes
from unicorn import *
from unicorn.arm_const import *
import sark
import idc

segs = list(sark.segments())
elf_base = segs[0].ea
elf_size = segs[-1].ea + segs[-1].size
elf_size = 0x1000 * ((elf_size + 0x0FFF) / 0x1000)
stack_size = 4 * 1024 * 1024
mem_size = 4 * 1024 * 1024
mem_ptr = elf_base + elf_size + stack_size
all_size = elf_size + stack_size + mem_size
stack_init = elf_base + elf_size + stack_size / 2
mu = Uc(UC_ARCH_ARM, UC_MODE_ARM)
mu.mem_map(elf_base, all_size)
print("Init Module: base:= {:06X} size:= {:04X}".format(elf_base, all_size))
for seg in segs:
    segdata = idc.get_bytes(seg.ea, seg.size)
    mu.mem_write(seg.ea, segdata)
    print("Init Seg: base:= {:06X} size:= {:04X}".format(seg.ea, seg.size))

mu.reg_write(UC_ARM_REG_SP, stack_init)
mu.reg_write(UC_ARM_REG_R4, 0x80002C8)
mu.emu_start(0x08000180 + 1, 0x800028C)
mu.mem_read(0x080002C8, 0x2c)
