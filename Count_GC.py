'''

Problem

The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example,
the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is
called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some
labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the
label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx"
denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind
allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute
error below. Sample Dataset

>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output

Rosalind_0808
60.919540


'''


def gc_content(dna_string):
    """
    Calculates the GC-content of a DNA string.
    """
    count = 0
    for symbol in dna_string:
        if symbol == 'G' or symbol == 'C':
            count += 1
    return (count / len(dna_string)) * 100


def parse_fasta(data):
    """
    Parses DNA strings in FASTA format and returns a dictionary
    mapping the ID of each string to its DNA sequence.
    """
    sequences = {}
    current_id = None
    current_sequence = []
    for line in data.split('\n'):
        if line.startswith('>'):
            if current_id is not None:
                sequences[current_id] = ''.join(current_sequence)
            current_id = line[1:]
            current_sequence = []
        else:
            current_sequence.append(line)
    if current_id is not None:
        sequences[current_id] = ''.join(current_sequence)
    return sequences


def highest_gc_content(sequences):
    """
    Returns the ID of the string with the highest GC-content
    and its GC-content as a percentage.
    """
    max_gc_id = None
    max_gc_content = 0
    for seq_id, seq in sequences.items():
        gc = gc_content(seq)
        if gc > max_gc_content:
            max_gc_id = seq_id
            max_gc_content = gc
    return max_gc_id, max_gc_content


# Example usage:
data = '''>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT'''
sequences = parse_fasta(data)
max_gc_id, max_gc_content = highest_gc_content(sequences)
print(max_gc_id)
print(f'{max_gc_content:.6f}')

'''The gc_content function calculates the GC-content of a DNA string by counting the number of 'G' and 'C' symbols 
and dividing it by the length of the string. The result is multiplied by 100 to convert it to a percentage. 

The parse_fasta function parses the DNA strings in FASTA format and returns a dictionary mapping the ID of each 
string to its DNA sequence. It does this by iterating over each line of the input data and keeping track of the 
current ID and sequence. When a new ID is encountered, the previous ID and sequence are added to the dictionary. 

The highest_gc_content function iterates over the sequences dictionary and calculates the GC-content of each string 
using the gc_content function. It keeps track of the ID and GC-content of the string with the highest GC-content seen 
so far. 

The main program reads the input data and passes it to parse_fasta to get a dictionary of sequences. It then calls 
highest_gc_content to get the ID and GC-content of the string with the highest GC-content. Finally, it prints the ID 
and GC-content to the console. 

'''
