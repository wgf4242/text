import time, sys
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures.thread

data = {"future1": None, "future2": None, "future3": None}


def function1(n):
    time.sleep(1)
    data['future1'] = n
    print(n)


def function2(n):
    time.sleep(2)
    data['future2'] = n
    print(n)


def function3(n):
    time.sleep(3)
    data['future3'] = n
    print(n)


with ThreadPoolExecutor(max_workers=4) as executor:
    executor.submit(function1, 'test1')
    executor.submit(function2, 'test2')
    executor.submit(function3, 'test3')

    while True:
        if any(v is not None for v in data.values()):
            executor._threads.clear()
            concurrent.futures.thread._threads_queues.clear()
            break

print(data)
