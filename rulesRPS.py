#!/usr/bin/env python3

import utilsRPS as utils
import gameRPS as game

# Expressed as a dict of dicts: first:second:result
rules = {
   "Rock": {"Rock": "Draw", "Paper": "Second", "Scissors": "First"},
   "Paper": {"Rock": "First", "Paper": "Draw", "Scissors": "Second"},
   "Scissors": {"Rock": "Second", "Paper": "First", "Scissors": "Draw"}
}

def testData():
   validInput = utils.getKeysFrom(rules)
   
   # Check that the possible inputs are RPS, and only that.
   assert (validInput[0] == "Rock")
   assert (validInput[1] == "Paper")
   assert (validInput[2] == "Scissors")
   assert (validInput.__len__() == 3), "Number of keys"
   
   # Check sample of rules (note: draws and symmetry already checked)
   assert (game.decideWinner(rules, "Rock", "Paper") == "Second"), "Paper should beat Rock"
   assert (game.decideWinner(rules, "Rock", "Scissors") == "First"), "Rock should beat Scissors"
   assert (game.decideWinner(rules, "Paper", "Scissors") == "Second"), "Paper should beat Scissors"

   utils.testRules(rules)

testData()
