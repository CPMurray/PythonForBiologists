# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:35:59 2015

@author: colin
"""

#test
# a second change to the file for bitbucket commit test
# a third change for testing
#print("Hello world")
#print('Hello world')
#print("test escape character \"")
#print("Hello\rworld")

my_dna = "ATGCGTA"
print( my_dna )
my_dna = my_dna + "GGGGGG"
print( my_dna )
print( "len my_dna " + str( len(my_dna) ) )
print(my_dna.lower())

print("\r")
protein = "vlspadktnv"
print(protein)
# replace valine with tyrosine
print(protein.replace("v","y"))
print(protein[1:3])
first_residue = protein[0]

print("\ncount method section")
protein = "vlspadktnv"
# count amino acid residues
valine_count = protein.count("v")
lsp_count = protein.count("lsp")
tryptophan_count = protein.count("w")
# now print the counts
print("valines: " + str(valine_count))
print("lsp's: " + str(lsp_count))
print("tryptophans: " + str(tryptophan_count))
#print("\r")
print(str(protein.find("p")))
print(str(protein.find("kt")))
print(str(protein.find("w")))