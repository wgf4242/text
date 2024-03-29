# 羊城杯2021 Misc520
import zipfile
from pathlib import Path

origin = open('story', 'r', encoding="utf-8").read()

def zips():  #处理压缩包
    while True:
        if not any(True for _ in Path('.').glob('*.zip')):
            return
        for file in Path('.').glob('*.zip'):
            txt = open('story', 'r', encoding="utf-8").read()
            if txt != origin:
                print(txt)
            zip_file = zipfile.ZipFile(file)
            zip_list = zip_file.namelist()  #获取压缩包中的文件
            for f in zip_list:
                zip_file.extract(f, '.')      #将压缩文件放入‘.’文件夹下
            zip_file.close()
            file.unlink()
zips()