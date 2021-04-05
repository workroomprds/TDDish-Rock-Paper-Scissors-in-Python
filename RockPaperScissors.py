#!/usr/bin/env python3

### CONFIGURATION
import pytest

import rulesRPS as rulesRPS
import rulesRPSLS as rulesRPSLS
import utilsRPS as utils
import uiRPS as ui
import gameRPS as game

### Initialise
#rules = rulesRPS.rules
rules = rulesRPSLS.rules

### Main
#### Consider making each ruleset an object, with rules, validAbbreviations, decideWinner, acceptInput
#### consider a dict (for each ruleset) of viable abbreviations -> values
#### Consider putting this in a loop.
#### Consider keping score
#### Consider an algorithmic opponent (and how to convince that it's not just reading the user input /before/ throwing hand)

firstPlayerChoice  = game.request_valid_input(player="First",  rules=rules, get_input=ui.askForInput)
secondPlayerChoice = game.request_valid_input(player="Second", rules=rules, get_input=ui.askForInput)

winner = game.decide_winner(rules=rules, first=firstPlayerChoice, second=secondPlayerChoice)

print(game.build_announcement(winner=winner, first=firstPlayerChoice, second=secondPlayerChoice))

def test():
	"""To run tests on modules"""
	rulesRPS.test_data()
	rulesRPSLS.test_data()
	utils.test()
	game.test()
	
	