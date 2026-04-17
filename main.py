callsign = []

while True:
	print(f'Type the {str(len(callsign)+ 1)}. Phonetic or type nothing to skip')
	phonetic = input()
	if phonetic == '':
		break
	callsign += [phonetic]
print('The callsigns are:')
for phonetic in callsign:
	print(f' - {phonetic}')
