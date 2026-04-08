# Rock, Paper, Scissor with while loop
# imports
import random, sys

# keep track of wins, losses or ties, starting with zero
wins = 0
losses = 0
ties = 0

options = ['r','p','s']
# Core game loop
while True:
	print(f"Wins {wins}, Losses {losses}, Ties {ties}")
	# Player input loop
	while True:
		print("Type your choice")
		player = input()
		if player == 'q':
			sys.exit()
		if player == 'r' or player == 'p' or player == 's':
			break
	computer = random.choice(options)

	# Print player choice
	if player == 'r':
		print("Rock versus ")
	elif player == 'p':
		print("Paper versus ")
	elif player == 's':
		print("Scissors versus")

	#Print computer choice
	if computer == 'r':
		print("Rock")
	elif computer == 'p':
		print("Paper")
	elif computer == 's':
		print("Scissors")

	# Display results and record win/loss/tie
	if player == computer:
		print("It is a tie")
		ties += 1
	elif player == 'r':
		if computer == 's':
			print("You win!")
			wins += 1
		else:
			print("You lose!")
			losses += 1
	elif player == 'p':
		if computer == 'r':
			print("You win!")
			wins += 1
		else:
			print("You lose!")
			losses += 1
	elif player == 's':
		if computer == 'p':
			print("You win!")
			wins += 1
		else:
			print("You lose!")
			losses += 1
