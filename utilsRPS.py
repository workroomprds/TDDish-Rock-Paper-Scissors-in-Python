#!/usr/bin/env python3

def acceptInput(validInput, inputString): # game-related - may be refined to allow case-insenstivity / abbreviated (mind S)
	return (inputString in validInput)

def getKeysFrom(targetDictionary): # utility
	return( list(targetDictionary.keys())  )

def returnListOfValuesSeparatedBySlashes(targetList): # just here for testing + meaningful name - could be folded into buildInputRequest
	return(" / ".join(targetList))

def check_that_a_list_has_a_single_unique_value(myInput:list) -> bool:
	"""Returns true if all input are the same"""
	return (len(set(myInput)) == 1) or (len(myInput) == 0)

def test():
	# check that this function returns the keys from a dict
	assert (getKeysFrom({"A":0, "b":1}) == ["A", "b"]), "getValidInput should return keys of a dict - this returns "+str(getKeysFrom({"A":0, "b":1}))
	
	# Check that values in a list can be combined for input mesage
	assert (returnListOfValuesSeparatedBySlashes(["A", "b"]) == "A / b"), "returns values"
	
	# Check that check_that_a_list_has_a_single_unique_value works
	assert (check_that_a_list_has_a_single_unique_value(["A", "A", "A"])), "all same"
	assert (not check_that_a_list_has_a_single_unique_value(["A", "A", "B"])), "one different"
	assert (check_that_a_list_has_a_single_unique_value([])), "empty" 
	
	
test()
