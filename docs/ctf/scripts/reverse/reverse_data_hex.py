filename = 'daolnwod.zip'

def reverse_file(filename):
	file = open(filename, 'rb')
	data =file.read()
	data_reversed = data[::-1]
	f = open(new_name(filename), 'wb')
	f.write(data_reversed)
	f.close()

def new_name(filename):
	f,ext = filename.split('.')
	return f[::-1] + '.' + ext


if __name__ == '__main__':
	reverse_file(filename)
