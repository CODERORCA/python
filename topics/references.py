# ~ References 
# ~ Technically, what Variables do is store a reference to the actual value
# ~ meaning you can change the value of a variable later on while still being capable
# ~ to access the previous value through another reference.

# ~ The id() function will be used to showcase it

# ~ Here is a simplified example:

# ~ Variable alpha is being assigned the Value
alpha = 42
print(alpha)
print(f"alpha has ID: {id(alpha)}\n")

# ~ Variable beta is having the same Value as Alpha, which creates a reference
beta = alpha
print(beta)
print(f"beta has ID: {id(beta)}\n")

# ~ Now variable alpha receives a new Value. However, since beta is refering to the previous value of alpha, the value of beta won't change
alpha = 100
print(alpha)
print(f"alpha has ID: {id(alpha)}\n")

# ~ however, this does not work w/ lists
gamma = ['Tango','Uniform','Victor']
print(gamma)
print(f"gamma has ID: {id(gamma)}\n")

delta = gamma
print(delta)
print(f"delta has ID: {id(delta)}\n")

gamma[1] = 'Whiskey'
print(f"Result for gamma: {gamma}, ID: {id(gamma)}\n")
print(f"Result for delta: {delta}, ID: {id(delta)}\n")

# ~ What actually happens is Variables actually do not contain values. 
# ~ They are a "Reference" to a Value. Pyton internally assigns an ID, to which a reference can pinpoint to let python know what we want to access. 
# ~ So in essence, Variables are a Reference to a Value, even though people casually say a Variable contains a value.
# ~ That explains why both Variable gamma and delta resulted ro return the same items inside the list, because both are referencing to the same list. No new list has been created or copied (and in essence list items did not get copied)

