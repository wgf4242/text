# _*_ utf-8 _*_d
# 接收端用 nc -l -p 1234 > out.file

from socket import socket, AF_INET, SOCK_STREAM

HOST = "192.168.50.119"
PORT = 1234
FILE = "result.txt"


def connect(HOST, PORT):
    ADDR = (HOST, PORT)
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, file):
    with open(file, "rb") as f:
        r = f.read()
        client.send(r)


def main():
    client = connect(HOST, PORT)
    send(client, FILE)
    client.close()
    print("接收完毕")


if __name__ == "__main__":
    main()
