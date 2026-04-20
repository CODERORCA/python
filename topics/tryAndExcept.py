title = 'EXCEPTION HANDLING'
print(f'//// {title} ////\n')

# simple try and exception block using ZeroDivisionError
def alpha(divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		print("Error: Invalid argument")

print(alpha(2))
print(alpha(12))
print(alpha(0))
print(alpha(1))

print('')	# empty print

# putting function calls inside the try block
def beta(divideBy):
	return 42 / divideBy

try:
	print(beta(2))
	print(beta(12))
	print(beta(0))		# error will occur here, so it will skip whatever lies beneath this line
	print(beta(1))
except ZeroDivisionError:
	print("Error: Invalid argument")

