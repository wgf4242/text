def print_bytes_addr():
	from idaapi import *
	bytes_addr = 0xCFFFD6F8
	bytes_size = 32
	data = get_bytes(bytes_addr,bytes_size)
	L = [hex(ch) for ch in data]
	print (L)
	# 假密文
	#['0xdd', '0x9f', '0x58', '0xb3', '0x72', '0x80', '0xef', '0x96', '0xc1', '0x2', '0x3b',


# https://www.52pojie.cn/thread-1117330-1-1.html
def print_dword_addr():
	addr=0x08048A90 # 数组的地址
	arr=[]
	for i in range(6): # 数组的个数
	    arr.append(Dword(addr+4*i))
	print(arr)


# CTF特训营 P117
def patch_batch():
	import idaapi
	from idaapi import *
	from idc import *
	from idautils import *

	start_ea = 0x401000

	patterns = [('73 02', 2), ('EB 03', 1), ('72 03 73 01', 1), ('74 03 75 01', 1), ('7E 03 7F 01', 1), ('74 04 75 02', 2)]

	for pattern in patterns:
	    ea = start_ea
	    while True:
	        ea = FindBinary(ea, SEARCH_DOWN, pattern[0])
	        if ea == idaapi.BADADDR:
	            break
	        ea += len(pattern[0].replace(' ', '')) / 2

	        for i in range(pattern[1]):
	            PatchByte(ea + i, 0x90)
	            MakeCode(ea + i)

# https://bbs.pediy.com/thread-260297.htm
def goInitarray(self):
    # _get_modules是idc提供的接口，如其名
    for module in idc._get_modules():
        # 遍历所有module，找到linker
        module_name = module.name
        if 'linker' in module_name:
            print 'linker address is ' + str(hex(module.base + 0x2464))
            # 0x2464是Android某个版本的init_array的偏移地址,
            # jumpto可以直接跳转到目标地址
            idc.jumpto(module.base + 0x2464)
            # 在init_array上下个断点
            idc.add_bpt(module.base + 0x2464, 1)
            # makecode更不用说了，相当于C
            idaapi.auto_make_code(module.base + 0x2464)



# 网鼎杯朱雀组 tree https://www.52pojie.cn/forum.php?mod=viewthread&tid=1181476
def wangding_tree():
	a=[]
	lujing=[]
	def traverse_leaf(pnode):
	    if pnode != 0:
	        if get_wide_dword(pnode + 12) == 0 and get_wide_dword(pnode + 16) == 0:
	            print(chr(get_wide_byte(pnode)))
	            print("".join(a))
	            lujing.append([chr(get_wide_byte(pnode)), "".join(a)])
	        a.append('0')
	        traverse_leaf(get_wide_dword(pnode + 12))
	        a.append('1')
	        traverse_leaf(get_wide_dword(pnode + 16))
	    if pnode != 0x00406530:
	        a.pop()
	  
	  
	traverse_leaf(0x00406530)
	print(lujing)


def preorder():
	addr = 0x00601290
	def preorder_tree(addr):
	    if addr:
	        b = get_wide_byte(addr)
	        print(chr(b))
	        preorder_tree(get_dword(addr + 8))
	        return preorder_tree(get_dword(addr + 16))
	preorder_tree(addr)


def export_asm():
	print "[-] 开始导出反汇编代码"
	import idautils
	ea = idc.ScreenEA()
	addrs = idautils.FuncItems(ea)
	text = ''
	for addr in addrs:
	    #print idc.GetDisasm(addr)
	    text += idc.GetDisasm(addr) + '\n'
	with open("D:\\disasm.txt", 'w')as f:
	    f.write(text)
	print "[+] 成功将当前函数的反汇编代码写入d:\\disasm.txt"


def batch_bytes_selection_nop():
	from ida_bytes import  *
	addr = 0x402219
	for i in range(224):
	    a = addr + i
	    patch_byte(a, get_byte(a) ^ 0x99)


def batch_bytes_xor_smcfix():
	from ida_bytes import  *
	addr = 0x402219
	for i in range(224):
	    a = addr + i
	    patch_byte(a, get_byte(a) ^ 0x99)


def batch_bytes_undefined():
	import ida_bytes

	start_addr = 0x402219
	end_addr = 0x0402220

	for i in range(start_addr, end_addr):
	    ida_bytes.del_items(i)

def jump_addr_next_func():
	import idc
	end = 0x0402220
	ea = idc.get_screen_ea()
	while idc.find_func_end(ea) < end:
	    next_func = get_next_func(ea)
	    print(hex(next_func))
	    idc.jumpto(next_func)
	    ea = idc.get_screen_ea()


def remake_main():
	# 先新建好所有函数, 再执行
	# -- 脚本将start~end所有函数 undefined, 在start处make function
	import ida_bytes

	start_addr = 0x0402126
	end_addr = 0x0402220

	for i in range(start_addr, end_addr):
	    ida_bytes.del_items(i)

	idc.jumpto(start_addr)
	idc.add_func(start_addr)

	import ida_hexrays  # open pseudocode view
	ida_hexrays.open_pseudocode(0x0402126, ida_hexrays.OPF_NO_WAIT)

def ask():
	import ida_kernwin
	ID=ida_kernwin.ask_long(1,"Enemy skill No.?") 
	print(ID)
