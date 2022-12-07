'''
copyright:elex

'''


import socket
import time
import getopt
import sys
import struct
import os

    
if __name__ == "__main__":    
    dstport = 102   
    dstip ="172.16.28.241"
    addr = (dstip,dstport)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(addr)


    #CR TPDU
    sock.send("\x03\x00\x00\x16\x11\xe0\x00\x00\x00\x01\x00\xc1\x02\x10\x00\xc2\x02\x03\x01\xc0\x01\x0a")
    sock.recv(1024)

    #DP TPDU
    sock.send("\x03\x00\x00\x19\x02\xf0\x80\x32\x01\x00\x00\xcc\xc1\x00\x08\x00\x00\xf0\x00\x00\x01\x00\x01\x03\xc0")
    sock.recv(1024)



    ##m0.0 to1
    sendstart = "\x03\x00\x00\x24\x02\xf0\x80\x32\x01\x00\x00\x00\x03\x00\x0e\x00\x05\x05\x01\x12\x0a\x10\x02\x00\x01\x00\x00\x83\x00\x00\x00\x00\x04\x00\x08\x01"
    sock.send(sendstart)
    print sock.recv(1024)

    ##m0.0 to0
    sendstart = "\x03\x00\x00\x24\x02\xf0\x80\x32\x01\x00\x00\x00\x04\x00\x0e\x00\x05\x05\x01\x12\x0a\x10\x02\x00\x01\x00\x00\x83\x00\x00\x00\x00\x04\x00\x08\x04"
    sock.send(sendstart)
    print sock.recv(1024)



    sock.close()       

            