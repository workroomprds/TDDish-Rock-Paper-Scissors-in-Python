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
	
	# Check that the input maeeage is well-formatted
	assert (buildInputRequest("A", ["B", "c"]) == "A player throws B / c : "), "function to build input question"
	
	# Check winning message
	assert (buildAnnouncement("Draw", "A", "B") == "...and it's a draw!"), "message on draw"
	assert (buildAnnouncement("First", "A", "B") == "First wins, as A beats B"), "message on draw"
	assert (buildAnnouncement("Second", "A", "B") == "Second wins, as B beats A"), "message on draw"
	
	