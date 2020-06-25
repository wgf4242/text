# wp
 
## 方法1 angr

```asm
.text:0000000000400842                 jnz     short loc_400855
.text:0000000000400844                 mov     edi, offset s   ; "Nice!"
.text:0000000000400849                 call    _puts
.text:000000000040084E                 mov     eax, 0
.text:0000000000400853                 jmp     short loc_40086B
.text:0000000000400855 ; ---------------------------------------------------------------------------
.text:0000000000400855
.text:0000000000400855 loc_400855:                             ; CODE XREF: main+5A↑j
.text:0000000000400855                 mov     edi, offset aIncorrectPassw ; "Incorrect password!"
.text:000000000040085A                 call    _puts
.text:000000000040085F                 mov     eax, 1
.text:0000000000400864                 jmp     short loc_40086B
```
```python
import angr
proj = angr.Project("./r100",auto_load_libs=False)
state = proj.factory.entry_state()
simgr = proj.factory.simgr(state) 
simgr.explore(find=0x400844,avoid=0x400855) # 0x400844 =>nice, 0x400855 错误跳转的位置
a = simgr.found[0].posix.dumps(0)
print(a) # 直接跑出答案
```

## 方法2 正常分析
```c
signed __int64 __fastcall sub_4006FD(__int64 a1)
{
  signed int i; // [rsp+14h] [rbp-24h]
  const char *v3; // [rsp+18h] [rbp-20h]
  const char *v4; // [rsp+20h] [rbp-18h]
  const char *v5; // [rsp+28h] [rbp-10h]

  v3 = "Dufhbmf";
  v4 = "pG`imos";
  v5 = "ewUglpt";
  for ( i = 0; i <= 11; ++i )
  {
    if ( (&v3)[i % 3][2 * (i / 3)] - *(char *)(i + a1) != 1 )
        // v3,v4,v5连着, (&v3)[i % 3] => 相当于看成一个数组, 循环取其中1个
        // a1传的是地址, *(char *)(i + a1) 相当于每次地址向前移动取值 = 取每个字符
      return 1LL;
  }
  return 0LL;
}
```
逆向

```python
v3 = "Dufhbmf"
v4 = "pG`imos"
v5 = "ewUglpt"
for i in range(12):
    ch = [v3,v4,v5][i % 3][2 * (i // 3)]
    k = ord(ch) - 1
    print(chr(k), end='')
```