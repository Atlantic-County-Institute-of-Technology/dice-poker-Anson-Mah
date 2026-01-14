import os
import random
import time

def main():
	while True:
		# Initial Menu
		print("-------------------------")
		print("[0]. Quit Program")
		print('[1]. Play Blackjack')
		print("[2]. View Settings")
		print("[3]. Change Settings")
		print('[4]. Explain Settings')
		print('[5]. How to Play Blackjack')

		# Input Correction
		# If the user's input would break the program, it changes the input such that it will not break the program.
		try:
			selection = int(input("Select an Option: "))
		except ValueError:
			# On ValueError, the input variable is instead set to an integer not corresponding to anything on the menu, which will bring you back to the initial menu
			selection = 9

		clear_terminal()

		# Runs different functions based off of what you inputted
		match selection:
			case 0:
				print("Program Terminated")
				exit()
			case 1:
				play()
			case 2:
				view_settings()
			case 3:
				change_settings()
			case 4:
				explain_settings()
			case 5:
				how_to_play()


class Hand:
	global deck

	def __init__(self, cards, bet):
		self.bet = bet
		self.cards = cards
		self.busted = False
		self.surrendered = False
		self.blackjack = False

	def bust(self):
		self.busted = True

	def surrender(self):
		self.surrendered = True

	def check_blackjack(self):
		if (return_hand_total(self.cards)[0] == 21) and (len(self.cards) == 2):
			self.blackjack = True

	def hit(self):
		self.cards.append(deck.pop(0))

	def double_down(self):
		self.bet *= 2
		self.cards.append(deck.pop(0))

	def split(self):
		return Hand([self.cards.pop()], self.bet)

	# Will print the cards in hand along with the hand's total
	def __str__(self):
		return f"{", ".join(self.cards)} ({return_hand_total(self.cards)[0]})"


