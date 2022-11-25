
file = 'secret_data'
f = open(file, 'rb')

w = open('output', 'wb')
while t:=f.read(4):
    w.write(t[::-1])
