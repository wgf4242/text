import concurrent
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def process(duration):
    print(f"processing with duration {duration}")
    time.sleep(duration)
    if duration == 3:
        return "result found"
    print(f"processing with duration {duration} end")


j = 1
while True:
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process, i) for i in range(80000)]
        for future in as_completed(futures):
            if future.result() == "result found":
                # executor.shutdown(wait=False)
                print("shutdown")
                for f in futures:  # 如果不cancel 会留下一个 i没清除变大
                    if not f.done():
                        f.cancel()
                executor._threads.clear()
                concurrent.futures.thread._threads_queues.clear()
                break
    j += 1
    print("about to exit")
    if j > 3:
        break
