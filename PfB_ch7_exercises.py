# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:28:56 2015

@author: colin
"""

import re

# (1) accession names
# write code that will print accession names that meet various criteria

accs = ( "xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", 
"xjhd53e", "45da", "de37dp" ) # tuple

# contain the number 5
for acc in accs: # cycle through each assession name in accs
    if (re.search(r"5",acc)):
        print(acc, " contains 5")

# contain the letter 'd' or 'e'
for acc in accs: # cycle through each assession name in accs
    if (re.search(r"[de]",acc)):
        print(acc, " contains 'd' or 'e'")

# contains the letters 'd' and 'e' in that order (not necessarily contiguously)
for acc in accs: # cycle through each assession name in accs
    if (re.search(r"d.*e",acc)):
        print(acc, " contains 'd.*e'")

# contain the letter 'd' or 'e' in that order with a single letter between them
for acc in accs: # cycle through each assession name in accs
    if (re.search(r"d.e",acc)):
        print(acc, " contains 'd.e'")

# contain both letters 'd' and 'e' in any order
for acc in accs: # cycle through each assession name in accs
    if ( re.search(r"d.*e",acc) or re.search(r"e.*d",acc) ):
        print(acc, " contains 'd' and 'e' in any order")

# start with 'x' or 'y'
for acc in accs: # cycle through each assession name in accs
    if (re.search(r"^[xy]",acc)):
        print(acc, " starts with 'x' or 'y'")

# start with 'x' or 'y' and ends with 'e'
for acc in accs: # cycle through each assession name in accs
    if (re.search(r"^[xy].*e$",acc)):
        print(acc, " starts with 'x' or 'y' and end with 'e'")

# contains 3 or more numbers in a row
for acc in accs: # cycle through each assession name in accs
    if (re.search(r"[1234567890]{3}",acc)):
        print(acc, " contains 3 or more numbers in a row")

# Jones' improved version
for acc in accs: # cycle through each assession name in accs
    if (re.search(r"\d{3,}",acc)):
        print(acc, " contains 3 or more numbers in a row; Jones")

# end with 'd' followed by either 'a', 'r', or 'p'
for acc in accs: # cycle through each assession name in accs
    if (re.search(r"d[arp]$",acc)):
        print(acc, " ends with 'd' followed by either 'a','r',or 'p'")


###########################################################################
# (2) double digest
# import sequence form ch7 dna.txt. predict fragment lengths of digestion by
# (made-up restriction enzymes) AbcI ANT*AAT and AbcII GCRW*TG, where * 
# represents the position of the cut sites

dir_name = "exercises/chapter_7/"
file_name = "dna.txt"
readstr = dir_name + file_name # read string

# open input file and read
infile = open(readstr,"r")
dna = infile.read().rstrip("\n")
infile.close()

# instantiate list to contain cut indices
cut_positions = []

# not sure what 'real' convention is, but i am assuming that cuts take 
# are made to the right of index, AFTERNOTE: Jones' uses left convention
# A N T*A A T
# 0 1 2 3 4 5 
# here the cut is made at index 2, where index 0 is start position of motif,
# and left-fragment has length index # + 1
# last fragment will have length len(dna) - (lastCutPos+1), eg if only 1 cut
# above (if dna = "ATNAAT"), then len(dna)=6 and lastCutPos = 2

# http://en.wikipedia.org/wiki/Nucleic_acid_notation
# "Degenerate base symbols in biochemistry are an IUPAC representation for a
#  position on a DNA sequence that can have multiple possible alternatives. 
#  These should not be confused with non-canonical bases ..."
# N -> any Nucleotide (not a gap)
# R -> puRine, A or G
# W -> Weak, A or T

# find cut positions of AbcI, motif ANT*AAT, * is cut location
cuts_AbcI = re.finditer(r"A[ATGC]TAAT",dna) # sequence of match objects
for match in cuts_AbcI:
    # cuts take place 2 positions over from motif start index
    cut_positions.append( match.start() + 2 )
    
# find cut positions of AbcII, motif GCRW*TG, * is cut location
cuts_AbcII = re.finditer(r"GC[AG][AT]TG",dna)
for match in cuts_AbcII:
    # cuts take place 3 positions over from motif start index
    cut_positions.append( match.start() + 3 )
    
# sort the cut_positions list
cut_positions.sort()
print("\ncut positions ", cut_positions) # diagnostic

# calculate fragments after full digestion
# n cuts will result in n+1 fragments
fragment_lengths = [] # instantiate list for fragment lengths

# first fragment length will be cut_positions[0] + 1
# second length will be cut_positions[1] - cut_positions[0]
# third -> cut_positions[2] - cut_positions[1]
# nth -> cut_positions[n-1] - cut_positions[n-2]
# last -> len_dna - cut_positions[-1] (value in last element of cut_positions)

for i in range( len(cut_positions) ):
    if (i == 0): # first fragment
        fragment_lengths.append( cut_positions[0] + 1)
    else : # 2nd through next to last fragments
        fragment_lengths.append( cut_positions[i] - cut_positions[i-1] )
    # end if
# end for
        
# last fragment
fragment_lengths.append( len(dna) - (cut_positions[-1] + 1) ) 

print("fragment lengths: ",fragment_lengths)
    
# sum of fragments lengths should equal length of original sequence
assert sum(fragment_lengths) == len(dna)





















