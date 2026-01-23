# Name: Anson Mah
# Project: Dice Poker
# Date: January 2026

from dicehandler import DiceHandler
from display import display_dice
import os

def clear_terminal(): os.system('cls' if os.name == 'nt' else 'clear')

def main():
	while True:
		# Initial Menu
		print("------------------------------")
		print("[0]. Quit Program")
		print('[1]. Play Dice Poker')
		print("[2]. View Settings")
		print("[3]. Change Settings")
		print('[4]. How to Play Dice Poker')

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
				how_to_play()

def play():
	global dice_faces, max_rolls

	current_rolls = 0

	game = DiceHandler(dice_faces)
	current_rolls += 1
	roll_dice_game(game)
	while True:
		print(f'Roll {current_rolls}/{max_rolls}\n')
		print(display_dice(game.show()))

		# End Round on Final Roll
		if current_rolls == max_rolls:
			print("You do not have any more rolls left. The round has automatically ended.")
			break

		print('Select some dice to Keep.')
		print("------------------------------")
		for i in range(game.hand_size):
			print(f"[{"X" if game.keep_list[i] == True else ""}] {game.dice_list[i].get_value()}")
		print(f"{game.hand_size+1}. Roll Dice")
		print(f"{game.hand_size+2}. End Round")

		# Input Validation
		try:
			selection = int(input("Input: "))
		except ValueError:
			selection = 0
		if selection < 0:
			selection = -selection

		# Toggle Dice Keep
		try:
			game.toggle_keep(selection-1)
			clear_terminal()
		except IndexError:
			pass

		# Roll Dice Again
		if selection == game.hand_size + 1:
			if current_rolls < max_rolls:
				roll_dice_game(game)
				current_rolls += 1
		
		# End Round on User Input
		if selection == game.hand_size + 2:
			clear_terminal()
			print(f'Roll {current_rolls}/{max_rolls}\n')
			print(display_dice(game.show()))
			print("You have ended the round.")
			break

		clear_terminal()

	print(f"Your Hand: {game.show()}")
	print(f"Result: {game.score()}")

def roll_dice_game(game):
	for _ in range(50):
		game.roll()
		print(display_dice(game.show()))
		clear_terminal()

def view_settings():
	global dice_faces, max_rolls
	print("Current Settings")
	print("-----------------")
	print(f"Dice Faces: {dice_faces}")
	print(f"Maximum Rolls: {max_rolls}")

def change_settings():
	global dice_faces, max_rolls

	# Settings Menu
	print("Which settings would you like to change?")
	print("-----------------------------------------")
	print("[0]. Exit Settings")
	print("[1]. Dice Faces")
	print("[2]. Maximum Rolls")
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
			# Dice Faces
			while True:
				try:
					user_input = int(input("Input desired # of Dice Faces: "))
				except ValueError:
					print("\nPlease input a positive integer.")
					continue
				if user_input <= 0:
					print("\nYou have inputted a non-positive integer. Please input a positive integer.")
				else:
					dice_faces = user_input
					clear_terminal()
					print(f"# of Dice Faces set to {dice_faces}.\n")
					break
		case 2:
			# Maximum Rolls
			while True:
				try:
					user_input = int(input("Input desired # for Maximum Rolls: "))
				except ValueError:
					print("\nPlease input a positive integer.")
					continue
				if user_input <= 0:
					print("\nYou have inputted a non-positive integer. Please input a positive integer.")
				else:
					max_rolls = user_input
					clear_terminal()
					print(f"# of Maximum Rolls set to {max_rolls}.\n")
					break
		case 3:
			# Restore Default Settings
			dice_faces = 6
			max_rolls = 3
			clear_terminal()
			print("Default Settings have been restored.\n")

	change_settings()

def how_to_play():
	print("How to Play: Dice Poker")

	print("")

	print("OBJECTIVE:")
	print("Use your dice to get the highest Dice Poker hand you possibly can.")

	print("")
	
	print("GAMEPLAY LOOP:")
	print("You start off the round with rolling your 5 dice. This initial roll counts as one of your three rolls.")
	print('You can choose various dice to "Keep".')
	print('After you reroll, the dice you Keep will not get rerolled.')
	print("Keeping dice is a useful mechanic that lets you utilize your 3 rolls to help you roll the best possible Dice Poker hand.")
	print("After rolling 3 times, your hand will be finalized and scored accordingly.")

	print("")

	print("DICE POKER HANDS:")
	print("The ordering of the hands are Highest to Lowest.")
	print("5 of a Kind: Five dice that share the same pip value.")
	print("4 of a Kind: Four dice that share the same pip value.")
	print("Full House: Two dice that share a common pip value along with three dice that share a different common pip value.")
	print("Straight: Five dice with pip values that are in consecutive order.")
	print("3 of a Kind: Three dice that share the same pip value.")
	print("Two Pair: Two dice that share a common pip value along with two different dice that share a different common pip value.")
	print("Pair: Two dice that share a common pip value.")
	print("Highest Dice: None of the above hands apply.")

	print("")

	print("EXAMPLES OF DICE POKER HANDS:")
	print("5 of a Kind: [6, 6, 6, 6, 6]")
	print("4 of a Kind: [5, 5, 5, 5, 3]")
	print("Full House: [2, 2, 3, 3, 3]")
	print("Straight: [1, 2, 3, 4, 5]")
	print("3 of a Kind: [4, 2, 1, 1, 1]")
	print("Two Pair: [2, 2, 1, 5, 5]")
	print("Pair: [6, 6, 1, 5, 2]")
	print("Highest Dice: [2, 6, 5, 3, 1]")

# Game Settings
dice_faces = 6
max_rolls = 3

if __name__ == "__main__":
	main()