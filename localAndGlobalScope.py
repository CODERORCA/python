print('//// Local and Global scope //// \n')

# Local scope cannot access local scope in another function
# local scopes can access global scopes
# global scopes cannot access local scopes
# Example
a = 'alpha'		# 		1. value globally assigned

def one():			# 				7. called Function defined
	a = 'bravo'	# 				8. value locally assigned
	print(a)		# 				9. print locally assigned value

def two():			# 			3. called Function defined
	a = 'charlie'	# 			4. value locally assigned
	print(a)		# 			5. print locally assigned value
	one()				# 			6. call function
	print(a)		# 				10. print locally assigned value

two()					# 		2. call function
print(a)			# 				11. prints globally assigned value

# it can become confusing using the same names for global and local scopes.
# Best practice: avoid that

print('\n//// Global statement ////\n')
# sometimes you want to modify a global variable from within a function.
# use the global statement like this:
b = 'delta'			# 		1. value assigned to global scope

def three():			# 			3. called Function defined
	global b			# 			4. set local scope to global scope (think of modify or overwrite the global scope)
	b = 'delta'	# 			5. value gets assigned to local scope

three()					# 		2. call function
print(b)				# 			6. print variable

# this will cause the print expression to return the string bravo instead of alpha.
# For a better feeling of the local and global scopes,
# the following practice run has been written
print('\n//// Practice ////\n')

c = 42					# 1. Global variable set

def four():				#		3. called function defined
	global c			#		4. local variable set to global
	c = 'echo'			#		5. value assigned to local variable
	print(c)
	five()

def five():				#		6. function defined
	c = 'foxtrot'		#		7. value assigned to local variable
	print(c)
	six()

def six():				#		8. function defined
	print(c)			#		9. value assigned to local variable

four()					#	2. call function
print(c)				#		10. printing out value
