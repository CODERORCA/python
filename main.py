import random,copy

width = 3
height = 2

row = []
print(row)
alpha = ['a','b','c']
beta = ['d','e','f']
row.append(alpha)
row.append(beta)
print(row)

currentCells = copy.deepcopy(row)
for y in range(height):
	for x in range(width):
		print(currentCells[x][y],end='')
	print()
