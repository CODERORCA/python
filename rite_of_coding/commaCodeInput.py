def commaCode(parameter):
	for item in range(len(parameter)-1):
		print(f"{parameter[item]}, ", end="")
	print(f"and {parameter[item+1]}")

phonetics = []

while True:
	items = input('Type your item here: ')
	if items != '':
		phonetics.append(items)
	else:
		break
		
argument = phonetics
commaCode(argument)