def play():
	global deck, money, total_money_bet, card_values, amount_of_decks, hit_on_soft17

	make_deck(amount_of_decks)
	
	# 1. Lots and Lots of Splitting
	# deck = ['8', 'J', '8', '6', '2', 'A', '8', '8', '2', 'J', '5', 'A', '5', 'Q', '3']
	
	# 2. Blackjack after Splitting
	# deck = ['A', 'J', 'A', '5', 'J', 'J', '5']
	# deck = ['A', 'J', 'A', '5', 'J', '9', '5']
	
	# 3. Initial Blackjack
	# deck = ['10', 'Q', 'A', '2']

	bet = bet_money(True)

	while True:
		# Shuffles a new shoe when cards get low
		if len(deck) < 26:
			print("Deck getting low, shuffling a new deck.")
			deck = []
			make_deck(amount_of_decks)

		# Reset Player and Dealer hands
		dealer = Hand([], 0)
		player = [Hand([], bet)]

		# Reset Other Variables
		total_money_bet = bet

		# Deal Out Cards
		for i in range(4):
			if i % 2 == 0:
				player[0].hit()
			else:
				dealer.hit()

			time.sleep(0.5)
			clear_terminal()

			print("-------------------------")
			print(f"Total Money Bet: ${total_money_bet}")
			print(f"Current Bet: ${player[0].bet}\n")

			match i:
				case 0:
					time.sleep(0.5)
					print("Dealer Cards: ")
					print(f"Player Cards: {player[0]}")
				case 1 | 2:
					print(f"Dealer Cards: {dealer.cards[0]}")
					print(f"Player Cards: {player[0]}")
				case 3:
					print(f"Dealer Cards: {dealer.cards[0]}, ?")
					print(f"Player Cards: {player[0]}")
					time.sleep(0.5)
					# clear_terminal()

		# Checks for an Initial Blackjack
		player[0].check_blackjack()
		if player[0].blackjack == True:
			print("\nBlackjack!")
			print(f"Payout: ${bet * 1.5}")
			money += (bet * 1.5)
			print(f"New Balance: ${money}")
			bet = bet_money(False)
			continue

		# Player's Turn
		j = 0
		while j < len(player):
			clear_terminal()
			play_hand(dealer, player, j)
			j += 1

		# Check to see if there's a player hand that has not lost yet
		all_is_lost = True
		for i in range(len(player)):
			if player[i].busted == False and player[i].surrendered == False:
				all_is_lost = False
			else:
				continue

		# Dealer's Turn
		if all_is_lost == False:
			while True:
				clear_terminal()

				print("-------------------------")
				print(f"Total Money Bet: ${total_money_bet}")
				print(f"Current Bet: ${player[0].bet}\n")
				print(f"Dealer Cards: {dealer}")

				# Prints Player's Cards
				for k in range(len(player)):
					if player[k].busted == True:
						print(f"Player Cards: {player[k]} (BUS)")
					elif player[k].surrendered == True:
						print(f"Player Cards: {player[k]} (SUR)")
					elif player[k].blackjack == True:
						print(f"Player Cards: {player[k]} (BLJ)")
					else:
						print(f"Player Cards: {player[k]}")

				dealer_total = return_hand_total(dealer.cards)[0]

				if dealer_total < 17:
					# Hit if under 17
					dealer.hit()
					time.sleep(0.5)
				elif dealer_total > 21:
					dealer.busted = True
					print("\nThe dealer has busted. You win!\n")

					payout = 0
					for i in range(len(player)):
						payout += player[i].bet
					money += payout

					print(f"Your Reward: ${player[0].bet}")
					print(f"New Balance: ${money}")
					break
				elif dealer_total == 17:
					# If 'Hit on Soft 17' is Enabled and the hand is a Soft 17, then Hit
					if hit_on_soft17 == True and return_hand_total(dealer.cards)[1] == True:
						dealer.hit()
						time.sleep(0.5)
					else:
						# Stand on Hard 17 or if 'Hit on Soft 17' is Disabled
						break
				else:
					# Stand if over 17
					break

		# Compare Hands if Nobody Busted
		if dealer.busted == False and all_is_lost == False:
			win_count = 0
			lose_count = 0
			push_count = 0
			payout = 0
			for i in range(len(player)):
				time.sleep(0.5)

				if player[i].busted == True:
					lose_count += 1
					payout -= player[i].bet
					continue
				elif player[i].surrendered == True:
					lose_count += 1
					payout -= (player[i].bet / 2)
					continue
				elif player[i].blackjack == True:
					win_count += 1
					payout += (player[i].bet * 1.5)
					continue

				dealer_total = return_hand_total(dealer.cards)[0]
				player_total = return_hand_total(player[i].cards)[0]

				if player_total > dealer_total:
					win_count += 1
					payout += player[i].bet
				elif dealer_total > player_total:
					lose_count += 1
					payout -= player[i].bet
				else:
					push_count += 1

		if dealer.busted == False and len(player) > 1:
			# Results
			print(f"\nHands Won: {win_count}")
			print(f"Hands Lost: {lose_count}")
			print(f"Hands Pushed: {push_count}")

			# Payout
			money += payout
			print(f"\nPayout: ${payout}")
			print(f"New Balance: ${money}")
		
		if dealer.busted == False and (len(player) == 1 and all_is_lost == False):
			print()
			if player_total > dealer_total:
				print("Result: Win\n")
				money += bet
				print(f"Payout: ${bet}")
				print(f"New Balance: ${money}")
			elif dealer_total > player_total:
				print("Result: Loss\n")
				money -= bet
				print(f"Payout: $-{bet}")
				print(f"New Balance: ${money}")
			else:
				print("Result: Push")
				print("Your balance remains unchanged.")
				print(f"Your Balance: ${money}")

		if money > 0:
			bet = bet_money(False)
		else:
			break

	print("\nYou have no money left. You have been kicked out of the casino.")
	money = 1000


