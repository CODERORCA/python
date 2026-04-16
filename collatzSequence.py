# import
import sys

# Core function
def collatz(number):
	# conditional statement
	if number % 2 == 0:							# even number
		value = number // 2
	elif number % 2 == 1:						# odd number
		value = (number * 3) + 1

	# loop logic
	while value == 1:
		print(value)
		sys.exit()								# exit if 1
	while value != 1:
		print(value)
		collatz(value)							# reiterate if not 1

# Error Handling
try:
	number = int(input('Type your number'))
	if number < 0:								# no negative numbers
		number = abs(number)
		print('No negative numbers')
	collatz(number)								# otherwise pass the argument to the parameter
except ValueError:								# in case user types anything but integers
	print('you must type an integer')
