# ~ magic 8 ball w/ lists

# ~ import
import random

# ~ list
messages = [
"Alpha",
"Beta",
"Gamma",
"Delta",
"Epsilon",
"Zeta",
"Eta",
"Theta",
"Iota",]

# ~ assign method to variable r. It should select the number based on the length of the list, using it's index numbers, starting from 0.
# ~ -1 to prevent out of boundary error
r = random.randint(0, len(messages)-1)

# ~ print from the list it's value determined by the previous method
print(messages[r])
