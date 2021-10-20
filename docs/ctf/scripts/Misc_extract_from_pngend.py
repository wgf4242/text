from pathlib import Path

f = open('a.zip', 'wb')

for p in Path('.').glob('*.png'):
    print(p)
    rb = p.read_bytes()
    bend = [0x00, 0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, 0x44, 0xAE, 0x42, 0x60, 0x82]
    index = rb.find(bytearray(bend))
    rest = rb[index + len(bend):]
    f.write(rest)

f.close()
