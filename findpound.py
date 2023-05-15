#Copyright (c) James Barber 2023 All Rights Reserved

import re

def make_compound_dictionary(compound):
	element_array = re.findall('[^\d]+', compound)
	subscript_array = re.findall('\d+', compound)

	compound_dictionary = {}

	count = 0
	for element in element_array:
		compound_dictionary[element] = subscript_array[count]
		count += 1
	
	return compound_dictionary

elements = {
	'Fe': [1, 2, 3, 4, 5, 6],
	'O': [-2]
}

print("Findpound v0.0.1")

filepath = input("Path to file of compounds (compounds.txt): ")

if filepath == "":
	filepath = "compounds.txt"

max_number_of_elements = int(input("Max number of elements in compound: "))
element_of_interest_text = input("Comma-separated list of elements of interest: ")
state_of_interest = input("State of interest (integer): ")

compounds = []
decimals =[]
elements_of_interest = element_of_interest_text.split(",")

file = open(filepath, 'r')

while True:
	line = file.readline()
	
	if not line:
		break

	has_interests = True

	for element_of_interest in elements_of_interest:
		if element_of_interest not in line:
			has_interests = False

	if has_interests == True:
		if len(re.split('\d+', line)) - 1 <= max_number_of_elements:
			if '.' in line:
				decimals.append(line)
			else:
				compounds.append(make_compound_dictionary(line))

print(compounds)
	
file.close()