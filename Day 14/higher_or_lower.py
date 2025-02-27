from art import logo, vs
from game_data import data
import os
import random

points = 0
radnomised_influencers = data.copy()
random.shuffle(radnomised_influencers)

def game_round(inf_a, inf_b):
	"""Prints and executes a full game round.

	Args:
			inf_a (dictionary): First influencer
			inf_b (dictionary): Second influencer

	Returns:
			string: The correct answer ('a' or 'b') if the player was right, or an empty string if the player was wrong
	"""
	os.system('cls')
	answer = 'a' if inf_a['follower_count'] > inf_b['follower_count'] else 'b'

	print(logo)
	if points > 0: print(f"You're right! Current score: {points}")
	print(f"Compare A: {inf_a['name']}, a {inf_a['description']} from {inf_a['country']}." )
	print(vs)
	print(f"Against B: {inf_b['name']}, a {inf_b['description']} from {inf_b['country']}." )

	guess = input("Who has more followers? Type 'A' or 'B': ").lower()

	if guess == answer:
		return answer
	else:
		return ''

# Game loop
while True:
	influencer_a = radnomised_influencers[0]
	influencer_b = radnomised_influencers[1]
	result = game_round(influencer_a, influencer_b)

	if result != '':
		points += 1

		if result == 'a':
			radnomised_influencers.remove(influencer_b)
		elif result == 'b':
			radnomised_influencers.remove(influencer_a)

	else:
		os.system('cls')
		print(logo)
		print(f"Sorry, that's wrong. Final score: {points}")
		break