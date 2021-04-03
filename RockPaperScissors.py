#!/usr/bin/env python3

### CONFIGURATION
import rulesRPS as rulesRPS
import rulesRPSLS as rulesRPSLS
import utilsRPS as utils
import uiRPS as ui
import gameRPS as game

### Initialise
#rules = rulesRPS.rules
rules = rulesRPSLS.rules



### Main
#### Consider making each ruleset an object, with rules, validAbbreviations, decideWinner, acceptInput
#### consider a dict (for each ruleset) of viable abbreviations -> values
#### Consider putting this in a loop.
#### Consider keping score
#### Consider an algorothmic opponent (and how to convince that it's not just reading the user input /before/ throwing hand)

firstPlayerChoice  = game.requestValidInput("First",  rules , ui.askForInput)
secondPlayerChoice = game.requestValidInput("Second", rules , ui.askForInput)

winner = game.decideWinner(rules, firstPlayerChoice, secondPlayerChoice)

print(game.buildAnnouncement(winner, firstPlayerChoice, secondPlayerChoice))	