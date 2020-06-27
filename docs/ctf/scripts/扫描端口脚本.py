# 转成一句话脚本
# echo aW1wb3J0IHJlcXVlc3RzCmhvc3QgPSAnIGh0dHA6Ly8xMjcuMC4wLjEnCmZvciBpIGluIHJhbmdlKDIwMDAsMjUwMCk6CiAgICBhZGQgPSBob3N0Kyc6JytzdHIoaSkKICAgIHRyeToKICAgICAgICBzID0gcmVxdWVzdHMuZ2V0KGFkZCkKICAgICAgICBwcmludChpKQogICAgICAgIHByaW50KHMudGV4dCkKICAgICAgICBleGl0KDEpCiAgICBleGNlcHQ6CiAgICAgICAgcHJpbnQoaSkKICAgICAgICBwYXNzCg== | base64 -d | python3

import requests
host = ' http://127.0.0.1'
for i in range(2000,2500):
    add = host+':'+str(i)
    try:
        s = requests.get(add)
        print(i)
        print(s.text)
        exit(1)
    except:
        print(i)
        pass
