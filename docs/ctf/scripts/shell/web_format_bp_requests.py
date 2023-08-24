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
import re

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
    cookie = re.search('Cookie: (.*)', txt).group(1)

    cookie_key, cookie_value = re.search('(.*)=(.*)', cookie).groups()
    cookie_dict = {cookie_key: cookie_value}
    cookie_json = json.dumps(cookie_dict)

    txt_without_cookie = re.sub('Cookie: .*\n', '', txt)
    return txt_without_cookie, cookie_json


arr = re.findall('^-----.*?(?=----)', txt, flags=re.DOTALL | re.MULTILINE)
print(len(arr))

data = {}
files = {}
for formitem in arr:
    if '; filename=' in formitem:
        files = do_file(formitem)
    else:
        info = do_normal(formitem)
        data.update(info)

# 上面是 req.txt , 从前2行提取出 url 地址
m = re.search('(?P<method>^[A-Z]+) (.*) HTTP/1.1\nHost: (.*)', txt)
method, path, host = m.groups()
method = method.lower()
txt, cookies = extract_cookies(txt)
url = 'http://' + host + path

print(url)

f = open('req.py', 'w', encoding='utf8')
f.write(f'''from requests_html import HTMLSession
session = HTMLSession()
url = '{url}'
data = {data}
files = {files}
cookies = {cookies}
# r = session.{method}(url, data=data, files=files, cookies=cookies)
r = session.{method}(url, data=data, files=files)
print(r.text)

''')
f.close()
