# set the values of all the header variables
header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"

# set the values of all the sequence variables
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG"

# make three files to hold the output
output_1 = open(header_1 + ".fasta", "w")
output_2 = open(header_2 + ".fasta", "w")
output_3 = open(header_3 + ".fasta", "w")

# write sequence 1 to output file 1
output_1.write('>' + header_1 + '\n' + seq_1 + '\n')

# write sequence 2 to output file 2
output_2.write('>' + header_2 + '\n' + seq_2.upper() + '\n')

# write sequence 3 to output file 3
output_3.write('>' + header_3 + '\n' + seq_3.replace('-', '') + '\n')

