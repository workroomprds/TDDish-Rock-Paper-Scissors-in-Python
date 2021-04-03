#!/usr/bin/env python3

import gameRPS as game

# Expressed as a dict of dicts: first:second:result
rules = {
   "Rock": {"Rock": "Draw", "Paper": "Second", "Scissors": "First"},
   "Paper": {"Rock": "First", "Paper": "Draw", "Scissors": "Second"},
   "Scissors": {"Rock": "Second", "Paper": "First", "Scissors": "Draw"}
}

def test_data():
   """Tests the rules for specific stuff for this ruleset"""
   validInput = game.valid_input_for_game(rules)
   
   # Check that the possible inputs are RPS, and only that.
   assert (validInput[0] == "Rock")
   assert (validInput[1] == "Paper")
   assert (validInput[2] == "Scissors")
   assert (validInput.__len__() == 3), "Number of keys"
   
   # Check sample of rules (note: draws and symmetry already checked)
   assert (game.decide_winner(rules, "Rock", "Paper") == "Second"), "Paper should beat Rock"
   assert (game.decide_winner(rules, "Rock", "Scissors") == "First"), "Rock should beat Scissors"
   assert (game.decide_winner(rules, "Paper", "Scissors") == "Second"), "Paper should beat Scissors"

   game.testRules(rules)

test_data()
