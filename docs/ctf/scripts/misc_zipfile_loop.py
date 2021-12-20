import zipfile
from pathlib import Path

def zips():  #处理压缩包
    while True:
        if not any(True for _ in Path('.').glob('*.zip')):
            return
        for file in Path('.').glob('*.zip'):
            zip_file = zipfile.ZipFile(file)
            zip_list = zip_file.namelist()  #获取压缩包中的文件
            for f in zip_list:
                is_encrypted = any(zinfo.flag_bits & 0x1 for zinfo in zip_file.infolist())
                if is_encrypted:
                    filename = (Path(file).stem).encode()
                    zip_file.extract(f, '.', pwd=filename)
                    continue
                zip_file.extract(f, '.')      #将压缩文件放入‘.’文件夹下
                # zip_file.extract(f, '.', pwd=b'123')
            zip_file.close()
            file.unlink()
zips()