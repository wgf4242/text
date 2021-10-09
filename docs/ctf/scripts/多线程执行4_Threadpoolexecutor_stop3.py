import concurrent
from time import sleep

global_a = 1


def write():
    global global_a
    i = 0
    while True:
        i += 1
        sleep(1)
        global_a += 1
        print('i is ', i, 'a is ', global_a)
        if global_a > 3:
            executor.shutdownNow(wait=True)


def read():
    j = 0
    while True:
        print('j is ', j, '-- a=', global_a)
        sleep(1)
        j += 0
        if global_a > 3:
            executor.shutdownNow(wait=True)


from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=30) as executor:
    for _ in range(1):
        executor.submit(read)
        executor.submit(write)
