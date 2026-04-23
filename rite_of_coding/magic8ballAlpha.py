# ~ Magic 8 Ball game with Greek alphabet

# ~ import
import random

# ~ core game function
# ~ l as parameter
def getLetter(l):
	# ~ return corresponding value based on the randomly selected number
	if l == 0:
		return "Alpha"
	if l == 1:
		return "Beta"
	if l == 2:
		return "Gamma"
	if l == 3:
		return "Delta"
	if l == 4:
		return "Epsilon"
	if l == 5:
		return "Zeta"
	if l == 6:
		return "Eta"
	if l == 7:
		return "Theta"
	if l == 8:
		return "Iota"
	if l == 9:
		return "Kappa"

# ~ assign method to variable r
r = random.randint(0,9)

# ~ call function (and store value of called function in a variable)
g = getLetter(r)

# ~ print the value
print(g)
