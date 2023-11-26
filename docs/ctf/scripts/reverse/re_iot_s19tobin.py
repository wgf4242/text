import re
print('32bit s19 to bin, 16位的要手动修改一下')

f = open('firmware.s19', 'r', encoding='utf8')
binfile = open('file.bin', 'wb')

frame_packets = f.read().splitlines()
last_line = frame_packets.pop()
size_line = frame_packets.pop()
for line in frame_packets:
    # 32bit start with S3,
    pattern = r"(?P<frame>..)(?P<frame_size>..)(?P<addr>.{8})(?P<data>.+)(?P<checksum>..)"
    matches = re.search(pattern, line)
    matches.group('data')
    # print(matches.groupdict())
    frame = matches.group('frame')
    frame_size = matches.group('frame_size')
    addr = matches.group('addr')
    data = matches.group('data')
    checksum = matches.group('checksum')
    binfile.write(bytes.fromhex(data))

# S70508000BB532
start_addr = int(last_line[4:12], 16)
print(f'start_addr: 0x{start_addr:08X}')
f.close()
