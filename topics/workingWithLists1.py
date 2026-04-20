# ~ Working with lists I

# ~ bad example storing values

phoneticA = 'alfa'
phoneticB = 'bravo'
phoneticC = 'charlie'
phoneticD = 'delta'
phoneticE = 'echo'
phoneticF = 'foxtrot'

print(f"{phoneticA}, {phoneticB}, {phoneticC}, {phoneticD}, {phoneticE}, {phoneticF}")

# ~ This method requires me to do everything manually 
# ~ and even repeat myself. But Python was made with DRY in mind

# ~ The next example tries a bit of automaton but I still need to
# ~ type in a lot myself. ANd if the number of phonetics change,
# ~ the program will not be able to store more variables

print('Enter the first phonetic: ')
phonetic1 = input()
print('Enter the second phonetic: ')
phonetic2 = input()
print('Enter the third phonetic: ')
phonetic3 = input()
print('Enter the fourth phonetic: ')
phonetic4 = input()
print('Enter the fifth phonetic: ')
phonetic5 = input()
print('Enter the sixth phonetic: ')
phonetic6 = input()

print(f"The phonetics are {phonetic1}, {phonetic2}, {phonetic3}, {phonetic4}, {phonetic5}, {phonetic6}")

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

# ~ Working with lists III
# Using for Loops with Lists

# Create list
phonetics = ['alfa','bravo','charlie','delta']

# return each item in list
for i in phonetics:
	print(i)

# return index number and corresponding item using range(len())
for i in range(len(phonetics)):
	print(f"Index {str(i)} in phonetics is {phonetics[i]}")

# in and not in Operator
print('Type a phonetic')
callsign = input()
if callsign not in phonetics:
	print(f'{callsign} is not present')
else:
	print(f'Yes {callsign} is present')

# multiple assignment trick
callsign1, callsign2, callsign3, callsign4 = phonetics
print(phonetics)

