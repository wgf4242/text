import os

from bitstring import BitArray

file = """a.pcapng"""
os.system("""tshark -r %s -Y modbus -T fields -e modbus.data |sed '/^$/d' > out""" % file)

lines = open('out', 'r').readlines()
for line in lines:
    l = line.strip('\n').replace(':', '')
    lbytes = BitArray(bytes.fromhex(l))
    print(lbytes.bytes)
    res = BitArray(bin=(lbytes.bin[::-1]))
    print(res.bytes[::-1])
