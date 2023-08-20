[link](https://www.cnblogs.com/Sentry-Prisoner/p/15177819.html)

| syscall_adr     | 0x68-0x6f |                                   |
|-----------------|-----------|-----------------------------------|
| binsh_addr      | 0x60-0x67 |
| pop_rdi_addr    | 0x58-0x5f |
| sys_execve_addr | 0x50-0x57 |
| mov_rdx_addr    | 0x48-0x4f |
| 0               | 0x40-0x47 |
| 0               | 0x38-0x3f |
| 0               | 0x30-0x37 |
| binsh_addr+0x50 | 0x28-0x2f | 0x4004E2 mov rax, 3Bh; ret 主要是ret |
| 0               | 0x20-0027 |
| 0               | 0x18-0x1f |
| pop_addr        | 0x10-0x17 |
| /bin/sh         | 0x8-0xf   |
| /bin/sh         | 0-0x7     |