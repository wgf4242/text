import os
import zipfile
from io import BytesIO


def make_zipfile(filename):
    with zipfile.ZipFile('spam.zip', 'w') as myzip:
        myzip.write(filename)

def make_zipfile_bystr(filename):
    io= BytesIO()
    with zipfile.ZipFile(io, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('file1.txt', "hi")
        zf.writestr('file2.txt', b'123')

def unzip_withpwd(filename, pwd):
    # 有的zip压缩方式不支持
    pwd = pwd.encode('utf8')
    with zipfile.ZipFile(filename) as zf:
        # method 1
        # zf.setpassword(pwd)
        # zf.extractall()
        # zf.extractall('out', pwd=b'a')

        # method 2
        zf.extractall(pwd=pwd)

def zips():  #处理压缩包
    for i in range(1,87):
        zip_file = zipfile.ZipFile(str(i)+'.zip')
        zip_list = zip_file.namelist()  #获取压缩包中的文件
        for f in zip_list:
            zip_file.extract(f, './a')      #将压缩文件放入‘a’文件夹下
        zip_file.close()

def base(): #处理图片中的base64
    flag=""
    for i in range(1,87):
        path ="a/"+ str(i)+".jpg"
        num = os.path.getsize(path)     #获取图片的大小
        f = open(path,'rb')
        f.seek(int(num)-100)                    
        s =  f.read(100)                    #读取最后100个字节
        flag+=bytes.decode(s)       
        f.close()    
    f1 = open('flag.txt','w')
    f1.write(flag)

# 输出文件名
def print_namelist_unknown_charset(filename):  # 处理压缩包
    zip_file = zipfile.ZipFile(filename)
    zip_list = zip_file.namelist()  # 获取压缩包中的文件
    for f in zip_list:
        name = f.encode('437').decode('936')
        print(name)
    zip_file.close()

filename = 'output/zip/外卖箱.zip'
print_namelist_unknown_charset(filename)


import tarfile
import os.path

# 如果是打phar, 使用os.system或python2，python3生成的phar可能服务器解析不了, py2打包的tar是已经gz加密过的
def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


import gzip

def make_gzipfile(output_filename, source_file):
    content = open(source_file, 'rb').read()
    f = gzip.open(output_filename, 'wb')
    f.write(content)
    f.close()

if __name__=="__main__":
    make_zipfile('a1.py')
    # zips()
    # base()
    # make_tarfile('aa.tar', 'dbgsrv')
    # make_gzipfile('aa.gz', 'aa.txt')