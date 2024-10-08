import os
import random

art = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
      |  \/ K|                            _/ |                
      '------'                           |__/           
'''

spades = "\U00002660"
hearts = "\U00002665"
diamonds = "\U00002666"
clubs = "\U00002663"
starting_deck = [f"A{spades}", f"A{hearts}", f"A{diamonds}", f"A{clubs}", f"2{spades}", f"2{hearts}", f"2{diamonds}", f"2{clubs}", f"3{spades}", f"3{hearts}", f"3{diamonds}", f"3{clubs}", f"4{spades}", f"4{hearts}", f"4{diamonds}", f"4{clubs}", f"5{spades}", f"5{hearts}", f"5{diamonds}", f"5{clubs}", f"6{spades}", f"6{hearts}", f"6{diamonds}", f"6{clubs}", f"7{spades}", f"7{hearts}", f"7{diamonds}", f"7{clubs}", f"8{spades}", f"8{hearts}", f"8{diamonds}", f"8{clubs}", f"9{spades}", f"9{hearts}", f"9{diamonds}", f"9{clubs}", f"10{spades}", f"10{hearts}", f"10{diamonds}", f"10{clubs}", f"J{spades}", f"J{hearts}", f"J{diamonds}", f"J{clubs}", f"Q{spades}", f"Q{hearts}", f"Q{diamonds}", f"Q{clubs}", f"K{spades}", f"K{hearts}", f"K{diamonds}", f"K{clubs}"]
deck = list(starting_deck) # "deck = starting_deck" would only store the reference to the list
random.shuffle(deck)

# "card" is string, "current_score" is int
def find_card_value(card, current_score):
	card = card[:-1] # remove the suit symbol before evaluation
	if card == "J" or card == "Q" or card == "K": return 10
	elif card == "A" and current_score < 11: return 11
	elif card == "A": return 1
	else: return int(card)

# "hand_to_value" is list of strings
def find_hand_value(hand_to_value):
	# To avoid aces being wrongly valued they have to be valued last
	hand_to_value.sort(key=(lambda e: e[0] == "A"))

	hand_value = 0
	for card in hand_to_value:
		hand_value += find_card_value(card, hand_value)
	return hand_value

# Draws 1 cards and returns it (string)
def draw():
	global deck
	global starting_deck
	if len(deck) == 0: 
		deck = list(starting_deck)
		random.shuffle(deck)
	card = deck.pop(0)
	return card

# Computer's turn. "comp_hand" and "pl_hand" are lists of strings 
# containing the computer's and player's hands of cards respectively.
# Returns a final hand, being a list of strings
def computer_ai(comp_hand, pl_hand):
	current_hand = comp_hand
	player_score = find_hand_value(pl_hand)
	current_hand.append(draw())

	# If the player already bust, the computer will win by just drawing the 1 card
	if player_score <= 21:
		while find_hand_value(current_hand) < 17:
			current_hand.append(draw())

	return current_hand

# "p_hand" is the player's hand, "c_hand" is the computer's hand
# Does not return anything, just resets the console and prints the new state
def show_scores(p_hand, c_hand):
	os.system('cls')
	print(f"Remaining cards in the deck: {len(deck)}")
	print(art)
	print(f"Your hand: {p_hand}, score: {find_hand_value(p_hand)}")
	print(f"Computer's hand: {c_hand}, score: {find_hand_value(c_hand)}")

# Main game
def blackjack():
	player_hand = []
	computer_hand = []

	player_hand.append(draw())
	player_hand.append(draw())

	computer_hand.append(draw())

	show_scores(player_hand, computer_hand)

	player_playing = True

	while player_playing:
		if find_hand_value(player_hand) >= 21:
			computer_hand = computer_ai(computer_hand, player_hand)
			show_scores(player_hand, computer_hand)
			player_playing = False
			break

		wants_draw = input("Do you want to draw another card? (y/n): ")

		if wants_draw == "y":
			player_hand.append(draw())
			show_scores(player_hand, computer_hand)
		else:
			computer_hand = computer_ai(computer_hand, player_hand)
			show_scores(player_hand, computer_hand)
			player_playing = False

	player_score = find_hand_value(player_hand)
	computer_score = find_hand_value(computer_hand)

	if player_score > 21: print("Loss! 😵 You bust.")
	elif player_score < 21 and computer_score > 21: print("Victory! 😏 The computer bust.")
	elif player_score == 21: print("Blackjack! 🤩")
	elif player_score > computer_score: print("Victory! 😎")
	elif player_score == computer_score: print("Draw! 😐")
	else: print("Loss! ☹️")


playing = True
while playing:
	blackjack()
	play_again = input("Do you want to play again? (y/n): ")
	if play_again != "y": playing = False