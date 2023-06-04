"""
txt format like:
0xffff97609614a770                    278324 /snap/home/john-doe/.mozilla/firefox/profiles.ini
"""
import os
from pathlib import Path
import re

lines = open('firefox.txt', 'r').read().splitlines()
file = r"..\mem.vmem"
profile = "LinuxUbuntu18_04_6LTS_5_4_0-42-generic_profilex64"

lst = []
exclude = []


def format():
    for group in lines:
        a = re.search('(.*?)\s+\d+ (.+)', group)
        node, path = a.groups()
        lst.append([node, path])

        p = Path(path)
        parent = str(p.parent.as_posix())
        exclude.append(parent)

    tmp = list(filter(lambda x: x[1] not in exclude, lst))
    return tmp


def extract(lst):
    for node, path in lst:
        p = Path(path)
        if not p.parent.exists():
            os.system(f'md {p.parent}')
        os.system(rf'D:\Python27\python.exe vol.py -f {file} --profile={profile} linux_find_file -i {node} -O {p.absolute()}')
        if p.exists() and not p.is_dir() and all(x == 0 for x in p.read_bytes()):
            p.unlink()
            p.mkdir()
        print(node, str(p))


if __name__ == "__main__":
    arr = format()
    extract(arr)
