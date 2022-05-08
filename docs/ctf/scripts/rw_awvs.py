# -*- coding:utf-8 -*-
#! /usr/local/bin/

# author: m3lon

"""
help:将待检测的url写入url.txt即可
生成的报告在reports文件夹下
"""

import requests
import json
import urllib3
import os
import time
import threading

urllib3.disable_warnings()

task_urls = []
awvs_url = "https://192.168.66.208:3443"
apikey = "1986ad8c0a5b3df4d7028d5f3c06e936ce034d471e990439fa037f5dd3599f400"
headers = {"X-Auth": apikey, 'content-type':"application/json"}

def add_task(url=''):
    try:
        data = {"address": url, "description": "www.wugeek.com", "criticality": "10"}
        response = requests.post(awvs_url + "/api/v1/targets", data=json.dumps(data), headers=headers, timeout=30, verify=False)
        result = json.loads(response.content)
        print("[INFO]: Task is added successfully, target_id: "+ result['target_id'])
        return result['target_id']
    except Exception as e:
        print(str(e))
        return

# 开启扫描
def scan(url=''):

    '''
        11111111-1111-1111-1111-111111111112    High Risk Vulnerabilities
        11111111-1111-1111-1111-111111111115    Weak Passwords
        11111111-1111-1111-1111-111111111117    Crawl Only
        11111111-1111-1111-1111-111111111116    Cross-site Scripting Vulnerabilities
        11111111-1111-1111-1111-111111111113    SQL Injection Vulnerabilities
        11111111-1111-1111-1111-111111111118    quick_profile_2 0   {"wvs": {"profile": "continuous_quick"}}
        11111111-1111-1111-1111-111111111114    quick_profile_1 0   {"wvs": {"profile": "continuous_full"}}
        11111111-1111-1111-1111-111111111111    Full Scan   1   {"wvs": {"profile": "Default"}}
    '''

    # 先获取全部url，避免重复
    tasks = get_scan_urls()
    if url in tasks:
        print("[Repeat]: %s has been added!" % url)
        return

    target_id = add_task(url)
    profile_id = "11111111-1111-1111-1111-111111111111"
    data = {"target_id":target_id,"profile_id":profile_id,"schedule":{"disable":False,"start_date": None ,"time_sensitive": False}}
    try:
        response = requests.post(awvs_url + "/api/v1/scans",data=json.dumps(data), headers=headers, verify=False)
        scan_id = response.headers['Location'][14:]
        return scan_id

    except Exception as e:
        print(str(e))

# 生成报告，感觉比较鸡肋，报告的话还是直接在网上看比较方便吧
def generate_report(scan_id):

    scan_url = get_scan_url(scan_id)

    while True:
        if get_scan_status(scan_id) == "completed":
            data = {"template_id": "11111111-1111-1111-1111-111111111115",
                    "source": {"list_type": "scans", "id_list": [scan_id]}}
            response = requests.post(awvs_url + "/api/v1/reports", data=json.dumps(data), headers=headers, verify=False)
            report_url = awvs_url + response.headers['Location'].replace('/api/v1/reports/', '/reports/download/')
            report_url = report_url + ".pdf"

            # 卡了一晚上，在二狗不懈的努力下，终于发现问题所在：产生报告需要时间，延时处理
            while True:

                report = requests.get(str(report_url),
                                      headers={"X-Auth": apikey, "Accept": "*/*"},
                                      verify=False)

                if report.status_code == 404:
                    time.sleep(5)
                elif report.status_code == 200:
                    break

            if(not os.path.exists("reports")):
                os.mkdir("reports")

            file = "reports/" + scan_url[7:] + ".pdf"

            if(os.path.exists(file)):
                print("[INFO] %s.pdf has generated" % scan_url[7:])
                return

            with open(file, "wb") as f:
                f.write(report.content)
            f.close()

            print("[INFO] %s.pdf is generated successfully" % scan_url[7:])
            break
        else:
            print("[STATUS] %s is processing" % scan_url[7:])
            time.sleep(60)


# 获取所有扫描对应的urls
def get_scan_urls():
    response = requests.get(awvs_url+ "/api/v1/scans" , headers=headers, verify = False)
    result = json.loads(response.content)
    urls = []
    for item in result['scans']:
        urls.append(item['target']['address'])
    return urls

# 获取扫描scan_id对应的url
def get_scan_url(scan_id):
    try:
        response = requests.get(awvs_url + "/api/v1/scans/" + str(scan_id), headers=headers, verify=False)
        result = json.loads(response.content)
        return result['target']['address']
    except Exception as e:
        print(str(e))
        return

# 获取扫描urls对应的scan_ids
def get_scan_ids(urls):
    response = requests.get(awvs_url + "/api/v1/scans", headers=headers, verify=False)
    result = json.loads(response.content)
    scan_ids = []
    for item in result['scans']:
        if item['target']['address'] in urls:
            scan_ids.append(item['scan_id'])
    return scan_ids

# 获取scan_id的扫描状态
def get_scan_status(scan_id):
    try:
        response = requests.get(awvs_url + "/api/v1/scans/"+ str(scan_id), headers=headers, verify=False)
        result = json.loads(response.content)
        status = result['current_session']['status']
        return status
    except Exception as e:
        print(str(e))
        return

# url预处理
def handle_url(url):
    if not url.lower().startswith(("http:", "https:")):
        url = "http://" + url

    url = url.strip().rstrip('/')
    return url

if __name__ == '__main__':
    with open("url.txt", 'r') as f:

        # 如果url.txt为空 则调用help函数
        if not os.path.getsize("url.txt"):
            print("请将待检测的url(如 http://www.baidu.com)写入url.txt")
            exit()

        for line in f.readlines():
            url = handle_url(line)
            task_urls.append(url)

    task_urls = list(set(task_urls))
    scan_ids = []

    for url in task_urls:
        scan(url)

    scan_ids = get_scan_ids(task_urls)
    for scan_id in scan_ids:
        t = threading.Thread(target=generate_report, args=(scan_id,))
        t.start()