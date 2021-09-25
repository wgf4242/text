from requests_html import AsyncHTMLSession

asession = AsyncHTMLSession()
url = 'http://1463-50e62051-2d46-4d20.nss.ctfer.vip:9080/shop?page={}'
find_str = 'lv6.png'
start, end = 0, 200


async def download(link, text):
    res = await asession.get(link)
    if text in res.text:
        print(link)


if __name__ == "__main__":
    lst = [url.format(i) for i in range(start, end)]
    funcs = [lambda x=x: download(x, find_str) for x in lst]
    asession.run(*funcs)
