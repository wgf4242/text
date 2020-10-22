# 从icmp获取长度转ascii
# 设置pychark
# D:\Python\Lib\site-packages\pyshark\config.ini
import pyshark
import base64

L_flag = []
packets = pyshark.FileCapture('fetus_pcap.pcap')
for packet in packets:
    for pkt in packet:
        if pkt.layer_name == "icmp":
            if int(pkt.type) != 0:
                L_flag.append(int(pkt.data_len))
c = len(L_flag)
for i in range(0, c):
    L_flag[i] = chr(L_flag[i])
print(''.join(L_flag))
print(base64.b64decode(''.join(L_flag)))
