# 羊城杯2021 misc520
# tshark -r flag.pcap -T fields -e usb.capdata > usbdata.txt 
nums = []
keys = open('usbdata.txt', 'r')
f = open('xy.txt', 'w')
posx = 0
posy = 0
for line in keys:
    if len(line) != 12:
        continue
    x = int(line[3:5], 16)
    y = int(line[6:8], 16)
    if x > 127:
        x -= 256
    if y > 127:
        y -= 256
    posx += x
    posy += y
    btn_flag = int(line[0:2], 16)  # 1 for left , 2 for right , 0 for nothing
    if btn_flag != 0:
        f.write(str(posx))
        f.write(' ')
        f.write(str(posy))
        f.write('\n')

f.close()
