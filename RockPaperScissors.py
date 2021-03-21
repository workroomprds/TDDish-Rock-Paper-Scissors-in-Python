#!/usr/bin/env python3

### CONFIGURATION

# Consider making each ruleset an object, with rules, validAbbreviations, decideWinner, acceptInput

# Rock Paper Scissors
# Expressed as a dict of dicts: first:second:result
rulesRPS ={
   "Rock": {"Rock": "Draw", "Paper": "Second", "Scissors": "First"},
   "Paper": {"Rock": "First", "Paper": "Draw", "Scissors": "Second"},
   "Scissors": {"Rock": "Second", "Paper": "First", "Scissors": "Draw"}
}

# Rock Paper Scissors Lizard Spock https://www.wikihow.com/Play-Rock-Paper-Scissors-Lizard-Spock
# Expressed as a dict of dicts: first:second:result
rulesRPSLS ={
   "Rock": 		{"Rock": "Draw",   "Paper": "Second", "Scissors": "First",  "Lizard": "First",  "Spock": "Second"},
   "Paper":		{"Rock": "First",  "Paper": "Draw",   "Scissors": "Second", "Lizard": "Second", "Spock": "First"},
   "Scissors":	{"Rock": "Second", "Paper": "First",  "Scissors": "Draw",   "Lizard": "First",  "Spock": "Second"},
   "Lizard":	{"Rock": "Second", "Paper": "First",  "Scissors": "Second", "Lizard": "Draw",   "Spock": "First"},
   "Spock":		{"Rock": "First",  "Paper": "Second", "Scissors": "First",  "Lizard": "Second",  "Spock": "Draw"}
}

# consider a dict (for each ruleset) of viable abbreviations -> values

rules = rulesRPSLS
testMe = True

### END OF CONFIG
### FUNCTIONS
#### Perhaps split by util / rules-related / game, in order to allow moving into classes
#### favouring (here) 'pure' functions, for ease of testing & reusability

def decideWinner(rules, first, second): # rules-related - maybe even for specific rules
	return(rules[first][second])
	
def acceptInput(validInput, inputString): # game-related - may be refined to allow case-insenstivity / abbreviated (mind S)
	return (inputString in validInput)

def getKeysFrom(targetDictionary): # utility
	return( list(dict.keys(targetDictionary))  )

def returnListOfValuesSeparatedBySlashes(targetList): # just here for testing + meaningful name - could be folded into buildInputRequest
	return(" / ".join(targetList))

def buildInputRequest(player, desiredInputs): # game-related - text message
	return (player+" player throws "+returnListOfValuesSeparatedBySlashes(desiredInputs)+" : ")

def buildAnnouncement(winner, first, second): # game-related - text message
	if (winner == "Draw"):
		return "...and it's a draw!"
	if (winner == "First"):
		return "First wins, as "+first+" beats "+second
	return "Second wins, as "+second+" beats "+first

### END OF FUNCTIONS	
### TESTS	
	
def testDataRPS(rules):
	validInput = getKeysFrom(rules)
	
	# Check that the possible inputs are RPS, and only that.
	assert (validInput[0] == "Rock")
	assert (validInput[1] == "Paper")
	assert (validInput[2] == "Scissors")
	assert (validInput.__len__() == 3), "Number of keys"
	
	# Check sample of rules (note: draws and symmetry already checked)
	assert (decideWinner(rules, "Rock", "Paper") == "Second"), "Paper should beat Rock"
	assert (decideWinner(rules, "Rock", "Scissors") == "First"), "Rock should beat Scissors"
	assert (decideWinner(rules, "Paper", "Scissors") == "Second"), "Paper should beat Scissors"
	
	
def testDataRPSLS(rules):
	validInput = getKeysFrom(rules)
	
	# Check that the possible inputs are RPSLS, and only that.
	assert (validInput[0] == "Rock")
	assert (validInput[1] == "Paper")
	assert (validInput[2] == "Scissors")
	assert (validInput[3] == "Lizard")
	assert (validInput[4] == "Spock")
	assert (validInput.__len__() == 5), "Number of keys"
	
	# Check sample of rules (note: draws and symmetry already checked)
	assert (decideWinner(rules, "Rock", "Paper") == "Second"), "Paper wraps Rock"
	assert (decideWinner(rules, "Rock", "Scissors") == "First"), "Rock blunts Scissors"
	assert (decideWinner(rules, "Rock", "Lizard") == "First"), "Rock squashes Lizard"
	assert (decideWinner(rules, "Rock", "Spock") == "Second"), "Spock blasts Rock"
	assert (decideWinner(rules, "Paper", "Scissors") == "Second"), "Scissors cut paper"
	assert (decideWinner(rules, "Paper", "Lizard") == "Second"), "Lizard eats paper"
	assert (decideWinner(rules, "Paper", "Spock") == "First"), "Paper disproves Spock"
	assert (decideWinner(rules, "Scissors", "Lizard") == "First"), "Scissors stab Lizard"
	assert (decideWinner(rules, "Scissors", "Spock") == "Second"), "Spock breaks Scissors"
	assert (decideWinner(rules, "Lizard", "Spock") == "First"), "Lizard poisons Spock"
	assert (decideWinner(rules, "Spock", "Lizard") == "Second"), "! Lizard poisons Spock"

