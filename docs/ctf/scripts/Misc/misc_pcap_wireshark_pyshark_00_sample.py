import pyshark
def func_s7():
    try:
        captures = pyshark.FileCapture("s702.pcapng")#这里为文件的路径
        func_codes = {}
        for c in captures:
            for pkt in c:
                if pkt.layer_name == "s7comm":
                    if hasattr(pkt, "param_func"):#param_func功能码字段
                        func_code = pkt.param_func
                        if func_code in func_codes:
                            func_codes[func_code] += 1
                        else:
                            func_codes[func_code] = 1
        print(func_codes)
    except Exception as e:
        print(e)

# 提取 s7comm.param.func==5

def extract_s7comm_param_func_5():
    captures = pyshark.FileCapture("s702.pcapng")
    list=[]
    for c in captures:
        for pkt in c:
            if pkt.layer_name == "s7comm" and hasattr(pkt, "param_func"):
                param_func = pkt.param_func
                try:
                    if param_func=='0x00000005':
                        list.append(pkt.resp_data)
                    else:
                        continue
                except Exception as e:
                    print(e)
    print(list)

    result=''
    for i in list:
        result=result+str(i)
    print(result)

