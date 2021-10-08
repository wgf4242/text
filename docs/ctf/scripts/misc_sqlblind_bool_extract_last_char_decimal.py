import re

f = open('123', 'r')
print(f)

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