def testData(rules):
	# ! NEEDS A TEST ITSELF - simple rules...
	
	validInput = getKeysFrom(rules)

	# Checks for each value in validInput
	for hand in validInput:
		# check that this function returns valid
		assert (acceptInput(validInput, hand)), hand + " is valid input"
	# check that invalid input is rejected
	assert (acceptInput(validInput, "afalhf") == False)
	# Check that wrong case is invalid input
	assert (acceptInput(validInput, "rock") == False)
	
	#Check symmetry / ordering - that if A beats B, B loses to A
	for myFirst in validInput:
		for mySecond in validInput:
			if (myFirst != mySecond):
				def invert(winner):
					if (winner=="First"): return "Second"
					if (winner=="Second"): return "First"
					if (winner=="Draw"): return "Draw"
					
				assert ((decideWinner(rules, myFirst, mySecond)  == invert(decideWinner(rules, mySecond, myFirst) ))), "rules are unsymmatrical for "+myFirst+" and "+mySecond
				
	# check that this function returns "draw" for two the same
	for hand in validInput:
		assert (decideWinner(rules, hand, hand) == "Draw"), "Same throw ("+throw+") draws" 
	
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
			wins[myFirst] += 1 if (decideWinner(rules, myFirst, mySecond) == "First") else 0
			losses[myFirst] += 1 if (decideWinner(rules, myFirst, mySecond) == "Second") else 0
			draws[myFirst] += 1 if (decideWinner(rules, myFirst, mySecond) == "Draw") else 0
	assert (len(set(wins.values())) == 1), wins  #(that all wins are the same)
	assert (len(set(losses.values())) == 1), losses  #(that all losses are the same)
	assert (len(set(draws.values())) == 1), draws #(that all draws are the same)
				
def testFunctions():
	
	# Check that this function returns the referenced value in a 2D matrix of 'rules'
	rules = {"A":{"A":1, "B":2}, "B":{"A":3, "B":4}}
	assert (decideWinner(rules, "A", "A") == 1)
	assert (decideWinner(rules, "A", "B") == 2)
	assert (decideWinner(rules, "B", "A") == 3)
	assert (decideWinner(rules, "B", "B") == 4)
	
	# check that this function returns the keys from a dict
	assert (getKeysFrom({"A":0, "b":1}) == ["A", "b"]), "getValidInput should return keys of a dict"
	
	# Check that values in a list can be combined for input mesage
	assert (returnListOfValuesSeparatedBySlashes(["A", "b"]) == "A / b"), "returns values"
	
	# Check that the input maeeage is well-formatted
	assert (buildInputRequest("A", ["B", "c"]) == "A player throws B / c : "), "function to build input question"

	# Check winning message
	assert (buildAnnouncement("Draw", "A", "B") == "...and it's a draw!"), "message on draw"
	assert (buildAnnouncement("First", "A", "B") == "First wins, as A beats B"), "message on draw"
	assert (buildAnnouncement("Second", "A", "B") == "Second wins, as B beats A"), "message on draw"

#### END OF TESTS
### DO TESTS	
	
if (testMe):
	testFunctions()
	testData(rulesRPS)
	testData(rulesRPSLS)
	testDataRPS(rulesRPS)
	testDataRPSLS(rulesRPSLS)
	
### Initialise
firstPlayerChoice = ""
secondPlayerChoice = ""

validInputForGame = getKeysFrom(rules)


### Main

#### Consider putting this in a loop.
#### Consider keping score
#### Consider an algorothmic opponent (and how to convince that it's not just reading the user input /before/ throwing hand)

while not (acceptInput(validInputForGame, firstPlayerChoice) ):
	firstPlayerChoice = input(buildInputRequest("First", validInputForGame) )
	
while not (acceptInput(validInputForGame, secondPlayerChoice) ):
	secondPlayerChoice = input(buildInputRequest("Second", validInputForGame) )
	
print(buildAnnouncement(decideWinner(rules, firstPlayerChoice, secondPlayerChoice), firstPlayerChoice, secondPlayerChoice))	