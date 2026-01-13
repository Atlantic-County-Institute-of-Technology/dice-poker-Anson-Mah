import random

class Dice:
	default_value = 1

	def __init__(self, faces):
		self.faces = faces  # How many sides does the dice have?
		self.value = self.default_value  # What side did the dice land on?

	def roll(self):
		self.value = random.randint(1, self.faces)

	def get_value(self):
		return self.value
	
class DiceHandler:
	def __init__(self):
		self.dice_list = [Dice(6), Dice(6), Dice(6), Dice(6), Dice(6)]
		self.keep_list = [False, False, False, False, False]

	def roll(self):
		for i in range(len(self.dice_list)):
			if self.keep_list[i] == False:
				self.dice_list[i].roll()
			else:
				continue

	def show(self):
		value_list = []
		for i in self.dice_list:
			value_list.append(i.get_value())
		return value_list

	def keep(self, index):
		self.keep_list[index] = True

	def score(self):
		pass

def test1():
	sigma = Dice(6)
	for i in range(100):
		sigma.roll()
		print(sigma.get_value())

def test2():
	skibidi = DiceHandler()

	skibidi.roll()
	print(skibidi.show())
	
	skibidi.keep(1)
	skibidi.keep(3)
	
	skibidi.roll()
	print(skibidi.show())

if __name__ == "__main__":
	test2()