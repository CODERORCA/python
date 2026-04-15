# Zig Zag program with inbuilt stop mechanism

# imports
import time, sys

# global parameters for the indents
indent = 0							# Indent start at 0
indentIncreasing = True				# globally to true, can't start with False

try:
# main loop
	while True:
		print(' ' * indent, end='')		# ' ' * indent is to print the correct amount of indents, end = '' prevents a new empty line to be printed
		print('*')						# star characters as example to be returned
		time.sleep(0.2)					# the interval at which the new line gets printed. .sleep annotation to slow the printing down

		# incrementing logic
		if indentIncreasing:
			indent += 1						# increment indents by one
			if indent == 4:					# if the number of indents reaches the specified number
				indentIncreasing = False	# global parameter gets changed to False, hence changing direction

		# decrementing logic
		else:
			indent -= 1							# decrement the number of indents
			if indent == 0:						# if the number of indents reaches zero
				indentIncreasing = True			# reverse direction by setting global parameter to true

# unless if interrupted by a keyboard input (Ctrl+C), the program will continue to create the zig zag
except KeyboardInterrupt:
	sys.exit()
