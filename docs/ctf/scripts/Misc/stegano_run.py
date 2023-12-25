import os
from pathlib import Path
key = ''
filename = 'mmm.jpg'
name,ext = filename.split('.')

p = Path(filename)
print(p.stem)
print(p.suffix)
print(dir(p))

if not key:
    print('试试题目名称')
if ext=='jpg':
    os.system(f'stegdetect -tjopi -s 10.0 ./a.jpg')
    os.system(f'steghide extract -sf test.jpg -p 123456')
    os.system(f'stegseek cvr.jpg wordlist.txt')
    os.system(f'jpseek {filename} %cd%/out.txt')
    ...
elif ext=='png':
    ...
elif ext=='bmp':
    ...