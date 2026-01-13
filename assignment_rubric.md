# Unit 5 Project -  Dice Poker

## Overview
In this project, you'll use Object-Oriented Programming to create two classes, an object and a 'handler' for that object. In this case, the handler will manipulate a series of 'Die' objects and facilitate playing the game of dice poker between these objects.

---
## Part I: The Die

This class will represent a six-sided die. The class will be made into multiple objects that share the same properties, but are unique elements. Your Die needs to possess the following variables and methods:


| Name        | Description                                                                                                                                          |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| face        | The total number of faces on this die, in this case the value is six.                                                                                |
| value       | The current value of the 'rolled face' of the die. The starting value is arbitrary, because we should roll the die before ever referencing it first. |
| Die         | Constructor to build a Die object from the class. Initializes face and value.                                                                        |
| roll()      | Returns the result of rolling the die and updates the value to match.                                                                                |
| get_value() | Returns the current face value of the die.                                                                                                           |

___
## Part II: The DiceHandler

This class operates and manages multiple Die objects and facilitates the functions needed to run a game of Dice Poker. Using a list, we are able to roll, show, and 'keep' dice, as well as determine the scoring for a game of DicePoker.

**Note:** We don't actually field any user interaction in the DiceHandler object itself, rather the DiceHandler handles the dice, and receives input from the main method in order to do so.

| Name        | Description                                                                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dice        | A list of type Die that implements five six-sided dice.                                                                                                                |
| keep_list   | A list of boolean values that keeps track of the retainment of each die when rolling. (true = **don't** roll the die, false = roll the die)                            |
| DiceHandler | Constructor to build a DiceHandler object from the class. Initializes and populates dice and keep_list.                                                                |
| roll()      | Returns a list of each value resulting from rolling all available dice. (*Note: this includes the values of dice that are not rolled in their corresponding position*) |
| show()      | Returns a list of the current face value of all dice.                                                                                                                  |
| keep(idx)   | Sets the corresponding index in the keep list to 'true', denoting that the parallel Die should not be rolled.                                                          |
| score()     | Determines the outcome of the game based on the rules of Dice Poker (see image)                                                                                        |
![[dice_poker.png]]

___
## Part III: Main Method

Your main method does not have to abide by strict rules, you are welcome to use any of the techniques we've learned to facilitate the game of Dice Poker. However, your program should allow users to perform the following actions:
- Start or exit the game. The user is able to restart or end their game whenever a game finished.
- Rolls the dice three times. Each roll, the user is able to choose which dice they'd like to keep, which are not counted in the next roll.
	- Kept dice cannot be un-kept once the next roll resolves.
- Allow the user to select specific dice via menu or marking indices. The dice outlined are marked as 'kept' and cannot be re-rolled for that round.
	- Be sure to allow the user to select AND de-select dice to keep, so long as it's in the same round. (Consider adding the ability to second-guess i.e. 'Are you sure you want to keep 3 and 4' )
- Present information about the dice to the user in a concise and informative way.
	- You **cannot** just print out the list, you must be able to label each Die as 1-5, and allow the user to use those values to select the dice in the list.
	- You can just print the number, or if you desire you can print glyphs representing the pips (dots) on the dice.
	- The game should also present the user with the results of winning. (i.e. print 'Four of a kind!' at the end or 'Full House!' once the score can be calculated.)

The game must be repeatable any number of times, and cannot retain any information from the previous game. A new game of dice poker should refresh the keep list.

___
## Part IV: Extras
Consider adding some extra functionality to your dice poker program, including but not limited to:
- Changing 'difficulties' that increase or decrease the number of rolls the player is allowed to make.
- A multiplayer mode where the kept dice and scoring are tracked differently for each player. According to the rankings in the picture above, the winner has the highest combination.
	- If neither player scores a combo, the highest value die wins. (It is likely you will never reach this state, but this is a contingency.)
- A betting system where the user is rewarded or punished by placing money on a game. If they win, they receive double back. If they lose, they lose all the money bet on that round. The game is considered 'lost' when the sum total money reaches $0, and 'won' when the sum total reaches $1000 (Though you can continue if you feel so included.)
## Key Requirements
By the end of this project, your program should allow for the following functionality:
- [ ] **Properly define a Die** using the class guide above. Your Die object should be able to emulate a real-world six-sided die.
- [ ] **Properly define the DiceHandler** using the class guide above. Your DiceHandler should **only** facilitate the handling of dice, and should not include and non-debugging print() statements or input from the user.
- [ ] **Properly outline the Main** method, with the functions specified above. The main method is the core of your program, and fields interaction between the user and the rest of your objects.
- [ ] **Support Good Programming Practices** such as input validation, error handling, and efficiency. Consider in your testing the events that cause your program to crash or produce unexpected results, you should be able to account for as many issues as you encounter.
- [ ] **Play Dice Poker.** This program should completely support the ability to play one or more games of Dice Poker, following the rules outlines above.

---
## Submission Guidelines
Please submit your file by pushing all changes to your assigned git repository. Your project submission should consist of 2 files
1. dicehandler.py - This file contains both the Die class and DiceHandler.
2. main.py - The main program that uses DiceHandler.
Additionally, include the following:
- **At least three** screenshots of terminal output done from your own testing. Include them in a folder labelled "Screenshots".
___
# Specification Grade Criteria

This project has a total of **30** points, **5** for each specification above. The chart below outlines what constitutes each point rating.

| Score | Problem Solving                                                                                                                                  |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 5     | Response gives evidence of a complete understanding of the problem; is fully developed; is clearly communicated.                                 |
| 4     | Response gives the evidence of a clear understanding of the problem but contains minor errors or is not fully communicated.                      |
| 3     | Response gives evidence of a reasonable approach but indicates gaps in conceptual understanding. Explanations are incomplete, vague, or muddled. |
| 2     | Response gives some evidence of problem understanding but contains major programming or reasoning errors.                                        |
| 1     | No response or response is completely incorrect or irrelevant.                                                                                   |