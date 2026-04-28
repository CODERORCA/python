# ~ Convay's game of life
# imports
import random,time,copy

# cell width and height
WIDTH = 20
HEIGHT = 20

# ~ Create cells
row = []		# create a list which is the row
for x in range(WIDTH):
	column = []							# create a column, which creates a list of lists
	for y in range(HEIGHT):
		if random.randint(0,1) == 0:	# 50/50 chance for cell to start off alive or dead
			column.append('#|')			# add living cell
		else:
			column.append(' |')			# add dead cell
	row.append(column)
# ~ This function basically says: Create a list. For each index item inside that list, create a list. Randomly choose the item in the inner list is # or ' |'. Append the result to the outer list

# ~ Program logic
while True:
	print('\n')
	currentCells = copy.deepcopy(row)
	# ~ We use deepcopy (like talked in previous lesson, to copy a list of lists items but keep the original intact)
	
	# ~ Print cells 
	for y in range(HEIGHT):
		for x in range(WIDTH):
			print(currentCells[x][y], end='')
		print()
	# ~ This tells python: print the full range of our list in each row, then take the next row and repeat this
	
	# ~ Cell logic
	for x in range(WIDTH):
		for y in range(HEIGHT):
			# ~ Getting coordinates of neighbor cell, with `% WIDTH` ensuring leftCoord is always between 0 and WIDTH - 1
			leftCoord = (x - 1) % WIDTH
			rightCoord = (x + 1) % WIDTH
			aboveCoord = (y - 1) % HEIGHT
			belowCoord = (y + 1) % HEIGHT

			# count living cells
			numNeighbors = 0
			
			if currentCells[leftCoord][aboveCoord] == '#|':
				numNeighbors += 1
				
			if currentCells[x][aboveCoord] == '#|':
				numNeighbors += 1
				
			if currentCells[rightCoord][aboveCoord] == '#|':
				numNeighbors += 1
				
			if currentCells[leftCoord][y] == '#|':
				numNeighbors += 1
				
			if currentCells[rightCoord][y] == '#|':
				numNeighbors += 1
				
			if currentCells[leftCoord][belowCoord] == '#|':
				numNeighbors += 1
				
			if currentCells[x][belowCoord] == '#|':
				numNeighbors += 1
				
			if currentCells[rightCoord][belowCoord] == '#|':
				numNeighbors += 1
				
				
	# ~ Rules
	# ~ Cell stay alive 
			if currentCells[x][y] == '#|' and (numNeighbors == 2 or numNeighbors == 3):
				row[x][y] = '#|'
			# ~ Bring cell to life
			elif currentCells[x][y] == ' |' and numNeighbors == 3:
				row[x][y] = '#|'
			# ~ Cell dies 
			else:
				row[x][y] = ' |'
	time.sleep(.1)
