import os
from art import logo
#HINT: You can call clear() to clear the output in the console.

bids = {}

def input_bids():
  print(logo)
  print("Welcome to the secret auction program.")
  print(f"Current amount of bids: {len(bids)}")
  name = input("What is your name?: ")
  amount = int(input("What's your bid?: $"))
  bids[name] = amount

  repeat = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if repeat == 'yes':
    os.system('cls')
    input_bids()

input_bids()

winner_name = "the house"
winner_bid = 0
for key in bids:
  if bids[key] > winner_bid:
    winner_name = key
    winner_bid = bids[key]

os.system('cls')
print(f"The winner is {winner_name} with a bid of ${winner_bid}.")