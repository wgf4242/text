# 冰蝎 帆软反序列化 流量解析工具
import base64
import json
import re

import pyshark

file = "result.pcap"
key = "e45e329feb5d925b"
post_map = {}
i = 0


def is_json_valid(data):
    try:
        json.loads(data)
        return True
    except:
        return False


def behinder4(file="cms.pcap"):
    try:
        captures = pyshark.FileCapture(file
                                       , tshark_path=r'D:\Program Files\Wireshark\tshark.exe'
                                       , display_filter="http")
        for packet in captures:

            try:
                length = int(packet.length)
                number = int(packet.number)
                stream = int(packet.tcp.stream)

                if length > 5000:
                    print(f"{number=}, {length=} is File ---")
                    # continue

                # if 'URLENCODED-FORM' in packet and packet.http.request_method == 'POST':
                # if hasattr(packet.http, 'request_uri') and packet.http.request_method == 'POST':
                if hasattr(packet.http, 'request_method') and packet.http.request_method == 'POST' \
                        and hasattr(packet.http, 'request_uri') and packet.http.request_uri == '/webroot/login':
                    post_map[stream] = 1
                    get_form_data(number, packet)

                if hasattr(packet.http, 'response') and post_map[stream]:
                    # if (re.search(r"\.(js|css|html)", packet.http.response_for_uri) or
                    #         "charset=utf-8" in packet.http.content_type):
                    #     continue
                    # data = get_http_file_data(packet).decode()
                    print(f'{number=}')
                    decode_beinder_data(packet)
            except:
                pass

            # form item 删除前2位
    except Exception as e:
        print(e)


def aes_decrypt(data, key):
    from Crypto.Cipher import AES
    if isinstance(key, str):
        key = key.encode()

    aes = AES.new(key, AES.MODE_ECB)
    result = aes.decrypt(data)
    # print(result)
    return result


def clean(txt):
    txt = re.sub(r'[\x00-\x10]+$', '', txt)
    return txt


def deep_parse(obj):
    if isinstance(obj, str) and is_json_valid(obj):
        item1 = json.loads(obj)
        return deep_parse(item1)
    elif isinstance(obj, list):
        lst = []
        for item in obj:  # type:dict
            # item = obj[0]
            new_item = {}
            for k, v in item.items():
                value = base64.b64decode(v).decode()
                parse = deep_parse(value)
                # print(f"{key=}, {parse=}")
                new_item[k] = parse
            lst.append(new_item)
        return lst
    elif isinstance(obj, dict):
        new_item = {}
        for k, v in obj.items():
            value = base64.b64decode(v).decode()
            new_item[k] = deep_parse(value)
        return new_item
    else:
        return obj
    return obj


def decode_beinder_data(packet):
    b64data = bytes.fromhex(packet.http.data)
    data = base64.b64decode(b64data)
    result = aes_decrypt(data, key)
    res = result.decode()
    res = clean(res)
    obj = json.loads(res)

    res = deep_parse(obj)
    print(res)


def get_form_data(number, packet):
    global i
    return


def get_http_file_data(packet):
    raw_http = bytes.fromhex(packet.http.file_data.replace(':', ''))
    return raw_http


behinder4(file)
