# -*- coding: utf-8 -*-
"""
Created on Mon May 25 13:41:55 2015

@author: colin
"""

# modules
import os
import re

# (1) binning DNA sequences
# write a program which creates 9 folders, one for sequences between 100 and
# 199 bases long, another for 200-299, etc. write out each DNA sequence in the 
# input files to a separate file in the appropriate folder

# first create 9 folders
# bin100_199
# bin200_299
# bin300_399
# bin400_499
# bin500_599
# bin600-699
# bin700-799
# bin800_899
# bin900_999
for i in range(1,10):
    # build string for os.mkdir() for output directory
    outdirstring = "bin" + str(i) + "00_" + str(i) + "99"
    # if directory already exists, skip the rest of this loop iteration
    if ( os.path.exists(outdirstring) ):
        continue
    os.mkdir(outdirstring)
# end for loop
    
dir_name = "exercises/chapter_9/" # *.dna data files are here

# slight variant of http://stackoverflow.com/questions/2225564/
#        get-a-filtered-list-of-files-in-a-directory
files = [f for f in os.listdir(dir_name) if re.match(r"....dna", f)]
# files is a list of strings
# NOTE: Jones used file_name.endswith(".dna")


# read in each data file and process
counter = 0 # counter for output file names

for file_name in files:

    readstr = dir_name + file_name # read string

    # open each input file
    infile = open(readstr,"r")
    
    # for each line of dna data in current input file
    for line in infile: 
        dna = line.rstrip("\n") # line was read in as text, strip \n
        len_dna = len(dna)
        
        # digit is assumed to be 1,2,3,...,9
        digit = int(len_dna/100) # will be used to sort by len_dna
        
        # begin diagnostic
        if (digit < 1 or digit > 9):
            print("dna length input error")
        # end diagnostic
            
        # build string to directory in which to write dna output, as a function
        # of len_dna    
        outdirstring = "bin" + str(digit) + "00_" + str(digit) + "99/"
        outfile_name = str(counter) + ".dna"
        counter += 1
        writestr = outdirstring + outfile_name
        
        print(writestr) # diagnostic  
        
        # open output file, write,close
        outfile = open(writestr, "w")
        outfile.write(dna)
        outfile.close()

    # end for line
    infile.close()
    
# end for file_name