# ~ Working with lists I

# ~ bad example storing values

phoneticA = 'alfa'
phoneticB = 'bravo'
phoneticC = 'charlie'
phoneticD = 'delta'
phoneticE = 'echo'
phoneticF = 'foxtrot'

print(f"{phoneticA}, {phoneticB}, {phoneticC}, {phoneticD}, {phoneticE}, {phoneticF}")

# ~ This method requires me to do everything manually 
# ~ and even repeat myself. But Python was made with DRY in mind

# ~ The next example tries a bit of automaton but I still need to
# ~ type in a lot myself. ANd if the number of phonetics change,
# ~ the program will not be able to store more variables

print('Enter the first phonetic: ')
phonetic1 = input()
print('Enter the second phonetic: ')
phonetic2 = input()
print('Enter the third phonetic: ')
phonetic3 = input()
print('Enter the fourth phonetic: ')
phonetic4 = input()
print('Enter the fifth phonetic: ')
phonetic5 = input()
print('Enter the sixth phonetic: ')
phonetic6 = input()

print(f"The phonetics are {phonetic1}, {phonetic2}, {phonetic3}, {phonetic4}, {phonetic5}, {phonetic6}")