def play_hand(dealer, player, j):
	global money, total_money_bet

	while True:
		# Give extra card after a Split
		if len(player[j].cards) == 1:
			player[j].hit()
			player[j].check_blackjack()
			if player[j].blackjack == True:
				# Player Decisions
				print("-------------------------")
				print(f"Playing Hand {j+1} of {len(player)}")
				print(f"Total Money Bet: ${total_money_bet}")
				print(f"Current Bet: ${player[j].bet}\n")
				print(f"Dealer Cards: {dealer.cards[0]}, ?")

				# Prints Player's Cards
				for k in range(len(player)):
					if j == k:
						print(f"Player Cards: {player[k]}  <--- CURRENT HAND")
					else:
						if player[k].busted == True:
							print(f"Player Cards: {player[k]} (BUS)")
						elif player[k].surrendered == True:
							print(f"Player Cards: {player[k]} (SUR)")
						elif player[k].blackjack == True:
							print(f"Player Cards: {player[k]} (BLJ)")
						else:
							print(f"Player Cards: {player[k]}")

				time.sleep(0.5)
				# Automatically Stand
				break

		# Player Decisions
		print("-------------------------")
		print(f"Playing Hand {j+1} of {len(player)}")
		print(f"Total Money Bet: ${total_money_bet}")
		print(f"Current Bet: ${player[j].bet}\n")
		print(f"Dealer Cards: {dealer.cards[0]}, ?")

		# Prints Player's Cards
		for k in range(len(player)):
			if j == k:
				print(f"Player Cards: {player[k]}  <--- CURRENT HAND")
			else:
				if player[k].busted == True:
					print(f"Player Cards: {player[k]} (BUS)")
				elif player[k].surrendered == True:
					print(f"Player Cards: {player[k]} (SUR)")
				elif player[k].blackjack == True:
					print(f"Player Cards: {player[k]} (BLJ)")
				else:
					print(f"Player Cards: {player[k]}")

		print()
		print("What would you like to do?")
		print("-------------------------")
		print("[1]. Hit")
		print("[2]. Stand")
		print("[3]. Double Down")
		print("[4]. Split")
		print("[5]. Surrender")

		# Input Correction
		# If the user's input would break the program, it changes the input such that it will not break the program.
		try:
			selection = int(input("Select an Option: "))
		except ValueError:
			# On ValueError, the input variable is instead set to an integer not corresponding to anything on the menu, which will bring you back to the initial menu
			selection = 9

		clear_terminal()

		# Runs different functions based off of what you inputted
		match selection:
			case 1:
				# Hit
				player[j].hit()

				if return_hand_total(player[j].cards)[0] > 21:
					print("-------------------------")
					print(f"Playing Hand {j+1} of {len(player)}")
					print(f"Total Money Bet: ${total_money_bet}")
					print(f"Current Bet: ${player[j].bet}\n")
					print(f"Dealer Cards: {dealer.cards[0]}, ?")

					# Prints Player's Cards
					for k in range(len(player)):
						if j == k:
							print(f"Player Cards: {player[k]}  <--- CURRENT HAND")
						else:
							if player[k].busted == True:
								print(f"Player Cards: {player[k]} (BUS)")
							elif player[k].surrendered == True:
								print(f"Player Cards: {player[k]} (SUR)")
							elif player[k].blackjack == True:
								print(f"Player Cards: {player[k]} (BLJ)")
							else:
								print(f"Player Cards: {player[k]}")

					time.sleep(0.5)
					player[j].bust()
					if len(player) == 1:
						print("\nYou have busted. The dealer wins.\n")
						money -= player[j].bet
						print(f"Payout: $-{player[j].bet}")
						print(f"New Balance: ${money}")
					break
			case 2:
				# Stand
				break
			case 3:
				# Double Down
				if len(player[j].cards) > 2:
					print("You can only Double Down on your first choice of the hand.")
				elif player[j].bet > (money - total_money_bet):
					print("You do not have enough money to Double Down.")
				else:
					total_money_bet += player[j].bet
					player[j].double_down()

					print("-------------------------")
					print(f"Playing Hand {j+1} of {len(player)}")
					print(f"Total Money Bet: ${total_money_bet}")
					print(f"Current Bet: ${player[j].bet}\n")
					print(f"Dealer Cards: {dealer.cards[0]}, ?")
					
					# Prints Player's Cards
					for k in range(len(player)):
						if j == k:
							print(f"Player Cards: {player[k]}  <--- CURRENT HAND")
						else:
							if player[k].busted == True:
								print(f"Player Cards: {player[k]} (BUS)")
							elif player[k].surrendered == True:
								print(f"Player Cards: {player[k]} (SUR)")
							elif player[k].blackjack == True:
								print(f"Player Cards: {player[k]} (BLJ)")
							else:
								print(f"Player Cards: {player[k]}")

					if return_hand_total(player[j].cards)[0] > 21:
						if len(player) == 1:
							print("\nYou have busted. The dealer wins.\n")
							money -= player[j].bet
							print(f"Payout: $-{player[j].bet}")
							print(f"New Balance: ${money}")
						player[j].bust()
						
					# End Player's Turn
					time.sleep(0.5)
					break
			case 4:
				# Split
				if len(player[j].cards) > 2:
					print("You can only Split with two cards.")
				elif not (card_values.get(player[j].cards[0]) == card_values.get(player[j].cards[1])):
					print("You can only Split when you have two cards of the same value.")
				elif player[j].bet > (money - total_money_bet):
					print("You do not have enough money to Split.")
				else:
					player.append(player[j].split())
					total_money_bet += player[j].bet
			case 5:
				if len(player) == 1:
					print("You have surrendered your Hand.\n")
					print(f"Your Loss: ${player[j].bet/2}")
					money -= (player[j].bet/2)
					print(f"New Balance: ${money}")
				player[j].surrender()
				break


