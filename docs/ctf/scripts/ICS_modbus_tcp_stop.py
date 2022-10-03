import socket
import time
import getopt
import sys
import struct
import os


if __name__ == "__main__":
    dstport = 502
    dstip ="192.168.180.146"
    addr = (dstip,dstport)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(addr)

    ##(Write coil)
    sendstr1="\x00\x00\x00\x00\x00\x06\x01\x05\x00\x03\x00\x00"
    sock.send(sendstr1)
    print sock.recv(1024000)



    sock.close()
