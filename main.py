from dicehandler import Dice
from dicehandler import DiceHandler
import random
import os

def clear_terminal(): os.system('cls' if os.name == 'nt' else 'clear')

def main():
	while True:
		# Initial Menu
		print("------------------------------")
		print("[0]. Quit Program")
		print('[1]. Play Dice Poker')
		print('[2]. How to Play Dice Poker')

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
				how_to_play()

def play():
	game = DiceHandler()
	game.roll()
	while True:
		print('Select some dice to Keep.')
		print("------------------------------")
		for i in range(game.hand_size):
			print(f"{i+1}. [{"X" if game.keep_list[i] == True else ""}] {game.dice_list[i].get_value()}")

		try:
			selection = int(input("Input: "))
		except ValueError:
			selection = 0

		try:
			game.toggle_keep(selection-1)
		except IndexError:
			clear_terminal()

		clear_terminal()

def how_to_play():
	pass

if __name__ == "__main__":
	clear_terminal()
	play()