# Creates decks for the game
def make_deck(amount_of_decks):
	global deck
	ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	for i in range(amount_of_decks):
		for j in range(len(ranks)):
			for k in range(4):
				deck.append(ranks[j])
	random.shuffle(deck)


def bet_money(first_round):
	# Input Validation for the Bet
	while True:
		try:
			if first_round == False:
				user_bet = float(input("\nYour New Bet: $"))
			else:
				print("-------------------------")
				print(f"Your Current Balance: ${money}")
				user_bet = float(input("Your Bet: $"))
				# user_bet = 100
		except ValueError:
			print("Please input a valid bet.")
			continue
		if user_bet > money:
			print(f"You cannot bet more than you have. You currently have ${money}.")
		elif user_bet < 0:
			print("You cannot have a negative bet. Please input a value greater than 0.")
		elif user_bet == 0:
			print("You cannot bet $0. Please input a value greater than 0.")
		else:
			bet = user_bet
			clear_terminal()
			break

	return bet


def return_hand_total(hand):
	global card_values
	is_soft_hand = False

	# Counts total hand value, with Aces automatically being 11
	total = 0
	for i in range(len(hand)):
		total += card_values.get(hand[i])

	if total > 21:
		# Checks for Soft Hands
		if 'A' in hand:
			is_soft_hand = True

			# Will change any necesary Aces from 11-valued to 1-valued
			while hand.count('A') > 0:
				ace_position = hand.index('A')
				hand[ace_position] = 'B'
				new_total = 0
				for i in range(len(hand)):
					new_total += card_values.get(hand[i])
				if new_total <= 21:
					total = new_total
					if hand.count('A') == 0:
						is_soft_hand = False
					for i in range(hand.count('B')):
						b_position = hand.index('B')
						hand[b_position] = 'A'
					break

	return total, is_soft_hand


def view_settings():
	global amount_of_decks, hit_on_soft17
	print("Current Settings")
	print("-----------------")
	print(f"Amount of Decks: {amount_of_decks}")
	print(f"Hit on Soft 17: {'Enabled' if hit_on_soft17 == True else 'Disabled'}")


def change_settings():
	global amount_of_decks, hit_on_soft17

	# Settings Menu
	print("Which settings would you like to change?")
	print("-----------------------------------------")
	print("[0]. Exit Settings")
	print("[1]. Amount of Decks")
	print("[2]. Hit on Soft 17")
	print("[3]. Restore Default Settings")

	# Input Correction
	# If the user's input would break the program, it changes the input such that it will not break the program.
	try:
		selection = int(input("Select an Option: "))
	except ValueError:
		# On ValueError, the input variable is instead set to an integer not corresponding to anything on the menu, which will bring you back to the initial menu
		selection = 9

	match selection:
		case 0:
			clear_terminal()
			main()
		case 1:
			# Amount of Decks
			while True:
				try:
					user_amount_of_decks = int(input("\nInput your desired amount of decks: "))
				except ValueError:
					print("Please input a positive integer.")
					continue
				if user_amount_of_decks <= 0:
					print("You have inputted a non-positive integer. Please input a positive integer.")
				else:
					amount_of_decks = user_amount_of_decks
					clear_terminal()
					print(f"Amount of Decks set to {amount_of_decks}.\n")
					break
		case 2:
			# Hit on 17
			if hit_on_soft17 == True:
				hit_on_soft17 = False
			else:
				hit_on_soft17 = True
			clear_terminal()
			print(f"Hit on Soft 17 has been {'Enabled' if hit_on_soft17 == True else 'Disabled'}.\n")
		case 3:
			# Restore Default Settings
			amount_of_decks = 2
			hit_on_soft17 = False
			clear_terminal()
			print("Default Settings have been restored.\n")

	change_settings()


