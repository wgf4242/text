"""req.txt
POST /dashboard/add-service.php HTTP/1.1
Host: 127.0.0.1

------WebKitFormBoundarywcErkFBF0NAVjT1I
Content-Disposition: form-data; name="service_title"

1111111
------WebKitFormBoundarywcErkFBF0NAVjT1I
Content-Disposition: form-data; name="service_desc"

2222222
------WebKitFormBoundarywcErkFBF0NAVjT1I
"""
import json
import re
from copy import deepcopy

txt = open('req.txt', 'r', encoding='utf8').read()
txt = re.sub(
    '^(Content-Length|Origin|Accept-Encoding|Cache-Control|Accept|Sec-Fetch|sec-ch|Connection:|Referer:|User-Agent:|Upgrade-Insecure-Requests:).*\n',
    '', txt, flags=re.MULTILINE)
print(txt)


def do_normal(txt):
    lines = txt.splitlines()
    m = re.search('name="(.*)"', txt)
    key = m.group(1)
    value = ''.join(lines[3:])
    return {key: value}


def do_file(txt):
    print(txt)
    b'------WebKitFormBoundarywcErkFBF0NAVjT1I\nContent-Disposition: form-data; name="ufile"; filename="image.jpg"\nContent-Type: image/jpeg\n\n\xc3\xbf\xc3\x98\xc3\xbf\xc3\xa0\n'
    lines = txt.splitlines()
    name, filename = re.search('name="(.*)"; filename="(.*)"', txt).groups()
    ctype = re.search('Content-Type: (.*)', lines[2]).group(1)
    files = {name: [filename, 'filedata_or_fp', ctype]}
    return files


def extract_cookies(txt):
    import json
    m = re.search('Cookie: (.*)', txt)
    if m:
        cookie = m.group(1)
        cookie_key, cookie_value = re.search('(.*)=(.*)', cookie).groups()
        cookie_dict = {cookie_key: cookie_value}
        cookie_json = json.dumps(cookie_dict)

        txt_without_cookie = re.sub('Cookie: .*\n', '', txt)
        return txt_without_cookie, cookie_json
    else:
        txt_without_cookie = re.sub('Cookie: .*\n', '', txt)
        return txt_without_cookie, {}


form_datas = re.findall('^-----.*?(?=----)', txt, flags=re.DOTALL | re.MULTILINE)
print(len(form_datas))

data = {}
files = {}
for form_item in form_datas:
    if '; filename=' in form_item:
        files = do_file(form_item)
    else:
        info = do_normal(form_item)
        data.update(info)
if not form_datas:
    from urllib.parse import parse_qs

    form_datas = re.findall('\n\n(.*)', txt, flags=re.DOTALL | re.MULTILINE)
    if form_datas:
        data = parse_qs(form_datas[0])

# 上面是 req.txt , 从前2行提取出 url 地址
m = re.search('(?P<method>^[A-Z]+) (.*) HTTP/1.1\nHost: (.*)', txt)
method, path, host = m.groups()
method = method.lower()
txt, cookies = extract_cookies(txt)
url = 'http://' + host + path

print(url)

f = open('req.py', 'w', encoding='utf8')


def get_files1(files):
    import re
    files1 = deepcopy(files)
    if not files1:
        return {}
    keys = list(files1.keys())[0]
    files1[keys][1] = f"open('{files[keys][0]}', 'rb')"
    txt = json.dumps(files1)
    res = re.sub(r'"(open.*\))"', "\\1", txt)
    return res


files1 = get_files1(files)

f.write(f'''from requests_html import HTMLSession
session = HTMLSession()
url = '{url}'
data = {data}
files = {files}
# files = {files1}
cookies = {cookies}
# r = session.{method}(url, data=data, files=files, cookies=cookies)
r = session.{method}(url, data=data, files=files)
print(r.text)

''')
f.close()
