import random

flips = 100
listOfStreaks = []

def coinFlip(t):
	for f in range(flips):
		if random.randint(0,1) == 0:
			listOfStreaks.append('H')
		else:
			listOfStreaks.append('T')
	print(t)
	
	cStreak = 1
	streaks = 0
	
	for i in range(len(t)):
		if t[i] == t[i-1]:
			cStreak += 1
		else:
			if cStreak >= 6:
				streaks += 1
				cStreak = 1
	print(streaks)

result = listOfStreaks
coinFlip(result)

