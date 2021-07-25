import string


enc ='8842101220480224404014224202480122'
for x in enc.split('0'):
	index = sum(int(n) for n in x)
	print(string.ascii_uppercase[index-1],end='')
print()