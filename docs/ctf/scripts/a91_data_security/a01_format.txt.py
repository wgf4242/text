from pathlib import Path
import re

out = Path('./out')
if not out.exists():
    out.mkdir()

for file in Path('./result').rglob('*'):
    print(file)
    lines = open(file, 'r', encoding='utf8').read().splitlines()

    fw = open(r'out/' + file.name, 'w')
    for line in lines:
        s = re.sub(r'.*\((\d+)\): ', rf'\1,{file.stem},', line)
        print(s)
        fw.write(s + '\n')
        # print(line)
    # exit()
