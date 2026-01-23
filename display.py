# display.py
# description: A display driver which generates square faces of six-sided die in a terminal interface
# author: pcostjr
# created: 1.15.2026
# last update: 1.16.2026

# dictionary of all possible layer displays for the dice
dlayer = {
	"top"       : f" ╔═══════════╗ ",
	"blank"     : f" ║           ║ ",
	"pip left"  : f" ║  ●        ║ ",
	"pip center": f" ║     ●     ║ ",
	"pip right" : f" ║        ●  ║ ",
	"two pips"  : f" ║  ●     ●  ║ ",
	"bottom"    : f" ╚═══════════╝ "
}

# display the text output of a list of n dice
def display_dice(dice):
	display = ""
	dice_count = len(dice)
	
	# arrange the top layer of the dice
	for i in range(dice_count):
		display += dlayer["top"]
	display += "\n"
	
	# arrange the second layer
	for i in range(dice_count):
		match dice[i]:
			case 1:
				display += dlayer["blank"]
			case 2 | 3:
				display += dlayer["pip left"]
			case 4 | 5 | 6:
				display += dlayer["two pips"]
	display += "\n"
	
	# arrange the third layer
	for i in range(dice_count):
		match dice[i]:
			case 1 | 3 | 5:
				display += dlayer["pip center"]
			case 2 | 4:
				display += dlayer["blank"]
			case 6:
				display += dlayer["two pips"]
	display += "\n"
	
	# arrange the fourth layer
	for i in range(dice_count):
		match dice[i]:
			case 1:
				display += dlayer["blank"]
			case 2 | 3:
				display += dlayer["pip right"]
			case 4 | 5 | 6:
				display += dlayer["two pips"]
	display += "\n"
	
	# arrange the fifth layer
	for i in range(dice_count):
		display += dlayer["bottom"]
	display += "\n"

	# add a numerical value to the bottom of each die for use in the menu
	for i in range(dice_count):
		display += f"      [{i + 1}]      "
	display += "\n"
	
	return display