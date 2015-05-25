# -*- coding: utf-8 -*-
"""
Created on Mon May 25 10:22:28 2015

@author: colin
"""

# DNA translation
# Write a program tht will translate a DNA sequence into protein. Your program
# should use the standard genetic code fount at 
# http://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=tgencodes#SG1
#TTT F Phe      TCT S Ser      TAT Y Tyr      TGT C Cys  
#TTC F Phe      TCC S Ser      TAC Y Tyr      TGC C Cys  
#TTA L Leu      TCA S Ser      TAA * Ter      TGA * Ter  
#TTG L Leu i    TCG S Ser      TAG * Ter      TGG W Trp  
#
#CTT L Leu      CCT P Pro      CAT H His      CGT R Arg  
#CTC L Leu      CCC P Pro      CAC H His      CGC R Arg  
#CTA L Leu      CCA P Pro      CAA Q Gln      CGA R Arg  
#CTG L Leu i    CCG P Pro      CAG Q Gln      CGG R Arg  
#
#ATT I Ile      ACT T Thr      AAT N Asn      AGT S Ser  
#ATC I Ile      ACC T Thr      AAC N Asn      AGC S Ser  
#ATA I Ile      ACA T Thr      AAA K Lys      AGA R Arg  
#ATG M Met i    ACG T Thr      AAG K Lys      AGG R Arg  
#
#GTT V Val      GCT A Ala      GAT D Asp      GGT G Gly  
#GTC V Val      GCC A Ala      GAC D Asp      GGC G Gly  
#GTA V Val      GCA A Ala      GAA E Glu      GGA G Gly  
#GTG V Val      GCG A Ala      GAG E Glu      GGG G Gly  

# function to translate DNA
# input: string of nucleotides
# output: string of amino acid residues
def translate_dna(dna):
    
    # dictionary containing the canonical genetic code
    genetic_code = {    # NOTE: Jones says put outside function so dict
    'TTT' : 'F', # Phe  # doesn't have to be recreated each time fn called
    'TTC' : 'F', # Phe      
    'TTA' : 'L', # Leu     
    'TTG' : 'L', # Leu i
    'TCT' : 'S', # Ser
    'TCC' : 'S', # Ser
    'TCA' : 'S', # Ser
    'TCG' : 'S', # Ser
    'TAT' : 'Y', # Tyr
    'TAC' : 'Y', # Tyr
    'TAA' : '*', # Ter
    'TAG' : '*', # Ter
    'TGT' : 'C', # Cys
    'TGC' : 'C', # Cys
    'TGA' : '*', # Ter
    'TGG' : 'W', # Trp
    'CTT' : 'L', # Leu
    'CTC' : 'L', # Leu
    'CTA' : 'L', # Leu
    'CTG' : 'L', # Leu i
    'CCT' : 'P', # Pro
    'CCC' : 'P', # Pro
    'CCA' : 'P', # Pro
    'CCG' : 'P', # Pro
    'CAT' : 'H', # His
    'CAC' : 'H', # His
    'CAA' : 'Q', # Gln
    'CAG' : 'Q', # Gln
    'CGT' : 'R', # Arg
    'CGC' : 'R', # Arg
    'CGA' : 'R', # Arg
    'CGG' : 'R', # Arg
    'ATT' : 'I', # Ile
    'ATC' : 'I', # Ile
    'ATA' : 'I', # Ile
    'ATG' : 'M', # Met i
    'ACT' : 'T', # Thr
    'ACC' : 'T', # Thr
    'ACA' : 'T', # Thr
    'ACG' : 'T', # Thr
    'AAT' : 'N', # Asn
    'AAC' : 'N', # Asn
    'AAA' : 'K', # Lys
    'AAG' : 'K', # Lys
    'AGT' : 'S', # Ser
    'AGC' : 'S', # Ser
    'AGA' : 'R', # Arg
    'AGG' : 'R', # Arg
    'GTT' : 'V', # Val
    'GTC' : 'V', # Val
    'GTA' : 'V', # Val
    'GTG' : 'V', # Val
    'GCT' : 'A', # Ala
    'GCC' : 'A', # Ala
    'GCA' : 'A', # Ala
    'GCG' : 'A', # Ala 
    'GAT' : 'D', # Asp
    'GAC' : 'D', # Asp
    'GAA' : 'E', # Glu
    'GAG' : 'E', # Glu
    'GGT' : 'G', # Gly 
    'GGC' : 'G', # Gly
    'GGA' : 'G', # Gly
    'GGG' : 'G'  # Gly
    } # end dict definition
    
    # preprocess input
    dna = dna.upper()
    
    # start by translating the first 3 nucleotides, then reiterate until done
    # if string length not divisible by 3, 'short codons' at end will not be
    # translated
    protein = [] # instantiate list for amino acid residues
    len_dna = len(dna)
    
    # begin diagnostic
    print("len_dna ", len_dna)
    print("dna ", dna)
    # end diagnostic
    
    for index in range(0,len_dna,3):
        codon = dna[index:index+3]
        #print(codon) # diagnostic
        
        # only translate complete 3-nt codons
        if (len(codon) != 3): 
            break # exit loop (ok b/c would be at end of sequence anyway)
        
        # if codon not in dict, return 'X' for unknown residue
        protein.append( genetic_code.get(codon,'X') )
    
    return ''.join(protein) # return concatenation of list contents   
    
# end function definition

# make assertions from Jones' test cases
assert translate_dna("ATGTTCGGT") == "MFG"
assert translate_dna("ATCGATCGATCGTTGCTTATCGATCAG") == "IDRSLLIDQ"
assert translate_dna("actgatcgtagcttgcttacgtatcgtat") == "TDRSLLTYR"
assert translate_dna("ACGATCGATCGTNACGTACGATCGTACTCG") == "TIDRXVRSYS"

# Jones' test cases
print( translate_dna("ATGTTCGGT"), "\n" )
print( translate_dna("ATCGATCGATCGTTGCTTATCGATCAG"), "\n" )
print( translate_dna("actgatcgtagcttgcttacgtatcgtat"), "\n" ) 
print( translate_dna("ACGATCGATCGTNACGTACGATCGTACTCG"), "\n" )