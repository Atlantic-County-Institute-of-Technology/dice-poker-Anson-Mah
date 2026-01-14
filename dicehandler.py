import random

class Dice:
	default_value = 1

	def __init__(self, faces):
		self.faces = faces  # How many sides does the dice have?
		self.value = self.default_value  # What side did the dice land on?

	def roll(self):
		self.value = random.randint(1, self.faces)

	# def get_value(self):
	# 	match self.value:
	# 		case 1:
	# 			return "⚀"
	# 		case 2:
	# 			return "⚁"
	# 		case 3:
	# 			return "⚂"
	# 		case 4:
	# 			return "⚃"
	# 		case 5:
	# 			return "⚄"
	# 		case 6:
	# 			return "⚅"

	def get_value(self):
		return self.value
	
class DiceHandler:
	hand_size = 5

	def __init__(self):
		self.dice_list = []
		self.keep_list = []

		for _ in range(self.hand_size):
			self.dice_list.append(Dice(6))
			self.keep_list.append(False)

	# Rolls all unkept dice
	def roll(self):
		for i in range(self.hand_size):
			if self.keep_list[i] == False:
				self.dice_list[i].roll()
			else:
				continue

	# Returns the rolled value of all dice
	def show(self):
		value_list = []
		for i in self.dice_list:
			value_list.append(i.get_value())
		return value_list

	# Toggles the "Keep" value of a certain dice
	def toggle_keep(self, index):
		self.keep_list[index] = not self.keep_list[index]

	# Matches the current hand to the highest possible Dice Poker hand
	def score(self):
		if self.dice_list[0] == self.dice_list[1] == self.dice_list[2] == self.dice_list[3] == self.dice_list[4]:
			return "5oak"

def test1():
	sigma = Dice(6)
	for _ in range(100):
		sigma.roll()
		print(sigma.get_value())

def test2():
	skibidi = DiceHandler()

	skibidi.roll()
	print(skibidi.show())
	
	skibidi.toggle_keep(1)
	skibidi.toggle_keep(3)
	
	skibidi.roll()
	print(skibidi.show())

# test2()