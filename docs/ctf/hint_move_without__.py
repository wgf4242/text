import shutil
from pathlib import Path

tmp = '../tmp_challenge'
depth = 2


def func(path, depth=1):
    ...


def init():
    Path(tmp).mkdir(exist_ok=True)
    Path(tmp + '/crypto').mkdir(exist_ok=True)
    Path(tmp + '/misc').mkdir(exist_ok=True)
    Path(tmp + '/pwn').mkdir(exist_ok=True)
    Path(tmp + '/reverse').mkdir(exist_ok=True)


def main(basedir, depth=1):
    for folder in Path(basedir).rglob('**/*'):
        if folder.name == '.idea':
            continue
        if not folder.is_dir():
            continue
        if depth == 1:
            main(folder, depth=depth + 1)
        if depth == 2:
            if folder.name.startswith('_'):
                continue
            parent = folder.parent
            # shutil copy override

            target = f'{tmp}/{parent.name}/{folder.name}'
            if Path(target).exists():
                shutil.rmtree(target)
            shutil.copytree(folder, target)


if __name__ == '__main__':
    init()
    main('.')
