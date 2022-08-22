import os

from bitstring import BitArray

if os.path.exists('final'):
    os.unlink('final')

file = """a.pcapng"""
os.system("""tshark -r %s -Y modbus -T fields -e modbus.data |sed '/^$/d' > out""" % file)
os.system("""tshark -r %s -Y modbus.request_frame -T fields -e modbus.data |sed '/^$/d'> out2""" % file)
os.system(r"""cat out2 | cut -d":" -f 2 | sed -z 's/\n//g' > result0""")
os.system(r"""xxd -r -ps result0 >> final""")

def solve2():
    lines = open('out', 'r').readlines()
    lst1 = []
    lst2 = []
    for line in lines:
        l = line.strip('\n').replace(':', '')
        lbytes = BitArray(bytes.fromhex(l))
        lst1.append(lbytes.bytes.decode('latin'))
        res = BitArray(bin=(lbytes.bin[::-1]))
        lst2.append(res.bytes[::-1].decode('latin'))

    f = open('final', 'a', encoding='latin')
    print(*lst1, sep='', file=f)
    print('----------------')
    print(*lst2, sep='', file=f)
    f.close()
# solve2()

os.system('cat final | more')