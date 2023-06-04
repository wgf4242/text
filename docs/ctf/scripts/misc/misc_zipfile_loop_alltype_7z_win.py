# win 使用方式
## 1.修改 filename
## 2.将filename压缩包放到 0_extract 文件夹


# 1. sagemath/bin里有file
# 2. 7z l filename 查找 Type =
import os
import subprocess
from pathlib import Path

i = 0
filename = 'Continue.zip'
folder = f'{i}_extract'


def setup():
    os.makedirs(folder, exist_ok=True)
    if not os.path.exists(f'{folder}/{filename}'):
        os.rename(filename, f'{folder}/{filename}')


def run():
    global filename, folder
    setup()

    while folder:
        has_zip = False
        for file in Path(folder).rglob('**/*'):
            out = subprocess.getoutput(f'7z l {str(file)}')
            if "Type = " in out:
                extract(file)
                # extract(file, password=file.stem)  # add password
                has_zip = True
                break
        if not has_zip:
            folder = ''


def extract(file: Path, password=None):
    global i, folder
    i += 1
    folder = f'{i}_extract'
    os.system(f'mkdir {folder} 2>nul')
    password = f'-p{password}' if password else ''
    os.system(f'7z -y x {str(file)} {password} -o{folder}/ > nul')


if __name__ == '__main__':
    run()
