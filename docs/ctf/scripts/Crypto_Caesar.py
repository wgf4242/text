import string
import sys
import re

txt = """39 61 61 56 20 5C 61 54 1E 20 6B 61 67 20 65 61
5E 68 57 56 20 61 60 57 20 5F 61 64 57 20 55 5A
53 5E 5E 57 60 59 57 20 5B 60 20 6B 61 67 64 20
5C 61 67 64 60 57 6B 20 20 46 5A 5B 65 20 61 60
57 20 69 53 65 20 58 53 5B 64 5E 6B 20 57 53 65
6B 20 66 61 20 55 64 53 55 5D 20 20 49 53 65 60
19 66 20 5B 66 31 20 23 24 2A 20 5D 57 6B 65 20
5B 65 20 53 20 63 67 5B 66 57 20 65 5F 53 5E 5E
20 5D 57 6B 65 62 53 55 57 1E 20 65 61 20 5B 66
20 65 5A 61 67 5E 56 60 19 66 20 5A 53 68 57 20
66 53 5D 57 60 20 6B 61 67 20 66 61 61 20 5E 61
60 59 20 66 61 20 56 57 55 64 6B 62 66 20 66 5A
5B 65 20 5F 57 65 65 53 59 57 20 20 49 57 5E 5E
20 56 61 60 57 1E 20 6B 61 67 64 20 65 61 5E 67
66 5B 61 60 20 5B 65 20 64 54 62 55 65 56 62 55
56 5E 56 57 20"""
txt="""U8Y]:8KdJHTXRI>XU#?!K_ecJH]kJG*bRH7YJH7YSH]*=93dVZ3^S8*$:8"&:9U]RH;g=8Y!U92'=j*$KH]ZSj&[S#!gU#*dK9\."""
txt = txt.replace('\n', ' ').replace(' ', '')
if all(c in string.hexdigits for c in txt):
    lst = txt.replace('\n', ' ').split(' ')
    tochar = lambda x: chr(int(x, 16))
    str_lst = [tochar(txt[i:i+2]) for i in range(0, len(txt), 2)]
else:
    str_lst = txt
print(str_lst)


# print(lst)
# print([int(x, 16) for x in lst])


def offset(ch, i, force=False):
    if force:
        return chr((ord(ch) + i) % 128)

    if re.match(r'[a-z]', ch):
        return chr((ord(ch) - ord('a') + i) % 26 + ord('a'))
    elif re.match(r'[A-Z]', ch):
        return chr((ord(ch) - ord('A') + i) % 26 + ord('A'))

    return chr((ord(ch) + i) % 128)


def decrypt(txt=str_lst, force=False):
    print('---------检测前4位')
    lower = str_lst.lower()
    print([ord(x) - ord(lower[i]) for i, x in enumerate('flag')])
    print('---------检测前4位 done---')
    for i in range(128):
        g = [offset(x, i, force) for x in txt]
        print(''.join(g))
        print('------------')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        decrypt(sys.argv[1])
        decrypt(sys.argv[1], True)
    else:
        decrypt('FRPHEVGL')
        print('xxxxxxxxxxxxxxxxx----------xxxxxxxxxs')
        decrypt(force=True)
