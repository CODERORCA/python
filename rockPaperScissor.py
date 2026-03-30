# Simple rock paper scissors game

# Imports
import random

# Base game
def game():

	# list of options
	options = ["Rock","Paper","Scissors"]

	# Player and Computer input
	player = input("Type your choice: ")
	computer = random.choice(options)

	# Storing values in a dict
	choices = {
	"Player": player,
	"Computer": computer
	}

	return choices

# Conditional setting
def check(player,computer):
	
	# Reveal choices
	print(f"You choose {player}, Computer choose {computer}")
	
	# Tie
	if player == computer:
		return "The game is a tie"
	
	# Player choose Rock
	elif player == "Rock":
		if computer == "Scissors":
			return "The Player wins"
		else:
			return "The Computer takes the win"

	# Player choose Paper
	elif player == "Paper":
		if computer == "Rock":
			return "The Player wins"
		else:
			return "The Computer takes the win"

	# Player choose Scissors
	elif player == "Scissors":
		if computer == "Paper}":
			return "The Player wins"
		else:
			return "The Computer takes the win"

# Call functions
choices = game()

# Printing values assigned to keys in dict
results = check(choices["Player"], choices["Computer"])
print(results)
