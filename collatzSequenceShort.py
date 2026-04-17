def collatz(n):
	while n != 1:
		if n % 2 == 0:
			n //= 2
			print(n)
		else:
			n = (n * 3) + 1
	print(n)

try:
	print('Type in your number')
	v = int(input())
	if v < 0:
		v = abs(v)
		print('No negative number!')
except ValueError:
	print('you must type an integer')
