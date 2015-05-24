# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:15:03 2015

@author: colin
"""

# (1) calculating AT content
#   AT content = (#A's + #T's)/stringlength
dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
numA = dna.count("A")
numT = dna.count("T")
len_dna = len(dna)
print("AT content problem")
print("AT content = ",str( (numA+numT)/len_dna) )

# (2) complementing DNA
dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

dna_c = dna.replace("A","t") # dna_c -> complement of dna
dna_c = dna_c.replace("T","a")
dna_c = dna_c.replace("G","c")
dna_c = dna_c.replace("C","g")
dna_c = dna_c.upper()
print("\nreverse complement problem")
print(dna)
print(dna_c)

# (3) restriction fragment lengths: calculate size of two frag
dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
# EcoRI G*AATTC recognition site, * is where cut is made
EcoRI_si = dna.find("GAATTC") # si -> start index of recog site
# the cut should occur between elements dna[EcoRI_si] and 
#   dna[EcoRI_si + 1]
len_dna = len(dna)
# indexing starts at zero, inclusive at start, exlusive at end
print("\nEcoRI restriction fragment lengths")
print("length of first fragment: ", str(EcoRI_si + 1))
print("length of second fragment: ", str(len_dna - (EcoRI_si + 1) ) )

# (4) splicing out introns, part 1
dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
# dna contains two exons and an intron
# exon 1: start to 63rd character
# exon 2: 91rst character to end
# print just the coding region of dna
len_dna = len(dna)
print("\nsplicing out introns, part 1")
exon_1 = dna[0:63]
exon_2 = dna[90:len_dna]
print(exon_1 + exon_2)

# (5) splicing out introns, part 2
# calculate the percentage of dna that is coding
print(str( 100*(len(exon_1) + len(exon_2))/len_dna ))

# (6) splicing out introns, part 3
# print out the original dna sequence with coding bases in
#   uppercase and non-coding bases in lowercase

print(dna[0:63] + dna[63:90].lower() + dna[90:len_dna])














