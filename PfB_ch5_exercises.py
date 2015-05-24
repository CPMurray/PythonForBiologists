# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:12:18 2015

@author: colin
"""

# (1) percentage of amino acid residues, part 1
# write a function that takes two arguments, a protein sequence 
# and an amino acid residue code

# this function returns percentage content of specified amino
# acid residue in specified peptide
#def get_aa_percentage(peptide,aa_residue):
#    # homogenize case
#    peptide = peptide.upper()
#    aa_residue = aa_residue.upper()    
#    
#    # total number of residues in peptide
#    len_peptide = len(peptide) 
#    
#    # number of specified amino acid residues in peptide
#    num_aa_residues = peptide.count(aa_residue)
#    
#    # return percentage content of specified aa residue
#    return 100.0*num_aa_residues/len_peptide
## end function get_aa_percentage

## begin main program
#assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "M") == 5
#assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "r") == 10
#assert get_aa_percentage("msrslllrfllfllllpplp", "L") == 50
#assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
#print("All assertions passed")  

#########################################################
# (2) percentage of amino acid residues, part 2
# modify functio from part 1 so that it accepts a list of
# residues. if no list is given, the function should return 
# the percentage of hydrophobic amino acid residues: 
# A,I,L,M,F,W,Y,V

# this function returns percentage content of specified amino
# acid residues in specified peptide
def get_aa_percentage(peptide, 
                aa_residue=['A','I','L','M','F','W','Y','V']):
    # homogenize case
    peptide = peptide.upper() # peptide is character
    for index in range(len(aa_residue)): # aa_residue is list
        aa = aa_residue[index] # aa is character
        #print(type(aa) is str) # diagnostic: check aa type
        aa_residue[index] = aa.upper()
    #print(aa_residue) # diagnostic
    
    # total number of residues in peptide
    len_peptide = len(peptide) 
    
    # number of specified amino acid residues in peptide
    num_aa_residues = 0 # initialize count
    for index in range(len(aa_residue)):
        aa = aa_residue[index]
        num_aa_residues = num_aa_residues + peptide.count(aa)
        #print("num_aa_residues ",num_aa_residues,"index ", index)
    
    # return percentage content of specified aa residue
    return 100.0*num_aa_residues/len_peptide
# end function get_aa_percentage
    
# begin main program
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP") == 65  
print("All assertions passed")  
    



