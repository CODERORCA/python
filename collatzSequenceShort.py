def collatz(n):

	while n != 1:
		print(n)
		if n % 2 == 0:
			n //= 2
		else:
			n = (n * 3) + 1
	print(n)

try:
	v = abs(int(input('Type your value: ')))
	collatz(v)
except ValueError:
	print('you must type an integer')
