#!/usr/bin/env python3

# Rock Paper Scissors Lizard Spock https://www.wikihow.com/Play-Rock-Paper-Scissors-Lizard-Spock
# Expressed as a dict of dicts: first:second:result
rules ={
   "Rock": 		{"Rock": "Draw",   "Paper": "Second", "Scissors": "First",  "Lizard": "First",  "Spock": "Second"},
   "Paper":		{"Rock": "First",  "Paper": "Draw",   "Scissors": "Second", "Lizard": "Second", "Spock": "First"},
   "Scissors":	{"Rock": "Second", "Paper": "First",  "Scissors": "Draw",   "Lizard": "First",  "Spock": "Second"},
   "Lizard":	{"Rock": "Second", "Paper": "First",  "Scissors": "Second", "Lizard": "Draw",   "Spock": "First"},
   "Spock":		{"Rock": "First",  "Paper": "Second", "Scissors": "First",  "Lizard": "Second",  "Spock": "Draw"}
}
