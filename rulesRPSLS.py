#!/usr/bin/env python3

from gameRPS import Game

# Rock Paper Scissors Lizard Spock https://www.wikihow.com/Play-Rock-Paper-Scissors-Lizard-Spock
# Expressed as a dict of dicts: first:second:result
rules ={
   "Rock": 		{"Rock": "Draw",   "Paper": "Second", "Scissors": "First",  "Lizard": "First",  "Spock": "Second"},
   "Paper":		{"Rock": "First",  "Paper": "Draw",   "Scissors": "Second", "Lizard": "Second", "Spock": "First"},
   "Scissors":	{"Rock": "Second", "Paper": "First",  "Scissors": "Draw",   "Lizard": "First",  "Spock": "Second"},
   "Lizard":	{"Rock": "Second", "Paper": "First",  "Scissors": "Second", "Lizard": "Draw",   "Spock": "First"},
   "Spock":		{"Rock": "First",  "Paper": "Second", "Scissors": "First",  "Lizard": "Second",  "Spock": "Draw"}
}

def test_data():
   """Tests the rules for specific stuff for this ruleset"""
   game = Game(rules)
   validInput = game.valid_input_for_game()
   
   # Check that the possible inputs are RPSLS, and only that.
   assert (validInput[0] == "Rock")
   assert (validInput[1] == "Paper")
   assert (validInput[2] == "Scissors")
   assert (validInput[3] == "Lizard")
   assert (validInput[4] == "Spock")
   assert (validInput.__len__() == 5), "Number of keys"
   
   # Check sample of rules (note: draws and symmetry already checked)
   assert (game.decide_winner("Rock", "Paper") == "Second"), "Paper wraps Rock"
   assert (game.decide_winner("Rock", "Scissors") == "First"), "Rock blunts Scissors"
   assert (game.decide_winner("Rock", "Lizard") == "First"), "Rock squashes Lizard"
   assert (game.decide_winner("Rock", "Spock") == "Second"), "Spock blasts Rock"
   assert (game.decide_winner("Paper", "Scissors") == "Second"), "Scissors cut paper"
   assert (game.decide_winner("Paper", "Lizard") == "Second"), "Lizard eats paper"
   assert (game.decide_winner("Paper", "Spock") == "First"), "Paper disproves Spock"
   assert (game.decide_winner("Scissors", "Lizard") == "First"), "Scissors stab Lizard"
   assert (game.decide_winner("Scissors", "Spock") == "Second"), "Spock breaks Scissors"
   assert (game.decide_winner("Lizard", "Spock") == "First"), "Lizard poisons Spock"
   assert (game.decide_winner("Spock", "Lizard") == "Second"), "! Lizard poisons Spock"
   
   game.testRules(rules)
   
test_data()