import socket
import time

if __name__ == "__main__":
    dstport = 102
    dstip = "192.168.80.133"
    addr = (dstip, dstport)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    time.sleep(0.1)
    cotp = bytes.fromhex('0300001611e00000000100c0010ac1020100c2020101')
    sock.send(cotp)
    setup_communication = bytes.fromhex('0300001902f08032010000040000080000f0000001000101e0')
    sock.send(setup_communication)
    time.sleep(0.1)

    var_set_1 = bytes.fromhex('0300002402f08032010000005f000e00050501120a100100010000830000000003000101')
    var_set_0 = bytes.fromhex('0300002402f080320100000060000e00050501120a100100010000830000000003000100')
    # sock.send(var_set_1)
    sock.send(var_set_0)
    sock.close()
