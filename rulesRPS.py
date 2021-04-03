#!/usr/bin/env python3

# Expressed as a dict of dicts: first:second:result
rules = {
   "Rock": {"Rock": "Draw", "Paper": "Second", "Scissors": "First"},
   "Paper": {"Rock": "First", "Paper": "Draw", "Scissors": "Second"},
   "Scissors": {"Rock": "Second", "Paper": "First", "Scissors": "Draw"}
}

