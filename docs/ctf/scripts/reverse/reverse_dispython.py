"""
python reverse_dispython.py
即可生成python的bytecode的指令序列
"""

import dis
import marshal
import sys
import types


def dis_code(code: types.CodeType, f):
    f.write(code.co_name)
    f.write('\n')
    dis.dis(code, file=f)


def main():
    file = sys.argv[1]
    with open(file, 'rb') as f:
        f.seek(16)
        asm = marshal.load(f)
        fp = open(file + '.asm', 'w', encoding='utf8')
        dis_code(asm, fp)


if __name__ == '__main__':
    main()