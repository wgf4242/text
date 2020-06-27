import os,glob
os.chdir("1234")
txt =''
for file in sorted(glob.glob('*')):
	txt += open(file).read()
print(txt)