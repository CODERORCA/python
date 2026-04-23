# import random library
import random

# base of game
def base():
	options = ["rock","paper","scissor"]	# possible choices
	player = input("Make your choice: ")	# player has to make input
	computer = random.choice(options)	# computer asked to make input with the help of random choice
	
# store values of choices in a dict called "choices" (key: value)
	selection = {
	"Player": player,	# store the player input assigned to key called "Player"
	"Computer": computer,	# store the computer input assigned to key called "Computer"
	}

# end iteration and return the values stored in the dict named "choices", will be later used to print the values
	return selection

# execution of game
def game(player,computer):		# passing player and computer variables as arguments to the function
	print(f"Player: {player} \n vs \nComputer: {computer}")		# print out the choices made, stored inside the aforementioned variables

# conditional statements
	if player == computer:		# Tie if both participants have made the same choice
		return "Tie"

# Player has Rock
	elif player == "rock":
		if computer == "scissor":
			return "Win"
		else:
			return "Loss"

# Player has Paper
	elif player == "paper":
		if computer == "rock":
			return "Win"
		else:
			return "Loss"

# Player has Scissor
	elif player == "scissor":
		if computer == "paper":
			return "Win"
		else:
			return "Loss"


# Calling functions
choices = base()	# call base() and assign returned values in variable 'choices'
results = game(choices["Player"], choices["Computer"])		# call game() and return the values of choices according to keys from the dict
print(results)	# print the results according to choice from return statements in game()
