#!/usr/bin/env python3

import utilsRPS as utils


def decide_winner(rules:object, first:str, second:str)->str: 
	"""Taking in rules and choices, picks which side wins (by ref in table) and returns result"""
	return(rules[first][second])

def build_input_request(player:str, desiredInputs:list)->str:
	"""Returns string to ask player to input throw"""
	return (player+" player throws "+utils.return_list_of_values_separated_by_slashes(desiredInputs)+" : ")

def build_announcement(winner:str, first:str, second:str)->str:
	"""Returns string to tell players who has won"""
	if (winner == "Draw"):
		return "...and it's a draw!"
	if (winner == "First"):
		return "First wins, as "+first+" beats "+second
	return "Second wins, as "+second+" beats "+first

def valid_input_for_game(rules:object)->list:
	"""Returns list of valid inputs"""
	return utils.get_keys_from(rules)

def request_valid_input(player:str, rules:object, get_input:object)->str:
	"""Returns a valid choice within the rules - choce from function (typically input)"""
	validSet = valid_input_for_game(rules)
	request = build_input_request(player, validSet)
	choice = ""
	while not (utils.accept_input(validSet, choice) ):
		choice = get_input(request)
	return(choice)




def test():
	"""Runs assertions against local functions"""
	# Check that this function returns the referenced value in a 2D matrix of 'rules'
	rules = {"A":{"A":1, "B":2}, "B":{"A":3, "B":4}}
	assert (decide_winner(rules, "A", "A") == 1)
	assert (decide_winner(rules, "A", "B") == 2)
	assert (decide_winner(rules, "B", "A") == 3)
	assert (decide_winner(rules, "B", "B") == 4)

	# Check that the input maeeage is well-formatted
	assert (build_input_request("A", ["B", "c"]) == "A player throws B / c : "), "function to build input question"

	# Check winning message
	assert (build_announcement("Draw", "A", "B") == "...and it's a draw!"), "message on draw"
	assert (build_announcement("First", "A", "B") == "First wins, as A beats B"), "message on draw"
	assert (build_announcement("Second", "A", "B") == "Second wins, as B beats A"), "message on draw"
	
	# Chaeck valid input for game
	rules = {"A":{"A":1, "B":2}, "B":{"A":3, "B":4}}
	assert (valid_input_for_game(rules) == ["A", "B"])
	
	# Check request_valid_input
	# CAN'T WORK OUT NOW TO DO THIS, YET.
	# Wanted to build capturedOutput, as a spy.
	# capturedOutput catches "First player throws A / B :"
	# but it's not available for checking....
	##rules = {"A":{"A":1, "B":2}, "B":{"A":3, "B":4}}
	##capturedOutput  = ""
	##def captureOutput(input):
	##	print(input)
	##	capturedOutput = input
	##	return validInputForGame(rules)[0]
	##
	##request_valid_input("First", rules, captureOutput )
	##print(capturedOutput)
	##assert (capturedOutput == "First player throws A / B : ")


def testRules(rules):
	"""To test the symmetry of the rules, and more."""
	# ! NEEDS A TEST ITSELF - simple rules...
	
	validInput = utils.get_keys_from(rules)
	
	
	# Checks for each value in validInput
	for hand in validInput:
		# check that this function returns valid
		assert (utils.accept_input(validInput, hand)), hand + " is valid input"
	# check that invalid input is rejected
	assert (utils.accept_input(validInput, "afalhf") == False)
	# Check that wrong case is invalid input
	assert (utils.accept_input(validInput, "rock") == False)
	
	#Check symmetry / ordering - that if A beats B, B loses to A
	for myFirst in validInput:
		for mySecond in validInput:
			if (myFirst != mySecond):
				def invert(winner):
					if (winner=="First"): return "Second"
					if (winner=="Second"): return "First"
					if (winner=="Draw"): return "Draw"
					
				assert ((decide_winner
				(rules, myFirst, mySecond)  == invert(decide_winner
					(rules, mySecond, myFirst) ))), "rules are unsymmetrical for "+myFirst+" and "+mySecond
				
	# check that this function returns "draw" for two the same
	for hand in validInput:
		assert (decide_winner
		(rules, hand, hand) == "Draw"), "Same throw ("+throw+") draws" 
		
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
			wins[myFirst] += 1 if (decide_winner
			(rules, myFirst, mySecond) == "First") else 0
			losses[myFirst] += 1 if (decide_winner
			(rules, myFirst, mySecond) == "Second") else 0
			draws[myFirst] += 1 if (decide_winner
			(rules, myFirst, mySecond) == "Draw") else 0
	assert (utils.check_that_a_list_has_a_single_unique_value(wins.values())), wins  #(that all wins are the same)
	assert (utils.check_that_a_list_has_a_single_unique_value(losses.values())), losses  #(that all losses are the same)
	assert (utils.check_that_a_list_has_a_single_unique_value(draws.values())), draws #(that all draws are the same)
	

test()