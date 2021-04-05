#!/usr/bin/env python3

### CONFIGURATION
import pytest

import rulesRPS as rulesRPS
import rulesRPSLS as rulesRPSLS
import utilsRPS as utils
import uiRPS as ui
from gameRPS import Game
#import gameRPS as gameRPS

### Initialise
#game = Game(rulesRPS.rules)
game = Game(rulesRPSLS.rules)
game.set_user_input_fn(ui.askForInput)

def test():
	"""To run tests on modules"""
	rulesRPS.test_data()
	rulesRPSLS.test_data()
	utils.test()
	game.test()
	
### Main
#### Consider making each ruleset an object, with rules, validAbbreviations, decideWinner, acceptInput
#### consider a dict (for each ruleset) of viable abbreviations -> values
#### Consider putting this in a loop.
#### Consider keping score
#### Consider an algorithmic opponent (and how to convince that it's not just reading the user input /before/ throwing hand)

firstPlayerChoice  = game.request_valid_input(player="First")
secondPlayerChoice = game.request_valid_input(player="Second")

winner = game.decide_winner(first=firstPlayerChoice, second=secondPlayerChoice)

print(game.build_announcement(winner=winner, first=firstPlayerChoice, second=secondPlayerChoice))

	
	