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

### END OF CONFIG
### FUNCTIONS
#### Perhaps split by util / rules-related / game, in order to allow moving into classes
#### favouring (here) 'pure' functions, for ease of testing & reusability

### END OF FUNCTIONS	
### TESTS	
	
def testRules(rules):
	# ! NEEDS A TEST ITSELF - simple rules...
	
	validInput = utils.getKeysFrom(rules)


	# Checks for each value in validInput
	for hand in validInput:
		# check that this function returns valid
		assert (utils.acceptInput(validInput, hand)), hand + " is valid input"
	# check that invalid input is rejected
	assert (utils.acceptInput(validInput, "afalhf") == False)
	# Check that wrong case is invalid input
	assert (utils.acceptInput(validInput, "rock") == False)
	
	#Check symmetry / ordering - that if A beats B, B loses to A
	for myFirst in validInput:
		for mySecond in validInput:
			if (myFirst != mySecond):
				def invert(winner):
					if (winner=="First"): return "Second"
					if (winner=="Second"): return "First"
					if (winner=="Draw"): return "Draw"
					
				assert ((utils.decideWinner(rules, myFirst, mySecond)  == invert(utils.decideWinner(rules, mySecond, myFirst) ))), "rules are unsymmetrical for "+myFirst+" and "+mySecond
				
	# check that this function returns "draw" for two the same
	for hand in validInput:
		assert (utils.decideWinner(rules, hand, hand) == "Draw"), "Same throw ("+throw+") draws" 
	
	# check that the rules are 'fair': that each valid item has the same number of wins/losses/draws
	# ignore that wins should == losses, if symmatry is kept above.
	wins = {}
	losses = {}
	draws = {}
	for myFirst in validInput:
		wins[myFirst] = 0
		losses[myFirst] = 0
		draws[myFirst] = 0
		for mySecond in validInput:
			wins[myFirst] += 1 if (utils.decideWinner(rules, myFirst, mySecond) == "First") else 0
			losses[myFirst] += 1 if (utils.decideWinner(rules, myFirst, mySecond) == "Second") else 0
			draws[myFirst] += 1 if (utils.decideWinner(rules, myFirst, mySecond) == "Draw") else 0
	assert (len(set(wins.values())) == 1), wins  #(that all wins are the same)
	assert (len(set(losses.values())) == 1), losses  #(that all losses are the same)
	assert (len(set(draws.values())) == 1), draws #(that all draws are the same)
				
#### END OF TESTS
### DO TESTS	
	
if (testMe):
	utils.test()
	rulesRPS.testData()
	rulesRPSLS.testData()
	testRules(rulesRPS.rules)
	testRules(rulesRPSLS.rules)
	
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