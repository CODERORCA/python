# local and global scope

one = 'a'

def alpha():
	global one
	one = 'b'
	print(one)
	beta()

def beta():
	one = 'c'
	print(one)
	charlie()

def charlie():
	print(one)

alpha()
print(one)
