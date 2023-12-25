# NCTF2023 jackpot
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/29/029 22:03
# @Author : H
# @File : getEmailHeader.py
 
import os
import re
from email.parser import Parser
 
 
def read_mail(path):
    if os.path.exists(path):
        with open(path) as fp:
            email = fp.read()
            return email
    else:
        print("file not exist!")
 
 
def emailInfo(emailpath):
    raw_email = read_mail(emailpath)  # 将邮件读到一个字符串里面
    print('emailpath : ', emailpath)
    emailcontent = Parser().parsestr(raw_email)  # 经过parsestr处理过后生成一个字典
    # for k,v in emailcontent.items():
    #     print(k,v)
    From = emailcontent['From']
    To = emailcontent['To']
    Subject = emailcontent['Subject']
    Date = emailcontent['Date']
    MessageID = emailcontent['Message-ID']
    XOriginatingIP = emailcontent['X-Originating-IP']
    if "<" in From:
        From = re.findall(".*<(.*)>.*", From)[0]
    if "<" in To:
        To = re.findall(".*<(.*)>.*", To)[0]
 
    print("From:\t", From)
    print("X-Originating-IP", XOriginatingIP)
    print("To:\t", To)
    print("Subject:\t", Subject)
    print("Message-ID:\t", MessageID)
    print("Date:\t", Date)
 
    # 循环信件中的每一个mime的数据块
    for par in emailcontent.walk():
        if not par.is_multipart():  # 这里要判断是否是multipart，是的话，里面的数据是无用的
            content = par.get_payload(decode=True)
            # print(str(content,"utf-8",errors='ignore'))
            print("content:\t", content.decode(encoding='gbk'))  # 解码出文本内容，直接输出来就可以了。
 
 
if __name__ == '__main__':
    email = "a.eml"
    emailInfo(email)
 
_str = 'str'
print(type(_str))
# 输出为 <class 'str'>
 
_bytes = b'bytes'
print(type(_bytes))
# 输出为<class 'bytes'>