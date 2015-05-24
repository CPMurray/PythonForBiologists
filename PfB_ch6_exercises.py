# -*- coding: utf-8 -*-
"""
Created on Sun May 24 12:14:10 2015

@author: colin
"""

# chapter 6 exercise: conditional tests: individual test comments inside loop

# fucntion calculating AT content
#   AT content = (#A's + #T's)/stringlength
def get_at_content(dna):
    numA = dna.upper().count("A")
    numT = dna.upper().count("T")
    len_dna = len(dna)

    return ((numA+numT)/len_dna)

# input data is csv with fields species name, sequence,
# gene name, expression level
dir_name = "exercises/chapter_6/"
file_name = "data.csv"
readstr = dir_name + file_name # read string

# open output file
infile = open(readstr,"r")

# cycle through each line, perform calculations
for line in infile: 
    line = line.rstrip("\n") # line was read in as text, strip \n
    data_record = line.split(sep=",") # data_record is a list
    species_name = data_record[0]
    gene_sequence = data_record[1]
    gene_name = data_record[2]
    gene_expression_level = int(data_record[3])
    
    # (1) several species
    # print out the gene names for all genes belonging to 
    # Drosophila melanogaster or Drosophila simulans
#    if (species_name == "Drosophila melanogaster" or
#    species_name == "Drosophila simulans"):
#        print(gene_name)
        
    # (2) length range
    # print out the gene names for all genes between 90 and 110 bases long
#    gene_length = len(gene_sequence)
#    if (gene_length > 90 and gene_length < 110):
#         print(gene_name)
        
    # (3) AT content
    # print out the gene names for all genes whose AT content is less than 0.5
    # and whose expression level is greater than 200
#    print(gene_name," AT content ",get_at_content(gene_sequence), " expr ",
#          gene_expression_level)
#    if ( get_at_content(gene_sequence) < 0.5 and gene_expression_level > 200 ):
#        print(gene_name)
    
    # (4) complex condition
    # print out the gene names for all genes whose name begins with "k" or "h"
    # except those belonging to Drosophila melanogaster
#    if ( (gene_name.startswith("k") or gene_name.startswith("h")) and 
#    (species_name != "Drosophila melanogaster") ):
#        print(gene_name)
        
    # (5) high low medium AT content
    # for each gene, print out a message giving the gene name and saying 
    # whether its AT content is high ( > 0.65), low ( < 0.45), or 
    # medium ( between 0.45 and 0.65)
    if ( get_at_content(gene_sequence) > 0.65 ):
        print(gene_name, " HIGH")
    elif ( get_at_content(gene_sequence) < 0.45 ):
        print(gene_name, " LOW")
    else :
        print(gene_name, " MEDIUM")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

