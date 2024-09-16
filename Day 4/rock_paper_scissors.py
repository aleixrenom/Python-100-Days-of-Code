rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

drawing_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
victory_message = "You win!"
loss_message = "You lose."
draw_message = "You draw."
result_message = ""

if user_choice == 0:
    if computer_choice == 0: result_message = draw_message
    if computer_choice == 1: result_message = loss_message
    if computer_choice == 2: result_message = victory_message
elif user_choice == 1:
    if computer_choice == 0: result_message = victory_message
    if computer_choice == 1: result_message = draw_message
    if computer_choice == 2: result_message = loss_message
elif user_choice == 2:
    if computer_choice == 0: result_message = loss_message
    if computer_choice == 1: result_message = victory_message
    if computer_choice == 2: result_message = draw_message

if user_choice > 2 or user_choice < 0:
    print("You wrote an invalid number, please try again.")
else: 
    print(drawing_list[user_choice])
    print("Computer chose:")
    print(drawing_list[computer_choice])
    print(result_message)