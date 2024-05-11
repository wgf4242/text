# 羊城杯2021 misc520
# tshark -r atta.pcapng -Y "usb.src == "2.3.1" -T fields -e usb.capdata > usbdata.txt
# tshark -r atta.pcapng -T fields -e usbhid.data > usbdata.txt
"""
00ff0400     -- 4B 数据类型1
010004300000 -- 6B 数据类型2
"""
nums = []
keys = open('usbdata.txt').read().splitlines()
f = open('xy.txt', 'w')


def handler8(line):
    x = int(line[2:4], 16)
    y = int(line[4:6], 16)
    btn_flag = int(line[0:2], 16)  # 1 for left , 2 for right , 0 for nothing
    return x, y, btn_flag


def handler12(line):
    x = int(line[4:6], 16)
    y = int(line[6:8], 16)
    btn_flag = int(line[2:4], 16)  # 1 for left , 2 for right , 0 for nothing
    return x, y, btn_flag


def main():
    posx = 0
    posy = 0

    for line in keys:
        if len(line) == 8:
            x, y, btn_flag = handler8(line)
        elif len(line) == 12:
            x, y, btn_flag = handler12(line)
        else:
            continue

        if x > 127:
            x -= 256
        if y > 127:  # 这个参数控制单个字符的高度，如果高度过大导致字符过瘦，请调大
            y -= 256  # 这个参数控制字符串的倾斜程度，如果向下倾斜就调高，如果向上倾斜就调低

        posx += x
        posy += y
        if btn_flag ==1:
            f.write(f"{posx} {-posy}\n")

    f.close()


if __name__ == "__main__":
    main()
