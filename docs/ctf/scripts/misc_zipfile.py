import os
import zipfile

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

if __name__=="__main__":
    zips()
    base()