import re
from collections import Counter

f = open('mmm', 'r', encoding='utf8')
a = ''
b = ''
for line in f.readlines():
    s = re.search(r"\{(.*)\}", line)
    res = s.groups()[0]
    a +=res
    b +=res.lower()
counter = Counter(a)
counterb = Counter(b)
print(counter)
print(counterb)
for k,num in counter.most_common():
    print(k, end='')
print()
for k,num in counterb.most_common():
    print(k, end='')

