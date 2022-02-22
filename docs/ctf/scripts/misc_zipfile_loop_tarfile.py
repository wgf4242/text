from pathlib import Path

i = 1
base_dir = Path('.').absolute()
folder = base_dir
while True:
    for f in Path(folder).rglob('*.tar.xz'):
        import tarfile
        my_tar = tarfile.open(f)
        folder = base_dir / f'{i}'
        my_tar.extractall(folder)  # specify which folder to extract to
        my_tar.close()
        i += 1
        break