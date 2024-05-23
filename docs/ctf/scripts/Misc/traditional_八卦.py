_hash = {"乾": "111", "兑": "011", "离": "101", "震": "001", "巽": "110", "坎": "010", "艮": "100", "坤": "000"}
text = "震坤艮 震艮震 坤巽坤 坤巽震 震巽兑 震艮震 震离艮 震离艮"
flag = [''.join(_hash[i] for i in word) for word in text.split()]

_flag = ''
for e in flag:
    _flag += ''.join(chr(int(e, 2)))
print("NSSCTF{" + _flag + "}")
