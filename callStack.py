# ~ call stack
# ~ This simple excersize visualizes how stacks work. Imagining a meandering conversation where the current and newly added topic comes first, while the topic that originally has been started is completed last. This is what is called: "First in, Last out", FiLo method

# ~ First function
def a():					# 1. Function defined
	print('a() starts')		# 1.1 Expression executed
	b()						# 1.2 Function called (2.)
	d()						# 3.4 Function called
	print('a() returns')	# 4.3 Expression executed

def b():					# 2. Function defined
	print('b() starts')		# 2.1. Expression executed
	c()						# 2.2 Function called (3.)
	print('b() returns')	# 3.3 Expression executed
	# ~ since a() is not complete, it jumps back to (3.4)

def c():					# 3. Function defined
	print('c() starts')		# 3.1 Expression executed
	print('c() returns')	# 3.2 Expression executed
	# ~ since b() is not complete, it jumps back to (3.3)

def d():					# 4. Function defined
	print('d() starts')		# 4.1 Expression executed
	print('d() returns')	# 4.2 Expression executed
# ~ a() is still not completed, so it will jump back to (4.3)

a()		# 0. Function called (or else Python returns nothing)
