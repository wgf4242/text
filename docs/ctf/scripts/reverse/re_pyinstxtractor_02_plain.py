"""
批量pyc转py,需要pycdc, struct.pyc
1. 解压出来的文件放到 pyc目录下
2. 当前目录放置 pycdc.exe
"""
import os
from pathlib import Path

prefix = open('pyc/struct.pyc', 'rb').read(8)

if not os.path.exists('pyc2'):
    os.mkdir('pyc2')
if not os.path.exists('out'):
    os.mkdir('out')

for f in Path('pyc').rglob('*'):
    read_bytes = bytearray(f.read_bytes())
    read_bytes[0:8] = prefix
    with open(f'pyc2/{f.name}', 'wb') as out:
        out.write(read_bytes)

for f in Path('pyc2').rglob('*'):
    rpath = f.as_posix()
    os.system(f'pycdc {rpath} > out/{f.stem}.py')
