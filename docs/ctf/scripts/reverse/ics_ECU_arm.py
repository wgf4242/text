# 网鼎杯-武为止戈 汽车通讯协议、汽车ECU、ARM
# 汽车-ECU_Upgrade
# Arm v6 32bit little Endian
# Base Address 08000000
with open('./can_log.asc', 'r') as f:
    fr = f.read().split('\n')
data = []
for fi in fr:
    fi = fi.split(' ')
    if len(fi) == 42:
        data += [(fi[6], fi[24], ''.join(fi[25: 32]))]
    if len(fi) == 41:
        data += [(fi[5], fi[23], ''.join(fi[24: 31]))]

res = []
tmp = ''
for d in data:
    id, tp, data = d
    if id == '7B0':     # ack
        continue
    elif tp[0] == '0':    # signal
        continue
    elif tp == '10':    # first
        res += [tmp]
        tmp = data[4:]
    elif tp[0] == '2':
        tmp += data
    else:
        print('???')
        print(tp, data)

test = ''
for r in res[3:]:
    print(r, len(r))
    test += r[2:-4]
print(test)
with open('./out.bin', 'wb') as f:
    f.write(bytes.fromhex(test))

# https://zhuanlan.zhihu.com/p/140896045

# flag{3dad13db-cb48-495d-b023-3231d80f1713}
