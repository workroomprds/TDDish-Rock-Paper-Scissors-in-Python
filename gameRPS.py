#!/usr/bin/env python3

import utilsRPS as utils


def decideWinner(rules, first, second): # rules-related - maybe even for specific rules
	return(rules[first][second])

def buildInputRequest(player, desiredInputs): # game-related - text message
	return (player+" player throws "+utils.returnListOfValuesSeparatedBySlashes(desiredInputs)+" : ")

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

	# Check that the input maeeage is well-formatted
	assert (buildInputRequest("A", ["B", "c"]) == "A player throws B / c : "), "function to build input question"

	# Check winning message
	assert (buildAnnouncement("Draw", "A", "B") == "...and it's a draw!"), "message on draw"
	assert (buildAnnouncement("First", "A", "B") == "First wins, as A beats B"), "message on draw"
	assert (buildAnnouncement("Second", "A", "B") == "Second wins, as B beats A"), "message on draw"



test()