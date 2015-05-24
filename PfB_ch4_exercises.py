# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:59:50 2015

@author: colin
"""

# (1) processing DNA in a file
# read lines of seq from file; trim 14 base adapter from start
# write cleaned sequences to a new file and print lengths to screen

dir_name = "exercises/chapter_4/"
file_name = "input.txt"
readstr = dir_name + file_name # read string

# open output file
outfile = open("trimmed.txt","w")

# read data
infile = open(readstr) # open file; create file object
for sequence in infile:
    len_seq = len(sequence) # find length for last index
    # strip 14-base adapter and newline
    sequence = sequence[14:len_seq].rstrip("\n") 
    print(sequence)
    outfile.write(sequence + "\n")

# cleanup
infile.close()
outfile.close() 

#################################################################
# (2) multiple exons from genomic DNA
# expect two input files 
#   -1 genomic_dna.txt: single sequence
#   -2 exons.txt: multiple integer pairs x,y start, stop positions
# extract the exon sections, concatenate, and write to file

print("\n") # to separate screen output of two exercises

# read in dna data
dir_name = "exercises/chapter_4/"
file_name = "genomic_dna.txt"
readstr = dir_name + file_name # read string
infile = open(readstr)
dna = infile.read().rstrip("\n")
infile.close()

# open output file
outfile_name = "coding_sequence.txt"
# write output to working dir, not data dir
outfile = open(outfile_name,"w") 

# read in exon start, stop position integer pairs
file_name = "exons.txt"
readstr = dir_name + file_name # read string
infile = open(readstr)
for line in infile: # read each line
    line = line.rstrip("\n") # line was read in as text, strip \n
    # exonStSt -> exon start and stop positions
    # make assumption that pairs of positions are already sorted
    exonStSt = line.split(sep=",") # 2 element list of char's
    start = int(exonStSt[0]) # deliberate type change
    stop = int(exonStSt[1])  # char to int
    print( "start " + str(start) )
    print( "stop " + str(stop) + "\n" )
    
    # extract exon from dna
    # note that author defines stop position as first element
    # that is NOT in exon, not the last element in exon
    exon = dna[start:stop] # exon fragment
    
    # write to output; NO "\n" b/c we want to concatenate inside
    # outputfile
    outfile.write(exon)    
    
# cleanup
infile.close()
outfile.close()
    
























