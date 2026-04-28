# ~ Passing References
# ~ Passing references is critical in understanding how data is handled.
# ~ The example below showcases how references are passed in form of an argument
# ~ to the parameter of the function

def alpha(paramAlfa):				# Function with a parameter
	paramAlfa.append('Hello')		# upon being called, the .append appends the string to the parameter

bravo = [1,2,3]						# a list
print(bravo)						
alpha(bravo)						# list is being passed on as argument to the parameter when function is called. paramAlfa becomes a reference to bravo
print(bravo)						
# ~ Since the function got called ahead, bravo returns printed with the appended string
