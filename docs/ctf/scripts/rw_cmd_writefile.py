"""
file = "3132" expected "12"
cmd.exe has a maximum command-line length limit of 8191 characters
Win32's CreateProcess has a maximum lpCommandLine length of 32,768 characters
"""
import os

fp = open("nc.exe", 'rb')
while b:=fp.read(4000):
    print(b)
    os.system(f'echo|set/p={b.hex()} >> InFile')
print('run:')
print('CertUtil -decodehex InFile OutFile')

