import re

result = open('result.txt', 'r', encoding='utf8')
dic = {}
for line in result.read().splitlines():
    hash, _, data = line.split(':')
    dic[hash] = data
print(dic)

crc_file = open('crc32.txt', 'r', encoding='utf8')
res_hex = ''
for crc_dic in crc_file.read().splitlines():
    hash = crc_dic.split(':')[0]
    res_hex += dic[hash]

print(res_hex)
text = bytes.fromhex(res_hex).decode('utf-8')
print(text)
