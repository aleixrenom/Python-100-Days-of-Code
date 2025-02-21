import random

NUMBER = random.randint(1, 100)

# Introduction
print("Welcome to the Number Guessing Game!")
print("You'll have to guess a number between 1 and 100")

# Setting the difficulty
attempts = 10 if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy" else 5

def game():
	# Called every time the program wants you to guess, returning a number indicating the outcome of the guess
	def guess():
		chosen_number = int(input("Make a guess: "))
		if chosen_number > NUMBER:
			print("Too high!")
			return 1
		elif chosen_number < NUMBER:
			print("Too low!")
			return 2
		else:
			print("Correct! You win!")
			return 3
	
	# Game start
	print(f"You have {attempts} attempts to guess the number.")

	# Game loop
	attempts_remaining = attempts
	while attempts_remaining > 0:
		ask = guess()
		if ask == 3:
			return
		else:
			attempts_remaining -= 1
			print(f"You have {attempts_remaining} attempts remaining.")
	print(f"Out of attempts, you lose. The number was {NUMBER}.")

game()