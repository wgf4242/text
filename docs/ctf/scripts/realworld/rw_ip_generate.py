import re

txt = """10.63.104.21-250
10.64.17.129-255
"""

tmp = []
lst = []

def rep(m):
    print(m)
    group = m.group()
    match = m.groups()[0]

    a, b = match.split('-')
    for i in range(int(a), int(b) + 1):
        res1 = group.replace(match, str(i))
        lst.append(res1)
    return '1'


def split(line):
    re.sub(r'.*?(\d+-\d+).*', rep, line)
    return lst


result = []
for line in txt.splitlines():
    tmp = []
    res = []
    if '-' in line:
        res = split(line)
    result.extend(res)

with open('res.txt', 'w') as f:
    # for ip in result:
    f.writelines('\n' + line for line in result)
