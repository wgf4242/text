from concurrent.futures import ThreadPoolExecutor, wait
from stegpy import lsb
from itertools import product
import string

password = '512'
file = 'steg.png'



def download_pdf(i, password):
    print(i, password)
    host = lsb.HostElement(file)
    host.read_message(password)


with ThreadPoolExecutor(max_workers=200) as executor:
    futures = []
    # for password, title in zip(iter(txt), iter(txt2)):
    dic = string.digits
    for i, tp in enumerate(product(dic, repeat=3)):
        title = tp
        password = ''.join(tp)

        futures.append(executor.submit(download_pdf, i, password))
    # 等待所有任务完成
    wait(futures)
