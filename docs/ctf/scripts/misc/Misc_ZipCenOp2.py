"""
python Misc_ZipCenOp2.py compress_file.zip
"""
import os
import sys

if len(sys.argv) == 1:
    print('please input file name')
    exit()
file = sys.argv[1]
fr = open(file, 'rb').read()
fr = bytearray(fr)
print(fr[6])
fr[6] = 8
name,ext = file.split('.')
new_name = f'unzip_{name}.{ext}'
open(new_name, 'wb').write(fr)
os.system(f'7z -y x {new_name}')
