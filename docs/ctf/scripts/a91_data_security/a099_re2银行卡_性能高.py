# https://mp.weixin.qq.com/s/6CfMK7KUbrGS17DzHpvP6A
"""
#phone_regex = r"(\+86\s?)?(\(\+86\)\s?)?((86)\s?)?((' + '|'.join(phone_prefixes) + r')\d{4}[\s-]?\d{4})"
phone_regex = r"((\+86\s)|(\(\+86\)\s?)|((86)\s?))((" + '|'.join(phone_prefixes) + r")\d{4}[\s-]?\d{4})"
email_regex = r"\b[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
"""
import os
import re2 as re
import time

start = time.perf_counter()

# 正则表达式
email_pattern = re.compile(r'\b(((([*+\-=?^_{|}~\w])|([*+\-=?^_{|}~\w][*+\-=?^_{|}~\.\w]{0,}[*+\-=?^_{|}~\w]))[@]\w+([-.]\w+)*\.[A-Za-z]{2,8}))\b')

'''
\b：表示单词边界，用于确保匹配的是完整的邮箱地址。
(：开始一个捕获组。
((([+-=?^_{|}~\w])|([+-=?^{|}~\w][*+-=?^{|}~.\w]{0,}[*+-=?^{|}~\w]))：表示邮箱地址的本地部分，可以是一个字母、数字或者特殊字符，也可以包含多个字母、数字、点号（.）或下划线（），但是必须以字母或数字结尾。
[@]：表示必须包含一个@符号。
\w+：表示@符号后面的域名部分，必须是一个或多个字母、数字或下划线。
([-.]\w+)*：表示域名中可能包含一个或多个连字符（-）或点号（.），后面跟着一个或多个字母、数字或下划线的字符串。
.[A-Za-z]{2,8}：表示域名的最后一部分，必须是一个点号后面跟着两个到八个字母的字符串，比如.com、.edu等等。
)：结束捕获组。
\b：单词边界。
'''

# 遍历指定文件夹下的所有txt文件
folder_path = 'folder/txt_files'
output_file = 'email.txt'

with open(output_file, 'w') as f:
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as txt_file:
                # 对txt文件中的每一行进行匹配
                for line in txt_file:
                    result = [m.group(0) for m in email_pattern.finditer(line)]
                    # 如果匹配到了银行卡号，将结果按照指定格式写入到txt文件中
                    if result:
                        for eamil in result:
                            f.write('{} {} {}\n'.format(file_name, 'email', eamil))
end = time.perf_counter()

spt = end - start

print('完成，用时{}秒'.format(spt))
