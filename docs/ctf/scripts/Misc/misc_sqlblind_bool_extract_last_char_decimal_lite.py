"""c.txt 要干净些
tshark -r ctf.pcapng -Y " (urlencoded-form.key == ""u"") && (frame.number > 18709)" -T fields -e urlencoded-form.value > c.txt

u=1234'+and+if(ascii(substr((select+group_concat(hint)+from+hacker),1,1))=101,sleep(3),1)+and+'&p=123
u=1234'+and+if(ascii(substr((select+group_concat(hint)+from+hacker),1,1))=102,sleep(3),1)+and+'&p=123
"""
import re

f = open('b.txt', 'r', encoding='utf8').read()
print(f)

p = r',(\d+),1\)\)=(\d+),.*(?=\n.*?from.\w+\),(?!\1,\d\)\)))'
res = re.findall(p, f)
print(''.join(chr(int(val)) for i, val in res))
print('最后一行要手动提取')
