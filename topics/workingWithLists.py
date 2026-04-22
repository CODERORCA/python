from phonetics import phon1,phon2,phon3,phon4,allPhon
import random

# ~ Working with lists
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

# ~ create empty list
callsign = []

# ~ core logic, loop will continue until condition is False
while True:
	
	# ~ increment if a phonetic is typed
	print(f'Type the {str(len(callsign)+ 1)}. phonetic or type nothing to skip: ')
	phonetic = input()
	
	# ~ if nothing is typed, break out of loop
	if phonetic == '':
		break
	
	# ~ add value of input as list item to the list
	callsign += [phonetic]

# ~ Return phonetics
print('The phonetics are:')
for phonetic in callsign:
	print(f" - {phonetic}")

# ~ Working with lists III
# Using for Loops with Lists

# ~ return each item in list
for i in phon2:
	print(i)

# ~ return index number and corresponding item using range(len())
for i in range(len(phon1)):
	print(f"Index {str(i)} in phonetics is {phon1[i]}")

# ~ in and not in Operator
print('Type a phonetic')
callsign = input()
if callsign not in phon3:
	print(f'{callsign} is not present')
else:
	print(f'Yes {callsign} is present')

# ~ multiple assignment trick
callsign1, callsign2, callsign3, callsign4 = phon1
print(phon1)

# ~ Example List
# ~ phonetics = ['alfa','bravo','charlie','delta']

# ~ enumerate()
# ~ instead of using range(len(), enumerate returns both the item index and item
for index,item in enumerate(allPhon):
	print(f'The item for {index} in phonetics is {item}')

# ~ Using random.choice() and randome.shuffle()
rnd = random.choice(phon1)
print(rnd)

rnds = random.shuffle(phon2)
print(phon2)

# ~ Finding a Value in a List with index()
item = phon1.index('Alfa')
print(item)

# ~ In case of duplicates, it returns the index of the first item that is found
myList = ['Alfa','Bravo','Charlie','Bravo']
myItem = myList.index('Bravo')
print(myItem)

# ~ add a value to a list with append() and insert()
# ~ append() appends the item to the end of the list
myList2 = ['Foxtrot','Golf','Hotel']
myList2.append('India')
print(myList2)

# ~ insert() allows targeinsert
myList2.insert(0,'Echo')
print(myList2)

# ~ remove an item with remove() when not knowing the index but the item or list value
myList2.remove('Golf')
print(myList2)

# ~ remove an item with del statement when knowing the index of an item but not the list value
del myList2[2]
print(myList2)

# ~ sort lists with sort()
myList3 = ['Zulu','Juliet','Bravo','Romeo']
myList3.sort()
print(myList3)

# ~ pass True to reverse keyword argument to sort in reverse order
myList3.sort(reverse=True)
print(myList3)

# ~ or just use .reverse() to reverse the order of items in a list
myList4 = ['Zulu','Juliet','Bravo','Romeo']
myList4.reverse()
print(myList3)

# ~ interestingly, because of ASCIIbetical order, uppercase letter strings get prinfirst
myList5 = ['Zulu','Juliet','Bravo','Romeo','zulu','juliet','bravo','romeo']
myList5.sort()
print(myList5)

# ~ to sort the values in alphabetical order, pass the key=str.lower kwarg
myList5.sort(key=str.lower)
print(myList5)

# ~ see magic8BallList.py to see how using lists makes writing code for this game more elegant
