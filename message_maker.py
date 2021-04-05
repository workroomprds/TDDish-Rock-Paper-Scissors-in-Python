#!/usr/bin/env python3

import utilsRPS as utils
import pytest


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

def request_valid_input(player:str, validSet:list, get_input:object)->str:
	"""Returns a valid choice within the rules - choce from function (typically input)"""
	#validSet = valid_input_for_game(rules)
	request = build_input_request(player, validSet)
	choice = ""
	while not (utils.accept_input(validSet, choice) ):
		choice = get_input(request)
	return(choice)


def test():
	"""Runs assertions against local functions"""
	# Check that the input maeeage is well-formatted
	assert (build_input_request("A", ["B", "c"]) == "A player throws B / c : "), "function to build input question"

	# Check winning message
	assert (build_announcement("Draw", "A", "B") == "...and it's a draw!"), "message on draw"
	assert (build_announcement("First", "A", "B") == "First wins, as A beats B"), "message on draw"
	assert (build_announcement("Second", "A", "B") == "Second wins, as B beats A"), "message on draw"
	
	def check_request_valid_input():
		pass
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
		
test()