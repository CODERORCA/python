# ~ Sequence Data Types
# ~ Strings and lists are similar if you image strings to be an orderedlist
# ~ the next examples showcase it

phonetic = 'November'

print(phonetic[0])
print(phonetic[:5])
print(phonetic[-4])
if 'n' not in phonetic:
	print('No')
else:
	print('Yes')
if 'vem' not in phonetic:
	print('No')
else:
	print('Yes')

for i in phonetic:
	print(f'//// {i} ////')

# ~ The difference: lists are mutable, while strings are immutable
# ~ one way to change November for example is to create a new variable and tell python which characters based on their index we don't want to change

newPhonetic = phonetic[:1] + 'ö' + phonetic[2:]
print(newPhonetic)

# ~ List values neither cannot be changed unless deleted first and then append the new ones
phonetics = ['Alfa','Bravo','Charlie','Delta']
del phonetics[3]
del phonetics[2]
del phonetics[1]
del phonetics[0]
phonetics.append('Echo')
phonetics.append('Foxtrot')
phonetics.append('Golf')
phonetics.append('Hotel')

print(phonetics)
