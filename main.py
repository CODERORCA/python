def collatz(n):
	while n != 1:
		print(n)
		if n % 2 == 0:
			n //= 2
		else:
			n = (n * 3) + 1
		print(n)

try:
	print('Input your integer: ')
	v = int(input())
	if v < 0:
		v = abs(v)
		print('No negative numbers')
	else:
		collatz(v)
except ValueError:
	print('Only integers')
