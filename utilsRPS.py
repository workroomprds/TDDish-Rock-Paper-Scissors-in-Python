#!/usr/bin/env python3

def accept_input(validInput:list, inputString:str)->bool: # may need to move to game, if made flexible
	"""Takes in a list and a string, outputs a boolean"""
	return (inputString in validInput)

def get_keys_from(targetDictionary:dict)->list: # utility
	"""Takes in a dict, returns the keys"""
	return( list(targetDictionary.keys())  )

def return_list_of_values_separated_by_slashes(targetList:list)->str: # just here for testing + meaningful name - could be folded into buildInputRequest
	"""Takes in a list, returns a /-separated str"""
	return(" / ".join(targetList))

def check_that_a_list_has_a_single_unique_value(myInput:list) -> bool:
	"""Returns true if all input are the same"""
	return (len(set(myInput)) == 1) or (len(myInput) == 0)


def test():
	"""Test local methods"""
	assert(accept_input(["A", "b"], "A") == True)
	assert(accept_input(["A", "b"], "C") == False)

	# check that this function returns the keys from a dict
	assert (get_keys_from({"A":0, "b":1}) == ["A", "b"]), "getValidInput should return keys of a dict - this returns "+str(get_keys_from({"A":0, "b":1}))
	
	# Check that values in a list can be combined for input mesage
	assert (return_list_of_values_separated_by_slashes(["A", "b"]) == "A / b"), "returns values"
	
	# Check that check_that_a_list_has_a_single_unique_value works
	assert (check_that_a_list_has_a_single_unique_value(["A", "A", "A"])), "all same"
	assert (not check_that_a_list_has_a_single_unique_value(["A", "A", "B"])), "one different"
	assert (check_that_a_list_has_a_single_unique_value([])), "empty" 
	
	
test()
