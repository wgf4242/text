from stegpy import lsb

password = '512'
file = 'steg.png'

host = lsb.HostElement(file)
# host.read_message(password)

from itertools import product
import string

dic = string.digits
for tp in product(dic, repeat=3):
    password = ''.join(tp)
    host.read_message(password)
