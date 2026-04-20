# lists
alpha = ['alfa','bravo','charlie','delta']		# variable is list value
print(alpha[2])									# access index 2 of the list
# ~ print(alpha[6])									# accessing outside the list range causes an error (commented out for a reason)
print('')

# accessing a list inside a list
beta = [['echo','foxtrot','golf'],['hotel','juliett'],['kilo','lima','mike']]		# list contains several lists
print(beta[0][1])			# access specific item of a list inside a list. in this example: Access list at index 1, item at index 2
print('')

# negative index
gamma = ['november','oscar','papa','quebec','romeo']
print(gamma[-2])		# read the list in reverse order
print('')

# slices
# lists can also be accessed using slices, notated like this [0:1]
delta = ['sierra','tango','uniform','victor']
print(delta[:3])		# 0 can be skipped if it should be read from index 0
print('')

# get a lists length with len()
epsilon = ['whiskey','xray','yankee','zulu']
print(len(epsilon))
print('')

# change value of a list
zeta = ['alfa','bravo','golf','delta','echo','foxtrot']
zeta[2] = 'charlie'
print(zeta)
print('')

# concatenate and replicate
# the + operator combines two lists. the * operator replicates a list depending on the integer value you assign
print(alpha + gamma)
print('')

print(gamma * 3)
print('')

eta = zeta + epsilon
print(eta)
print('')

# remove list items with the del statement
theta = ['sierra','tango','uniform','victor']
del theta[2]
print(theta)
