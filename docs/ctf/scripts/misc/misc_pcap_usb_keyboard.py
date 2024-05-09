"""
18长度的
020800150000000000
16长度 - 缺ID
  0800150000000000

<DEL>删除前一个输入
"""
import os

# os.system("tshark -r 1.pcapng -Y 'usb.src == 2.3.1' -T fields -e usbhid.data > usbdata.txt")
# os.system("tshark -r 1.pcapng -T fields -e usb.capdata > usbdata.txt")

normalKeys = {"04": "a", "05": "b", "06": "c", "07": "d", "08": "e", "09": "f", "0a": "g", "0b": "h", "0c": "i", "0d": "j", "0e": "k", "0f": "l", "10": "m", "11": "n", "12": "o",
              "13": "p", "14": "q", "15": "r", "16": "s", "17": "t", "18": "u", "19": "v", "1a": "w", "1b": "x", "1c": "y", "1d": "z", "1e": "1", "1f": "2", "20": "3", "21": "4",
              "22": "5", "23": "6", "24": "7", "25": "8", "26": "9", "27": "0", "28": "<RET>", "29": "<ESC>", "2a": "<DEL>", "2b": "\t", "2c": "<SPACE>", "2d": "-", "2e": "=",
              "2f": "[", "30": "]", "31": "\\", "32": "<NON>", "33": ";", "34": "'", "35": "<GA>", "36": ",", "37": ".", "38": "/", "39": "<CAP>", "3a": "<F1>", "3b": "<F2>",
              "3c": "<F3>", "3d": "<F4>", "3e": "<F5>", "3f": "<F6>", "40": "<F7>", "41": "<F8>", "42": "<F9>", "43": "<F10>", "44": "<F11>", "45": "<F12>"}
shiftKeys = {"04": "A", "05": "B", "06": "C", "07": "D", "08": "E", "09": "F", "0a": "G", "0b": "H", "0c": "I", "0d": "J", "0e": "K", "0f": "L", "10": "M", "11": "N", "12": "O",
             "13": "P", "14": "Q", "15": "R", "16": "S", "17": "T", "18": "U", "19": "V", "1a": "W", "1b": "X", "1c": "Y", "1d": "Z", "1e": "!", "1f": "@", "20": "#", "21": "$",
             "22": "%", "23": "^", "24": "&", "25": "*", "26": "(", "27": ")", "28": "<RET>", "29": "<ESC>", "2a": "<DEL>", "2b": "\t", "2c": "<SPACE>", "2d": "_", "2e": "+",
             "2f": "{", "30": "}", "31": "|", "32": "<NON>", "33": ":", "34": "\"", "35": "<GA>", "36": "<", "37": ">", "38": "?", "39": "<CAP>", "3a": "<F1>", "3b": "<F2>",
             "3c": "<F3>", "3d": "<F4>", "3e": "<F5>", "3f": "<F6>", "40": "<F7>", "41": "<F8>", "42": "<F9>", "43": "<F10>", "44": "<F11>", "45": "<F12>"}
modkeys = {"00": "", "08": "<Win>"}
nums = []
keys = open('usbdata.txt').read().splitlines()
for line in keys:
    # print(line)
    # if len(line)!=17: #首先过滤掉鼠标等其他设备的USB流量
    #      continue
    if len(set(line)) == 1:
        continue
    elif len(line) == 16:
        line = "00" + line
    elif len(line) != 18:
        raise Exception("Length error, should be 16 or 18")
    nums.append(line[2:4] + line[6:8])  # 提取:修饰键 按键
    # print(nums)

output = ""
for n in nums:
    # if n[2:4] == "00":
    #     continue

    if n[2:4] in normalKeys:
        if n[0:2] == "02":  # 表示按下了shift
            output += shiftKeys[n[2:4]]
        else:
            output += modkeys.get(n[0:2], '')
            output += normalKeys[n[2:4]]
    else:
        output += '[unknown]'
print('output :' + output)
