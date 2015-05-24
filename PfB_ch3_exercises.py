# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:01:44 2015

@author: colin
"""

# (1) splitting genomic dna
# split genomic_dna into coding and non-coding parts and write
# to output files

# initial literal values
dir_name = "exercises/chapter_3/"
file_name = "genomic_dna.txt"
readstr = dir_name + file_name # read string

# read data
infile = open(readstr) # open file; create file object
dna = infile.read().rstrip("\n")
infile.close()

# splice out intron and exons
len_dna = len(dna)
exon_1 = dna[0:63]
intron_1 = dna[63:90]
exon_2 = dna[90:len_dna]

# open output files, write output, close
file_name = "coding_dna.txt"
outfile = open(file_name,"w")
outfile.write(dna[0:63] + dna[90:len_dna])
outfile.close()

file_name = "noncoding_dna.txt"
outfile = open(file_name,"w")
outfile.write(dna[63:90])
outfile.close()

# (2) writing a FASTA file
# set the values of all the header variables
header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"

# set the values of all the sequence variables
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG"

file_name = "sequences.fasta"
outfile = open(file_name,"w")

outfile.write( ">" + header_1 + "\n")
outfile.write( seq_1.upper() + "\n")

outfile.write( ">" + header_2 + "\n")
outfile.write( seq_2.upper() + "\n")

outfile.write( ">" + header_3 + "\n")
outfile.write( seq_3.replace("-","").replace("—","") )

outfile.close()

# (3) writing multiple FASTA files
outfile_name1 = header_1 + ".fasta"
outfile_name2 = header_2 + ".fasta"
outfile_name3 = header_3 + ".fasta"

outfile1 = open(outfile_name1,"w")
outfile1.write( ">" + header_1 + "\n")
outfile1.write( seq_1.upper() + "\n")
outfile1.close()

outfile2 = open(outfile_name2,"w")
outfile2.write( ">" + header_2 + "\n")
outfile2.write( seq_2.upper() + "\n")
outfile2.close()

outfile3 = open(outfile_name3,"w")
outfile3.write( ">" + header_3 + "\n")
outfile3.write( seq_3.replace("-","").replace("—","") )
outfile3.close()



















