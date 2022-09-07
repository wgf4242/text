import zipfile, zlib, string, itertools, tqdm

crcs = {int(i.filename.split('.')[0]): i.CRC for i in zipfile.ZipFile('res_rev.zip').filelist}
crcs = [crcs[i] for i in sorted(crcs)]

with tqdm.tqdm(total=100 ** 4) as pbar:
    for i in itertools.product(string.printable, repeat=4):
        crc32 = zlib.crc32(''.join(i).encode())
        if crc32 in crcs:
            crcs = [''.join(i) if crc == crc32 else crc for crc in crcs]
            print(''.join(i))
            if all(type(x) == str for x in crcs):
               break
        pbar.update(1)
print(''.join(crcs))
