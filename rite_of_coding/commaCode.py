def commaCode(parameter):
	for item in range(len(parameter)-1):
		print(f"{parameter[item]}, ", end="")
	print(f"and {parameter[item+1]}")

phonetics = ['Alpha','Beta','Gamma','Delta']
argument = phonetics
commaCode(argument)
