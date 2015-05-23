def get_aa_percentage(protein, aa):
	protein = protein.upper()
	aa = aa.upper()
	aa_count = protein.count(aa)
	protein_length = len(protein)
	percentage = aa_count * 100 / protein_length
	return percentage
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert get_aa_percentage("msrslllrfllfllllpplp", "L") == 50
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
