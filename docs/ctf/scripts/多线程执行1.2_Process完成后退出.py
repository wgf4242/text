import sys
from binascii import unhexlify
import time
import multiprocessing


# 开始遍历
# 我的CPU是8个逻辑核，所以开8个进程，每个进程分配到18750000个。
def go(start, end, event: multiprocessing.Event() ):
    enc = 'c3abf969fc605facb1811e597b3de703164b3b81f34ccaa284a68eb06b8493c6'
    skr = 'd03bd6d9fe'
    skr = unhexlify(skr)
    import hashlib

    for c1 in range(start, end):
        for c2 in range(256):
            for c3 in range(256):
                k = bytes([c1, c2, c3])
                code = skr + k
                if hashlib.sha256(code).hexdigest() == enc:
                    print(code.hex())
                    event.set()


if __name__ == '__main__':
    print(time.asctime())

    jobs = []
    #Create Event
    event = multiprocessing.Event()
    for i in range(0, 256, 8):
        p = multiprocessing.Process(target=go, args=(i, i + 8, event))
        p.start()

    while True:
        if event.is_set():
            print("Exiting all child processess..")
            for i in jobs:
                #Terminate each process
                i.terminate()
            #Terminating main process
            sys.exit(1)
        time.sleep(2)