# Crypto_rar_defake.py filename.rar
import sys,os
from pathlib import Path

fname = Path(sys.argv[1])
data = open(fname, 'rb').read()
dnew = data[:0x17] + b'\x80' + data[0x18:]
with open(f'dec_{fname.name}', 'wb') as f:
	f.write(dnew)
