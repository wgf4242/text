import zipfile, zlib, string, itertools, tqdm

crcs = {int(i.filename.split('.')[0]): i.CRC for i in zipfile.ZipFile('flag.zip').filelist}
# crcs = {int(i.filename.split('/')[1]): i.CRC for i in zipfile.ZipFile('res_rev.zip').filelist if not i.is_dir()}
crcs = [crcs[i] for i in sorted(crcs)]
print([hex(x) for x in crcs])

f = open('crc32.txt', 'w', encoding='utf8')
for crc in crcs:
    print(f"{crc:08x}:00000000", file=f)
f.close()

# hashcat -m 11500 crc32.txt -O -a 3 ?b?b?b --outfile-format=1,3
# hashcat -m 11500 crc32.txt -O -a 3 ?b?b?b --outfile-format=1,3 --show -o result.txt

# result.txt
"""
55de84d6:00000000:e88286
"""