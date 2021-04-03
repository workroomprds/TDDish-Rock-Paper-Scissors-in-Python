#!/usr/bin/env python3

### CONFIGURATION
import rulesRPS as rulesRPS
import rulesRPSLS as rulesRPSLS
import utilsRPS as utils
import gameRPS as game

#rules = rulesRPS.rules
rules = rulesRPSLS.rules

### Initialise
firstPlayerChoice = ""
secondPlayerChoice = ""
validInputForGame = utils.getKeysFrom(rules)


### Main
#### Consider making each ruleset an object, with rules, validAbbreviations, decideWinner, acceptInput
#### consider a dict (for each ruleset) of viable abbreviations -> values
#### Consider putting this in a loop.
#### Consider keping score
#### Consider an algorothmic opponent (and how to convince that it's not just reading the user input /before/ throwing hand)

while not (utils.acceptInput(validInputForGame, firstPlayerChoice) ):
	firstPlayerChoice = input(game.buildInputRequest("First", validInputForGame) )
	
while not (utils.acceptInput(validInputForGame, secondPlayerChoice) ):
	secondPlayerChoice = input(game.buildInputRequest("Second", validInputForGame) )
	
winner = game.decideWinner(rules, firstPlayerChoice, secondPlayerChoice)

print(game.buildAnnouncement(winner, firstPlayerChoice, secondPlayerChoice))	