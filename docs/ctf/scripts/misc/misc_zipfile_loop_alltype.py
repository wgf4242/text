# 用win下 7z写更好 全部都能解
import os
import subprocess
from pathlib import Path

filename = '2'
out = ''
i = 0
folder = ''


def getfile(folder):
    global filename, out
    for file in Path(folder).rglob('*'):
        out = subprocess.getoutput(f'file {str(file)}')
        if any(x in out for x in ['bzip', '7-zip', 'gzip', 'POSIX tar', 'Zip archive', 'XZ compressed']):
            filename = str(file)
            return
        else:
            filename = ''


def check():
    global i, folder
    out = subprocess.getoutput(f'file {filename}')
    folder = f'{i}_extract'
    os.system(f'mkdir {folder} 2>/dev/null')
    if 'bzip2' in out:
        print(f'tar -jxvf {filename} -C {folder}/')
        os.system(f'tar -jxvf {filename} -C {folder}/')
    elif '7-zip' in out:
        print(f'7z x {filename} -o{folder}/')
        os.system(f'7z x {filename} -o{folder}/')
    elif 'gzip' in out:
        print(f'tar zxvf {filename} -C {folder}/')
        os.system(f'tar zxvf {filename} -C {folder}/')
    elif 'POSIX tar' in out:
        print(f'tar xvf {filename} -C {folder}/')
        os.system(f'tar xvf {filename} -C {folder}/')
    elif 'Zip archive' in out:
        print(f'unzip {filename} -d {folder}/')
        os.system(f'unzip {filename} -d {folder}/')
    elif 'XZ compressed' in out:
        print(f'tar -xf {filename} -C {folder}/')
        os.system(f'tar -xf {filename} -C {folder}/')
    getfile(folder)
    i += 1
    if not filename:
        exit(0)


if __name__ == '__main__':
    while filename:
        check()
