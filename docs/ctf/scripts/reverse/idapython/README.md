

# GetValue

```py
idaapi.get_bytes(0x7FF70627FB00, 8)
idaapi.get_64bit(addr)
```

# String

```py
idaapi.get_bytes(here(),10).decode('utf-8')
idaapi.get_strlit_contents(idc.here(), -1, idaapi.STRTYPE_C) # b'GetModuleHandleW'
```