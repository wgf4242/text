# -*- coding: utf-8 -*
# python2
import utf9
f = open('flag_is_here_rfc4042', 'rb')
s = ''
for line in f:
    s += line
    
print utf9.utf9decode(s)