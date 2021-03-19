#!/usr/bin/env python3

### CONFIGURATION
# Expressed as a dict of dicts: first:second:result
# Rock Paper Scissors
rulesRPS ={
   "Rock": {"Rock": "Draw", "Paper": "Second", "Scissors": "First"},
   "Paper": {"Rock": "First", "Paper": "Draw", "Scissors": "Second"},
   "Scissors": {"Rock": "Second", "Paper": "First", "Scissors": "Draw"}
}

# Rock Paper Scissors Lizard Spock https://www.wikihow.com/Play-Rock-Paper-Scissors-Lizard-Spock
rulesRPSLS ={
   "Rock": 		{"Rock": "Draw",   "Paper": "Second", "Scissors": "First",  "Lizard": "First",  "Spock": "Second"},
   "Paper":		{"Rock": "First",  "Paper": "Draw",   "Scissors": "Second", "Lizard": "Second", "Spock": "First"},
   "Scissors":	{"Rock": "Second", "Paper": "First",  "Scissors": "Draw",   "Lizard": "First",  "Spock": "Second"},
   "Lizard":	{"Rock": "Second", "Paper": "First",  "Scissors": "Second", "Lizard": "Draw",   "Spock": "First"},
   "Spock":		{"Rock": "First",  "Paper": "Second", "Scissors": "First",  "Lizard": "Second",  "Spock": "Draw"}
}

rules = rulesRPSLS
testMe = True

### END OF CONFIG
### FUNCTIONS

def decideWinner(rules, first, second):
	return(rules[first][second])
	
def acceptInput(validInput, inputString):
	return (inputString in validInput)

def getKeysFrom(targetDictionary):
	return( list(dict.keys(targetDictionary))  )

def returnListOfValuesSeparatedBySlashes(targetList):
	sep = " / "
	return(sep.join(targetList))

def buildInputRequest(player, desiredInputs):
	return (player+" player throws "+returnListOfValuesSeparatedBySlashes(desiredInputs)+" : ")

def celebrate(winner, first, second):
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
	
	# Check that the possible inputs are RPS, and only that.
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
					
				assert ((decideWinner(rules, myFirst, mySecond)  == invert(decideWinner(rules, mySecond, myFirst) ))), "symmetry not kept for "+myFirst+" and "+mySecond
				
	# check that this function returns "draw" for two the same
	for hand in validInput:
		assert (decideWinner(rules, hand, hand) == "Draw"), "Same throw ("+throw+") draws" 
	
	# check that each row / col has an even no. of wins / losses
	# NOT DONE
	
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
	assert (celebrate("Draw", "A", "B") == "...and it's a draw!"), "message on draw"
	assert (celebrate("First", "A", "B") == "First wins, as A beats B"), "message on draw"
	assert (celebrate("Second", "A", "B") == "Second wins, as B beats A"), "message on draw"

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
while not (acceptInput(validInputForGame, firstPlayerChoice) ):
	firstPlayerChoice = input(buildInputRequest("First", validInputForGame) )
	
while not (acceptInput(validInputForGame, secondPlayerChoice) ):
	secondPlayerChoice = input(buildInputRequest("Second", validInputForGame) )
	
print(celebrate(decideWinner(rules, firstPlayerChoice, secondPlayerChoice), firstPlayerChoice, secondPlayerChoice))	