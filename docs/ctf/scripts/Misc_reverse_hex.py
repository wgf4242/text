import sys
from pathlib import Path


def reverse_file(path):
    file = Path(path)
    f = open(file, 'rb').read()
    with open(f'{file.stem}_rev.{file.suffix}', 'wb') as fw:
        fw.write(f[::-1])


if __name__ == '__main__':
    path = sys.argv[1]
    reverse_file(path)
