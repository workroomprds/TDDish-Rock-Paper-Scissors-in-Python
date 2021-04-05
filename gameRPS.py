#!/usr/bin/env python3

import utilsRPS as utils
import message_maker as message_maker
import pytest

class Game:
	
	def __init__(self, rules):
		self.rules = rules
		self.input_fn = ""

	def request_valid_input(self, player:str)->str:
		return message_maker.request_valid_input(player, self.valid_input_for_game(), self.input_fn)
	
	def build_announcement(self, winner, first, second)->str:
		return message_maker.build_announcement(winner, first, second)
	
	def decide_winner(self, first:str, second:str)->str: 
		"""Taking in rules and choices, picks which side wins (by ref in table) and returns result"""
		return(self.rules[first][second])

	def valid_input_for_game(self)->list:
		"""Returns list of valid inputs"""
		return utils.get_keys_from(self.rules)

	def set_user_input_fn(self, get_input_fn):
		self.input_fn = get_input_fn


	def test(self):
		"""Runs assertions against local functions"""
		rules_test = Game({"A":{"A":1, "B":2}, "B":{"A":3, "B":4}})

		# Check that this function returns the referenced value in a 2D matrix of 'rules'
		assert (rules_test.decide_winner("A", "A") == 1)
		assert (rules_test.decide_winner("A", "B") == 2)
		assert (rules_test.decide_winner("B", "A") == 3)
		assert (rules_test.decide_winner("B", "B") == 4)
	
		# Check valid input for game
		assert (rules_test.valid_input_for_game() == ["A", "B"])
		
		# Check build_announcement
		# Not going to bother - it's a straight call
		
		# Check request_valid_input
		# returns a fn - test when I know how
		
		# again, testing a a function
		#assert (self.set_user_input_fn)
		


	workingRules = {"A":{"A":"Draw", "B":"First", "C":"Second"}, "B":{"A":"Second", "B":"Draw", "C":"First"}, "C":{"A":"First", "B":"Second", "C":"Draw"}}
	def testRules(self,rules=workingRules):
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
				def invert(winner):
					if (winner=="First"): return "Second"
					if (winner=="Second"): return "First"
					if (winner=="Draw"): return "Draw"
					
				assert ((self.decide_winner(myFirst, mySecond)  == invert(self.decide_winner(mySecond, myFirst) ))), "rules are unsymmetrical for "+myFirst+" and "+mySecond
					
		# check that this function returns "draw" for two the same
		for hand in validInput:
			assert (self.decide_winner(hand, hand) == "Draw"), "Same throw ("+throw+") draws" 
			
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
				wins[myFirst] += 1 if (self.decide_winner(myFirst, mySecond) == "First") else 0
				losses[myFirst] += 1 if (self.decide_winner(myFirst, mySecond) == "Second") else 0
				draws[myFirst] += 1 if (self.decide_winner(myFirst, mySecond) == "Draw") else 0
		assert (utils.check_that_a_list_has_a_single_unique_value(wins.values())), wins  #(that all wins are the same)
		assert (utils.check_that_a_list_has_a_single_unique_value(losses.values())), losses  #(that all losses are the same)
		assert (utils.check_that_a_list_has_a_single_unique_value(draws.values())), draws #(that all draws are the same)
	

## for running tests here
workingRules = {"A":{"A":"Draw", "B":"First", "C":"Second"}, "B":{"A":"Second", "B":"Draw", "C":"First"}, "C":{"A":"First", "B":"Second", "C":"Draw"}}
g = Game(workingRules)
g.test()
g.testRules()