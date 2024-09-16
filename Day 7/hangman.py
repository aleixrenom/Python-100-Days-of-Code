import os
import random
from hangman_art import logo, stages
from hangman_words import word_list

# Initial print of the logo for the first guess
print(logo)

chosen_word = random.choice(word_list)
game_over = False
lives = 10
guessed_letters = []

display = []
for _ in chosen_word:
    display += "_"

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f'You already guessed "{guess}"')
        continue  # skips this loop's iteration
    else:
        guessed_letters += guess

# With the letter guessed, we can redraw everything, possibly ending with the prompt for the next guess
    os.system('cls')
    print(logo)
    guessed_right = False

    # Changing the display
    for i, char in enumerate(chosen_word):
        if guess == char:
            display[i] = char
            guessed_right = True

# Reaction to right or wrong guess
    if not guessed_right:
        lives -= 1
        print(f'"{guess}" is not in the word.')
    else:
        print(f'"{guess}" is in the word!')

# Document wrong guesses
    wrong_guesses = []
    for letter in guessed_letters:
        if letter not in chosen_word: wrong_guesses += letter
    if len(wrong_guesses) > 0:
        print(f"Letters guessed wrong: {', '.join(wrong_guesses)}")

# Appropriate hangman drawing
    print(stages[lives])

    # React to the game ending and end the game if the game ends
    if "_" not in display:
        game_over = True
        print(' '.join(display))
        print("You win.")
    elif lives == 0:
        game_over = True
        print(' '.join(display))
        print(f'You lose. The word was "{chosen_word}"')
    else:
        print(' '.join(display))
