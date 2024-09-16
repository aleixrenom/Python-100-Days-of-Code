import os
# os.system('cls')
import random

deck = ["A", "A", "A", "A", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]
random.shuffle(deck)

# "card" is string, "current_score" is int
def find_card_value(card, current_score):
	if card == "J" or card == "Q" or card == "K": return 10
	elif card == "A" and current_score < 11: return 11
	elif card == "A": return 1
	else: return int(card)

# "hand" is list of strings
def find_hand_value(hand):
	# To avoid aces being wrongly valued they have to be valued last
	def sort_aces(e): return e == "A"
	hand.sort(key=sort_aces)

	hand_value = 0
	for card in hand:
		hand_value += find_card_value(card, hand_value)
	return hand_value

h = ["2", "A", "K"]
print(find_hand_value(h))