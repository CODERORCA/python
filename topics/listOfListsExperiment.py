# ~ This file is an experiment I made. It's purpose was to help me better understand how data is being processed and in essence, know WHY a function, method, loop works

# ~ Conway's game of life especially was hard to grasp for me until I started to analyze it on the lower levels of abstraction
import copy

width = 2
height = 3

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

