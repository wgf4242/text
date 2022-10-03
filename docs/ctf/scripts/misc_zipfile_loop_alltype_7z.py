import os
import subprocess
from pathlib import Path

filename = '2'
i = 0
folder = ''
zip_type = ['bzip', '7-zip', 'gzip', 'POSIX tar', 'Zip archive', 'XZ compressed']

while filename:
    out = subprocess.getoutput(f'file {filename}')
    folder = f'{i}_extract'
    os.system(f'mkdir {folder} 2>/dev/null')
    if any(x in out for x in zip_type):
        os.system(f'7z x {filename} -o{folder}/')

    for file in Path(folder).rglob('*'):
        out = subprocess.getoutput(f'file {str(file)}')
        if any(x in out for x in zip_type):
            filename = str(file)
            break
    else:
        filename = ''
    i += 1
    if not filename:
        exit(0)
