# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:19:44 2015

@author: colin
"""

###################################################################
# (2) write a program that will calculate the number of all kmers of a given
# length across all DNA sequences in the input files and display just the ones
# that occur more than a give number of times. Your program should take two 
# command line arguments - the kmer length and the cutoff number

# modules    
import sys
import os
import re
import copy 

# command-line input, ex "python PfB_ch9_KMERcount.py 3 5"
k = int( sys.argv[1] ) # k-mer length
cutoff = int( sys.argv[2] ) # k-mer appearance frequency > cutoff --> display

# begin diagnostic
print("k ", k)
print("cutoff ", cutoff)
# end diagnostic

dir_name = "exercises/chapter_9/" # *.dna data files are here

# slight variant of http://stackoverflow.com/questions/2225564/
#        get-a-filtered-list-of-files-in-a-directory
files = [f for f in os.listdir(dir_name) if re.match(r"....dna", f)]
# files is a list of strings
# NOTE: Jones used file_name.endswith(".dna")

# instantiate dictionary, key = kmer, value = number occurrences
kmersdict = {} 

# read in each data file and process
for file_name in files:

    readstr = dir_name + file_name # read string

    # open each input file
    infile = open(readstr,"r")
    
    # for each line of dna data in current input file
    for line in infile: # implicit read
        dna = line.rstrip("\n") # line was read in as text, strip \n
        len_dna = len(dna)
        
        # for dna, cycle through indices to consider all possible k-mers
        # first check if a k-mer is a key in kmers dict, if not add it with
        # (count) value 1, if it is there already, increment the count;
        # note that there are len_dna - k + 1 k-mers in dna of length len_dna
        for i in range(len_dna - k + 1):
            kmer = dna[i:i+k] # subset kmer out of dna
            
            # from http://stackoverflow.com/questions/1692388/
# python-list-of-dict-if-exists-increment-a-dict-value-if-not-append-a-new-dic
            kmersdict[kmer] = kmersdict.get(kmer, 0) + 1
                            
    # end for line
    infile.close()
    
# end for file_name
    
# make deepcopy of kmersdict to .pop, b/c you can't remove items from dict
# while iterating over it
# https://docs.python.org/3.4/library/copy.html#copy.deepcopy
kmersdict_cutoff = copy.deepcopy(kmersdict)

for kmer in kmersdict.keys(): # for every kmer key
    if kmersdict.get(kmer) <= cutoff: # if not > than cutoff, delete item
        kmersdict_cutoff.pop(kmer)

for kmer in sorted(kmersdict_cutoff.keys()):
    print( kmer + " : " + str( kmersdict_cutoff.get(kmer) ) )

#########################################################
# example, successful test case; compared to book p.229
#python PfB_ch9_KMERcount.py 6 25                                  
#k  6
#cutoff  25
#agagat : 26
#agcggg : 26
#ccggtt : 26
#gagtgg : 28
#ggacgt : 27
#ttctga : 26