def explain_settings():
	print("AMOUNT OF DECKS:")
	print("Determines the amount of decks that will be shuffled with each new shoe.")

	print("")

	print("HIT ON SOFT 17:")
	print("By default, the dealer will automatically stand on all hands worth 17.")
	print("Enabling this setting will change that behavior, making the dealer hit on a Soft 17.")
	print("A Soft Hand is a hand that contains an 11-valued Ace. It is called a Soft hand because you cannot Bust if you take another card.")
	print("Note that even with this setting enabled, the dealer will still stand on a Hard 17 (A hand worth 17 but does not have an 11-valued Ace.)")


def how_to_play():
	print("How to Play: Blackjack")

	print("")
	print("")

	print("OBJECTIVE:")
	print("Win money by creating hands that are higher than the dealer's hand but do not exceed 21.")
	
	print("")
	print("")
	
	print("CARD VALUES:")
	print("Cards from 2-10 are worth their face value.")
	print("Face cards (J, Q, K) are worth 10.")
	print("Aces (A) are worth 11 or 1, depending on which is more advantageous to the hand.")
	
	print("")
	print("")
	
	print("ROUND START:")
	print("The dealer begins the round by dealing two cards to you and themself.")
	print("The dealer's cards are dealt one card face-up and another card face-down.")
	print("Both of your cards are dealt face-up.")
	
	print("")
	print("")
	
	print("BLACKJACK:")
	print("If your initial two cards make a value of 21, this is called a BLACKJACK.")
	print("If this happens, you immediately win an amount equal to 1.5 times your initial bet and the hand immediately ends.")
	
	print("")
	print("")
	
	print("PLAYER DECISIONS:")
	print("You will always take your turn first before the dealer takes their turn.")
	
	print("")
	
	print(" Hit: ")
	print(" Take an additional card from the deck and add it to your hand.")
	print(" If your hand becomes over 21 after hitting, this is called a BUST and you automatically lose your bet.")
	print(" You may hit as many times as you like, as long as you do not bust.")
	
	print("")
	
	print(" Stand: ")
	print(" End your turn and keep all cards dealt to you.")
	
	print("")
	
	print(" Double Down:")
	print(" Double your initial bet and add exactly one more card to your hand.")
	print(" After doubling down, you are forced to Stand immediately after.")
	
	print("")
	
	print(" Split:")
	print(" You can decide to Split your cards only if the 2 cards dealt to you are the same value.")
	print(" Splitting transforms the pair into two individual hands, each with their own separate bet equal to the player's initial bet.")
	print(" The dealer then deals you two additional cards to complete each hand.")
	
	print("")
	
	print(" Surrender:")
	print(" Forfeit half your bet and end the hand immediately.")
	
	print("")
	print("")
	
	print("DEALER'S TURN:")
	print("Once you have finished playing your hand(s), the dealer's turn begins.")
	print("The dealer begins their turn by revealing their face-down card.")
	print("Unlike the player, the dealer has specific rules regarding their play which must be followed at all times.")
	print("If the dealer has anything under 17, then they must HIT.")
	print("If the dealer has 17 or over, then they must STAND.")
	print("The dealer cannot DOUBLE DOWN, SPLIT, nor SURRENDER.")
	print("Once the dealer finishes playing their hand, you compare your hand(s) against the dealer's.")
	print("If you have multiple separate hands, then each comparison is resolved individually.")
	
	print("")
	
	print("If the dealer's hand is closer to 21 than yours, you lose your entire bet. ")
	print("If your hand is closer to 21 than the dealer's, you win an amount equal to your bet. ")
	print("If the dealer busts, you win an amount equal to your bet. ")
	print("If you and your dealer have the same value, then you PUSH (Tie), and no exchange of bets is made.")


def clear_terminal(): os.system('cls' if os.name == 'nt' else 'clear')


# Creates empty deck. Will be used later for game purposes.
deck = []		

# Game Settings
amount_of_decks = 2
hit_on_soft17 = False

# Money
money = 1000
total_money_bet = 0

# Card Values
card_values = {
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'10': 10,
	'J': 10,
	'Q': 10,
	'K': 10,
	'A': 11,
	'B': 1,
}

if __name__ == "__main__":
	main()