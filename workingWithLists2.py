# ~ Working with lists II

# ~ Instead of repetitively typing in the same variables with 
# ~ slight differences, a single variable can be used appending 
# ~ an integer, and then print out the values, using lists

callsign = []	# create empty list

while True:		# core logic, loop will continue until condition is False
	print(f'Type the {str(len(callsign)+ 1)}. phonetic or type nothing to skip: ')	# str(len(phonetic) + 1) will automatically add a number, incrementing it
	phonetic = input()		# input assign to 'call' variable
	if phonetic == '':		# if you type nothing
		break			# break out of loop
	callsign += [phonetic]	# whatever the user typed in gets added to the list (unless typed nothing, then this will be skipped)
print('The phonetics are:')
for phonetic in callsign:	# telling python to return each list value named 'call' inside the list named 'phonetic'
	print(f" - {phonetic}")
