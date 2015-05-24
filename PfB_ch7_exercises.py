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



# (2) double digest
# import sequence form ch7 dna.txt. predict fragment lengths of digestion by
# (made-up restriction enzymes) AbcI ANT*AAT and AbcII GCRW*TG, where * 
# represents the position of the cut sites

dir_name = "exercises/chapter_7/"
file_name = "dna.txt"
readstr = dir_name + file_name # read string

# open output file
infile = open(readstr,"r")























