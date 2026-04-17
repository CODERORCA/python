import random	# importing the random library

def getAnswer(getNumber):	# creating function and defining the parameter
	if getNumber == 0:		# if the value of the parameter matches the value passed on
		return "Nothing"	# return the following string
	if getNumber == 1:
		return "Odd and low"
	if getNumber == 2:
		return "Two is good"
	if getNumber == 3:
		return "Still odd but not as low"
	if getNumber == 4:
		return "Keep trying"
	if getNumber == 5:
		return "kinda of a middle here"
	if getNumber == 6:
		return "It's getting better"
	if getNumber == 7:
		return "Almost there"
	if getNumber == 8:
		return "Yeah that is pretty, NOT good"
	if getNumber == 9:
		return "NEIN!"

r = random.randint(0,9)		# create a variable and pass on randomly choosen integer from range 0 to 9, and store it in the said variable
fortune = getAnswer(r)		# create a variable which stores the value when of the function we call and pass the mentioned variable as an argument
print(fortune)		# print the value of the mentioned variable
