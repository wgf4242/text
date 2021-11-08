# 字母rot13，数字rot5

# ROT5、13、18 解密

import string

# 引入string的定义字符串
ascii_lowercase = string.ascii_lowercase  # 小写字符串
ascii_uppercase = string.ascii_uppercase  # 大写字符串
digits = string.digits

# rot-18
# ROT18：这是一个异类，本来没有，它是将ROT5和ROT13组合在一起，为了好称呼，将其命名为ROT18。

# rot-5
# ROT5：只对数字进行编码，用当前数字往前数的第5个数字替换当前数字，例如当前为0，编码后变成5，当前为1，编码后变成6，以此类推顺序循环。
digits_dict = {}
for i in range(len(digits)):
    digits_dict[digits[i]] = digits[i - 5]

# rot-13
# ROT13：只对字母进行编码，用当前字母往前数的第13个字母替换当前字母，例如当前为A，编码后变成N，当前为B，编码后变成O，以此类推顺序循环。
lookup_dict = {}
# 大写字符串填充
for i in range(len(ascii_uppercase)):
    lookup_dict[ascii_uppercase[i]] = ascii_uppercase[i - 13]
# 小写字符串填充
for i in range(len(ascii_lowercase)):
    lookup_dict[ascii_lowercase[i]] = ascii_lowercase[i - 13]

# 判断输入是否为数字、字母  后转换
# 这里有一个很有意思的发现：中文被if判断为alpha


import string
# a = string.ascii_letters + string.digits
cipher = input("what's your cipher str：")
# cipher = a
clear = ''
for i in cipher:
    if i.isdigit():
        a_digit = digits_dict[i]
    elif i.isalpha():
        a_digit = lookup_dict[i]
    else:
        a_digit = i
    clear += a_digit

print(clear)
# print(a)

