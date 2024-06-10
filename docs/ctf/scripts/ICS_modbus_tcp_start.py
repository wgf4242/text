"""
\xff 是置1, \x00 是置0
"""
import socket

if __name__ == "__main__":
    dstport = 502
    dstip = "192.168.80.136"
    addr = (dstip, dstport)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)

    ##(Write 1 coil)
    # sendstr1 = b"\x00\x00\x00\x00\x00\x06\x01\x05\x00\x00\xff\x00"
    maddr = b"\x00\x00"
    sendstr1 = b"\x00\x00\x00\x00\x00\x06\x01\x05%s\xff\x00" % maddr
    sock.send(sendstr1)

    ## write 0
    # sendstr1 = b"\x00\x00\x00\x00\x00\x06\x01\x05\x00\x00\x00\x00"
    # sock.send(sendstr1)
    print(sock.recv(1024000))

    sock.close()
