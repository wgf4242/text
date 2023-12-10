import collections

import wordninja

f = open('txt', 'r', encoding='utf8')
txt = f.read().replace('cryptosystem', 'crypto system')

lst = wordninja.split(txt)

counter1 = collections.Counter(lst)
print(counter1)
for i, (word, count) in enumerate(counter1.most_common()[::-1]):
    print(f"{word:20}: {count:5}, {i + 1}")
