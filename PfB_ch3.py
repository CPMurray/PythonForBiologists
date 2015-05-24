# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:07:55 2015

@author: colin
"""
dir_name = "exercises/chapter_3/"
file_name = "dna.txt"
readstr = dir_name + file_name # read string

file_obj = open(readstr) # open file; create file object

#dna = file_obj.read()
#dna = dna.rstrip() # strip newline
dna = file_obj.read().rstrip("\n")
file_obj.close()

dna_len = len(dna)
print("sequence is " + dna + " and length is " + str(dna_len))