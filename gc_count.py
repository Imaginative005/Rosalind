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


# Read input file
with open('rosalind_gc.txt', 'r') as f:
    data = f.read()

# Parse DNA sequences in FASTA format
sequences = parse_fasta(data)

# Find the sequence with the highest GC-content
max_gc_id, max_gc_content = highest_gc_content(sequences)

# Write output file
with open('gc_count_output.txt', 'w') as f:
    f.write(max_gc_id + '\n')
    f.write(f'{max_gc_content:.6f}\n')
