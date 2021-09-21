import re

f = open('15.txt', 'r')
print(f)

pattern = re.escape('''(password,xxxxx,1))_from_user)="xxxxx"''')
pattern = pattern.replace('xxxxx', '{}').format('(\d+)', '(\w+)')
reobj = re.compile(pattern)
prev =  ''
prev_char = ''
while line := f.readline():
    r = re.search(reobj, line)
    index, char_hex = r.groups()
    char = chr(int(char_hex, 16))
    if not prev:
        prev = index
        continue
    if index != prev:
        print(prev_char, end='')
    prev = index
    prev_char = char
print(prev_char)