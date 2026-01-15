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

	def __init__(self, faces):
		self.dice_list = []
		self.keep_list = []

		for _ in range(self.hand_size):
			self.dice_list.append(Dice(faces))
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
		value_list = self.show()
		value_list.sort()

		# 5 of a Kind
		if value_list[0] == value_list[1] == value_list[2] == value_list[3] == value_list[4]:
			return "5 of a Kind"

		# 4 of a Kind
		if (value_list[0] == value_list[1] == value_list[2] == value_list[3]) or (value_list[1] == value_list[2] == value_list[3] == value_list[4]):
			return "4 of a Kind"

		# Full House
		if ((value_list[0] == value_list[1] == value_list[2]) and (value_list[3] == value_list[4])) or ((value_list[0] == value_list[1]) and (value_list[2] == value_list[3] == value_list[4])):
			return "Full House"

		# Straight
		if value_list[0] == value_list[1] - 1 == value_list[2] - 2 == value_list[3] - 3 == value_list[4] - 4:
			return "Straight"

		# 3 of a Kind
		if (value_list[0] == value_list[1] == value_list[2]) or (value_list[1] == value_list[2] == value_list[3]) or (value_list[2] == value_list[3] == value_list[4]):
			return "3 of a Kind"

		# Two Pair
		if ((value_list[0] == value_list[1]) and (value_list[2] == value_list[3])) or ((value_list[1] == value_list[2]) and (value_list[3] == value_list[4])) or ((value_list[0] == value_list[1]) and (value_list[3] == value_list[4])):
			return "Two Pair"

		# Pair
		for i in range(self.hand_size):
			for j in range(self.hand_size):
				if i == j:
					continue
				if value_list[i] == value_list[j]:
					return "Pair"

		# Highest Dice / High Card
		return "Highest Dice"