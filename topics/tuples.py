# ~ Tuple data type
# ~ Difference between list and tuple
# ~ Writing a tuple

# ~ Lists use []
ListAlpha = ['Alfa','Bravo','Charlie']

# ~ Tuples use ()
tupleAlpha = ('Delta','Echo','Foxtrot')

# ~ in case only one value is stored, a trailing comma is a must or else Python thinks it is a string
tupleBeta = ('Golf')
tupleGamma = ('Hotel',)

print(f"{tupleBeta} - {type(tupleBeta)}")
print(f"{tupleGamma} - {type(tupleGamma)}")

# ~ Removing or adding does not work
# ~ Error handling to prevent crash
tupleDelta = ('India','Juliet','Kilo')

try:
	tupleDelta[1] = 'Mike'
	print(tupleDelta)
except:
	print('\nUser alert! \nAdding method denied in accordance to nature of Tuples.\n')

try:
	tupleDelta.append('Mike')
	print(tupleDelta)
except:
	print('User alert! \nAdding method denied in accordance to nature of Tuples.\n')

try:
	tupleDelta.insert(1,'Mike')
	print(tupleDelta)
except:
	print('User alert! \nInsert method denied in accordance to nature of Tuples.\n')

try:
	tupleDelta.remove('India')
	print(tupleDelta)
except:
	print('User alert! \nRemove method denied in accordance to nature of Tuples.\n')

try:
	del tupleDelta[1]
	print(tupleDelta)
except:
	print('User alert! \nDelete statement denied in accordance to nature of Tuples.\n')

# ~ Casting Data Types also include Tuples and Lists
tupleEpsilon = tuple(['November','Oscar','Papa'])
tupleZeta = tuple('Phonetics')

listEpsilon = list(('Quebec','Romeo','Sierra'))
listZeta = list('Greek Alphabet')

print(tupleEpsilon)
print(listEpsilon)
print(tupleZeta)
print(listZeta)
