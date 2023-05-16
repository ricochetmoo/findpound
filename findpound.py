#Copyright (c) James Barber 2023 All Rights Reserved

import re, itertools

def reverse_compound_dictionary(compound):
	string = ""
	
	for element, subscript in compound.items():
		string += element + subscript
	
	return string

def make_compound_dictionary(compound):
	compound = re.sub('\n', '', compound)
	element_array = re.findall('[^\d]+', compound)
	subscript_array = re.findall('\d+', compound)

	compound_dictionary = {}

	count = 0
	for element in element_array:
		compound_dictionary[element] = subscript_array[count]
		count += 1
	
	return compound_dictionary

elements = {
	'H': [1],
	'He': [0],
	'Li': [1],
	'Be': [2],
	'B': [3],
	'C': [-4. -3. -2, -1, 0, 1, 2, 3, 4],
	'N': [-3. -2, -1, 0, 1, 2, 3, 4, 5],
	'O': [-2],
	'F': [-1],
	'Ne': [0],
	'Na': [1],
	'Mg': [2],
	'Al': [3],
	'Si': [4],
	'P': [-3, 3, 5],
	'S': [-2, 2],
	'Cl': [-1],
	'Ar': [0],
	'K': [1],
	'Ca': [2],
	'Sc': [2, 3],
	'Ti': [2, 3, 4],
	'V': [1, 2, 3, 4, 5],
	'Cr': [1, 2, 3, 4, 5, 6],
	'Mn': [1, 2, 3, 4, 5, 6, 7],
	'Fe': [1, 2, 3, 4, 5, 6],
	'Co': [1, 2, 3, 4],
	'Ni': [1, 2, 3, 4],
	'Cu': [1, 2, 3],
	'Zn': [1, 2],
	'Ga': [3],
	'Ge': [2, 4],
	'As': [-3, 3, 5],
	'Se': [-2, 2, 4, 6],
	'Br': [-1],
	'Kr': [0],
	'Rb': [1],
	'Sr': [2],
	'Y': [3],
	'Zr': [1, 2, 3, 4],
	'Nb': [2, 3, 4, 5],
	'Mo': [1, 2, 3, 4, 5, 6],
	'Ru': [2, 3, 4, 5, 6, 7, 8],
	'Rh': [2, 3, 4, 5, 6],
	'Pd': [1, 2, 3, 4],
	'Ag': [1, 2, 3],
	'Cd': [2],
	'In': [1, 2, 3],
	'Sn': [2, 4],
	'Sb': [3, 5],
	'Te': [2, 4, 6],
	'I': [-1],
	'Xe': [0],
	'Cs': [1],
	'Ba': [2],
	'La': [2, 3],
	'Ce': [3, 4],
	'Pr': [2, 3, 4],
	'Nd': [2, 3],
	'Sm': [2, 3],
	'Eu': [2, 3],
	'Gd': [3],
	'Tb': [3, 4],
	'Dy': [3],
	'Ho': [3],
	'Er': [3],
	'Tm': [3],
	'Yb': [2, 3],
	'Lu': [3],
	'Hf': [4],
	'Ta': [2, 4, 5],
	'W': [2, 3, 4, 5, 6],
	'Re': [2, 3, 4, 5, 6, 7],
	'Os': [2, 3, 4, 5, 6, 7, 8],
	'Ir': [3, 4, 5, 6],
	'Pt': [2, 4],
	'Au': [1, 3, 4],
	'Hg': [1, 2],
	'Tl': [1, 3],
	'Pb': [2, 4],
	'Bi': [3, 5]
}

def sum_permutation(permutation):
	sum = 0

	for oxidation_state in permutation:
		sum += oxidation_state
	
	return sum


def test_for_valid_permutations(compound, primary_element, state_of_interest):
	valence_states_list = []

	for element, subscript in compound.items():
		if element == primary_element:
			valence_states_list.append([int(state_of_interest) * int(subscript)])
		else:
			element_vs_list = elements[element]
			element_vs_list_multiplied = []
			for vs in element_vs_list:
				element_vs_list_multiplied.append(vs * int(subscript))
			valence_states_list.append(element_vs_list_multiplied)

	permutations = itertools.product(*valence_states_list)

	found_permutation = False

	for permutation in permutations:
		if sum_permutation(permutation) == 0:
			found_permutation = True
			break
	
	return found_permutation

print("Findpound v1.0.0")

filepath = input("Path to file of compounds (compounds.txt): ")

if filepath == "":
	filepath = "compounds.txt"

max_number_of_elements = input("Max number of elements in compound (4): ")

if max_number_of_elements == "":
	max_number_of_elements = 4
else:
	max_number_of_elements = int(max_number_of_elements)

element_of_interest_text = input("Comma-separated list of elements required: ")

elements_of_interest = element_of_interest_text.split(",")

primary_element = input("Element of interest (" + elements_of_interest[0] + "): ")

if primary_element == "":
	primary_element = elements_of_interest[0]

state_of_interest = input("Oxidation state of interest: ")

compounds = []
valid_compounds = []
decimals = []

file = open(filepath, 'r')

while True:
	line = file.readline()
	
	if not line:
		break

	has_interests = True

	for element_of_interest in elements_of_interest:
		if element_of_interest not in line:
			has_interests = False
			break

	if has_interests == True:
		if len(re.split('\d+', line)) - 1 <= max_number_of_elements:
			if '.' in line:
				decimals.append(line)
			else:
				compounds.append(make_compound_dictionary(line))

file.close()

for compound in compounds:
	if test_for_valid_permutations(compound, primary_element, state_of_interest):
		valid_compounds.append(reverse_compound_dictionary(compound))

print(valid_compounds)