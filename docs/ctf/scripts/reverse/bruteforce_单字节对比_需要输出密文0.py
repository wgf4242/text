import subprocess

command = ['./a.out']
res = subprocess.check_output(command, input=b'aaaa\nbbbb')
print(res.decode())

