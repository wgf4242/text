import base64

import pyshark
import re

post_map = {}
i = 0


def antsword():
    try:
        captures = pyshark.FileCapture("cms.pcap"
                                       , tshark_path=r'D:\Program Files\Wireshark\tshark.exe'
                                       , display_filter="http")
        for packet in captures:

            try:
                length = int(packet.length)
                number = int(packet.number)
                stream = int(packet.tcp.stream)

                if length > 5000:
                    print(f"{number=}, {length=} is File ---")
                    continue

                if 'URLENCODED-FORM' in packet and packet.http.request_method == 'POST':
                    post_map[stream] = 1
                    get_form_data(number, packet)

                if hasattr(packet.http, 'response') and post_map[stream]:
                    if (re.search(r"\.(js|css|html)", packet.http.response_for_uri) or
                            "charset=utf-8" in packet.http.content_type):
                        continue
                    data = get_http_file_data(packet).decode()
                    print(f'{number=}')
                    print(data)
            except:
                pass

            # form item 删除前2位
    except Exception as e:
        print(e)


def get_form_data(number, packet):
    global i
    form = packet['URLENCODED-FORM']
    value = form.value
    raw_http = get_http_file_data(packet)
    match = re.findall(r'\$_POST\["(.*?)"\]', value)
    pwd, *rest = match
    from urllib.parse import unquote
    http = unquote(raw_http)
    http_lst = http.split('&')
    form_obj = {x.split('=', 1)[0]: x.split('=', 1)[1] for x in http_lst}
    data_payload = base64.b64decode(form_obj[pwd][2:])
    print(f"{number=}, {data_payload=}")
    rest_bin_hex = form_obj[rest[0]]
    if len(rest_bin_hex) > 5000:
        f = open(f'bin{i}', 'wb')
        f.write(bytes.fromhex(rest_bin_hex))
        f.close()
        print(f'bin{i} saved')
        i += 1
    else:
        print(bytes.fromhex(rest_bin_hex).decode())


def get_http_file_data(packet):
    raw_http = bytes.fromhex(packet.http.file_data.replace(':', ''))
    return raw_http


antsword()
