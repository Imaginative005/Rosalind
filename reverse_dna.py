import pandas

'''
def reverse_complement(s):
    complement = {"A": 'T', "C": 'G', "G": 'C', "T": 'A'}
    # return ''.join([complement[base] for base in s[::-1]])
    # new_list = [new_item for item in list if test]
    new_complement = [base for base in s if base in s[::-1]]
    new_str_dna = ''
    if new_complement:
        new_str_dna += str(new_complement)
    return new_str_dna


with open("rosalind_revc.txt", mode="r") as dna_f:
    dna_file = dna_f.read()
    # dna_string = pandas.Series(dna_file)
    # new_dict = dna_string.to_dict()
    print(f'The original DNA: {dna_file}')
    # print(dna_string)
    # print(new_dict)

# dna_string = "ACTGCTAGCT"
rev_dna = reverse_complement(dna_file)
reverse_dna = ''.join(rev_dna)
# print(reverse_dna)
# rev_dna = reverse_complement(new_dict)
# new_str = ''.join(str(rev_dna))
print(f'The reverse dna: {reverse_dna}')
'''

'''
Sure, here's an updated version of the code that reads the DNA string from an input file:

python

def reverse_complement(dna_string):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_complement_string = ''
    for nucleotide in dna_string[::-1]:
        reverse_complement_string += complement_dict[nucleotide]
    return reverse_complement_string

# Open the input file for reading
with open('input.txt', 'r') as input_file:
    # Read the DNA string from the input file
    dna_string = input_file.read().strip()

# Get the reverse complement of the DNA string
reverse_complement_string = reverse_complement(dna_string)

# Print the reverse complement to the console
print("The reverse complement of the DNA string is:", reverse_complement_string)

In this updated version, the program first opens an input file named "input.txt" using the open function. The with 
statement is used to ensure that the file is properly closed when the block is exited. 

The DNA string is then read from the input file using the read method and stripped of any leading or trailing 
whitespace using the strip method. 

The reverse_complement function is then called with the DNA string as its argument to obtain the reverse complement 
string, which is printed to the console using the print function. 
'''


def reverse_complement(dna_string):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_complement_string = ''
    for nucleotide in dna_string[::-1]:
        reverse_complement_string += complement_dict[nucleotide]
    return reverse_complement_string


# Open the input file for reading
with open('rosalind_revc.txt', 'r') as input_file:
    # Read the DNA string from the input file
    dna_string = input_file.read().strip()

# Get the reverse complement of the DNA string
reverse_complement_string = reverse_complement(dna_string)

# Print the reverse complement to the console
print("The reverse complement of the DNA string is:", reverse_complement_string)
