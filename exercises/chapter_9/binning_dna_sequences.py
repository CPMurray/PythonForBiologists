import os


for bin_lower in range(100,1000,100):
    bin_upper = bin_lower + 99
    bin_folder_name = str(bin_lower) + "_" + str(bin_upper)
    os.mkdir(bin_folder_name)

seq_number = 1
for file_name in os.listdir("."):
    if file_name.endswith(".dna"):
        print("reading sequences from " + file_name)
        dna_file = open(file_name)
        for line in dna_file:
            dna = line.rstrip("\n")
            length = len(dna)
            print("sequence length is " + str(length))
            for bin_lower in range(100,1000,100):
                bin_upper = bin_lower + 99
                if length >= bin_lower and length < bin_upper:
                    print("bin is " + str(bin_lower) + " to " + str(bin_upper))
                    bin_folder_name = str(bin_lower) + "_" + str(bin_upper)
                    output_path = bin_folder_name + '/' + str(seq_number) + '.dna'
                    output = open(output_path, "w")
                    output.write(dna)
                    output.close()
                    seq_number = seq_number+1

