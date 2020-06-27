# https://www.wandouip.com/t5i71143/
# https://www.52pojie.cn/forum.php?mod=viewthread&tid=673716&page=1
# https://www.b1ndsec.cn/?p=191
# https://blog.csdn.net/whklhhhh/article/details/78687357

a = 0x2B5C5C25
b = 0x36195D2F
c = 0x7672642C

def rev_hex(hex):
	if type(hex) != int:
		raise 'not number'
	a = bytearray.fromhex(f'{hex:x}')
	a.reverse()
	return a.hex()

def rev_hex_lst(*lst):
	# if type(lst) != list:
	# 	raise 'not list'
	return ''.join(rev_hex(x) for x in lst)


x1 = rev_hex(a)
txt = rev_hex_lst(a,b,c)
print(x1)
print(txt)


s = bytearray.fromhex(txt)
print(s)