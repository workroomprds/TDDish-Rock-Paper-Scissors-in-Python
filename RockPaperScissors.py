#!/usr/bin/env python3

### CONFIGURATION

# Consider making each ruleset an object, with rules, validAbbreviations, decideWinner, acceptInput


# Rock Paper Scissors
import rulesRPS as rulesRPS
import rulesRPSLS as rulesRPSLS
import utilsRPS as utils

# consider a dict (for each ruleset) of viable abbreviations -> values

rules = rulesRPS.rules
testMe = True

	
if (testMe): #all these are called within the modules, so this is not needed...
	utils.test()
	rulesRPS.testData()
	rulesRPSLS.testData()
	utils.testRules(rulesRPS.rules)
	utils.testRules(rulesRPSLS.rules)
	
### Initialise
firstPlayerChoice = ""
secondPlayerChoice = ""
validInputForGame = utils.getKeysFrom(rules)


### Main

#### Consider putting this in a loop.
#### Consider keping score
#### Consider an algorothmic opponent (and how to convince that it's not just reading the user input /before/ throwing hand)

while not (utils.acceptInput(validInputForGame, firstPlayerChoice) ):
	firstPlayerChoice = input(utils.buildInputRequest("First", validInputForGame) )
	
while not (utils.acceptInput(validInputForGame, secondPlayerChoice) ):
	secondPlayerChoice = input(utils.buildInputRequest("Second", validInputForGame) )
	
print(utils.buildAnnouncement(utils.decideWinner(rules, firstPlayerChoice, secondPlayerChoice), firstPlayerChoice, secondPlayerChoice))	