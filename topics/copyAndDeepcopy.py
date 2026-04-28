# ~ copy module
# ~ the copy module includes copy() and deepcopy method
# ~ This is especially important when handling lists and dicts

# ~ copy()
import copy

# ~ create a list
alpha = ['Alfa','Bravo','Charlie','Delta']
print(id(alpha))		# prints the id of the list

# ~ copy the list
beta = copy.copy(alpha)
print(id(beta))			# prints id, which is now different
beta[1] = '-...'		# replace a value

print(alpha)
print(beta)

# ~ Thanks to this, the original list remains unchanged while being able to print out a modified list
# ~ deepcopy() is used when a list item contains a list (list inside the list)
