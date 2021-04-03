#!/usr/bin/env python3

def decideWinner(rules, first, second): # rules-related - maybe even for specific rules
	return(rules[first][second])

def acceptInput(validInput, inputString): # game-related - may be refined to allow case-insenstivity / abbreviated (mind S)
	return (inputString in validInput)

def getKeysFrom(targetDictionary): # utility
	return( list(targetDictionary.keys())  )

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

def check_that_a_list_has_a_single_unique_value(myInput:list) -> bool:
	"""Returns true if all input are the same"""
	return (len(set(myInput)) == 1) or (len(myInput) == 0)

def test():
	# Check that this function returns the referenced value in a 2D matrix of 'rules'
	rules = {"A":{"A":1, "B":2}, "B":{"A":3, "B":4}}
	assert (decideWinner(rules, "A", "A") == 1)
	assert (decideWinner(rules, "A", "B") == 2)
	assert (decideWinner(rules, "B", "A") == 3)
	assert (decideWinner(rules, "B", "B") == 4)
	
	# check that this function returns the keys from a dict
	assert (getKeysFrom({"A":0, "b":1}) == ["A", "b"]), "getValidInput should return keys of a dict - this returns "+str(getKeysFrom({"A":0, "b":1}))
	
	# Check that values in a list can be combined for input mesage
	assert (returnListOfValuesSeparatedBySlashes(["A", "b"]) == "A / b"), "returns values"
	
	# Check that check_that_a_list_has_a_single_unique_value works
	assert (check_that_a_list_has_a_single_unique_value(["A", "A", "A"])), "all same"
	assert (not check_that_a_list_has_a_single_unique_value(["A", "A", "B"])), "one different"
	assert (check_that_a_list_has_a_single_unique_value([])), "empty" 
	
	# Check that the input maeeage is well-formatted
	assert (buildInputRequest("A", ["B", "c"]) == "A player throws B / c : "), "function to build input question"
	
	# Check winning message
	assert (buildAnnouncement("Draw", "A", "B") == "...and it's a draw!"), "message on draw"
	assert (buildAnnouncement("First", "A", "B") == "First wins, as A beats B"), "message on draw"
	assert (buildAnnouncement("Second", "A", "B") == "Second wins, as B beats A"), "message on draw"
	
def testRules(rules):
	"""To test the symmetry of the rules, and more."""
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
					
				assert ((decideWinner(rules, myFirst, mySecond)  == invert(decideWinner(rules, mySecond, myFirst) ))), "rules are unsymmetrical for "+myFirst+" and "+mySecond
				
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
	assert (check_that_a_list_has_a_single_unique_value(wins.values())), wins  #(that all wins are the same)
	assert (check_that_a_list_has_a_single_unique_value(losses.values())), losses  #(that all losses are the same)
	assert (check_that_a_list_has_a_single_unique_value(draws.values())), draws #(that all draws are the same)
	
test()
