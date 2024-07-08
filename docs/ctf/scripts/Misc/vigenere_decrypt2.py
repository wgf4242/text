"""
维吉尼亚密码，密码表换成了小写字母+{}，通过固定的flag头 ayyctf 爆破密钥，再解密。
"""
import random
import string

dicts = string.ascii_lowercase + "{}"
# print(dicts)

key = (''.join([random.choice(dicts) for i in range(4)])) * 8
enc = 'tsejk}gbxyiutfchpm}ylm}a}amuxlmg'
known = 'ayyctf{'

# print(len(enc))
key = ''
for i in range(4):
    key += dicts[(ord(enc[i]) - ord(known[i])) % 28]
# print(key)

key = key * 8

import string

# 初始化空字典
index_dict = {}

# 使用循环将 a-z 对应到 0-25
for i, letter in enumerate(string.ascii_lowercase):
    index_dict[letter] = i

# 将 '{' 对应到 26，将 '}' 对应到 27
index_dict['{'] = 26
index_dict['}'] = 27

# print(index_dict)

flag = ''
for i in range(len(enc)):
    flag += dicts[(index_dict.get(enc[i]) - index_dict.get(key[i])) % 28]

print(flag)
