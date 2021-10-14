import re

f = open('usbdata1.txt', 'r', encoding='utf8')
print(f)


# xxxxx 是匹配的占位符, index,  ascii码
pattern = re.escape(''',xxxxx,1))=xxxxx''')
pattern = pattern.replace('xxxxx', '{}').format('(\d+)', '(\w+)')
reobj = re.compile(pattern)
prev =  ''
prev_char = ''
while line := f.readline():
    r = re.search(reobj, line)
    index, char_hex = r.groups()
    char = chr(int(char_hex))
    if not prev:
        prev = index
        continue
    if index != prev:
        print(prev_char, end='')
    prev = index
    prev_char = char
print(prev_char)