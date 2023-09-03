"""
tshark filter: form urlencode, value
"""
# tshark -r hard_web.pcap -Y "http.request.method == ""POST""" -T json -e urlencoded-form.key -e urlencoded-form.value -x > 12.json
from jsonpath_ng import jsonpath, parse
import json
from itertools import chain

jsonpath_expr = parse('$..layers[*]')
data = json.load(open('12.json', 'r', encoding='latin'))
arr = [match.value for match in (jsonpath_expr.find(data))]

res = list(chain.from_iterable(item.values() for item in arr))
res1 = list(filter(lambda x: x, chain.from_iterable(res)))


def gzip_decode(data):
    import zlib
    return zlib.decompress(data, 16 + zlib.MAX_WBITS)

def aes_ecb(key, passwd):
    from Crypto.Cipher import AES
    aes = AES.new(key, AES.MODE_ECB)

    try:
        aes_decoded_data = aes.decrypt(passwd).strip(b'\x00')
        gzip_decode_data = gzip_decode(aes_decoded_data)
        print(gzip_decode_data)
    except Exception as e:
        print('error ')


if __name__ == '__main__':
    key = b'748007e861908c03'
    for data in res1:
        aes_ecb(key, data.encode('latin'))
