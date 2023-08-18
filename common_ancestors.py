def generate_profile_matrix(dna_strings):
    profile = {'A': [0] * len(dna_strings[0]),
               'C': [0] * len(dna_strings[0]),
               'G': [0] * len(dna_strings[0]),
               'T': [0] * len(dna_strings[0])}

    for dna_string in dna_strings:
        for i, symbol in enumerate(dna_string):
            profile[symbol][i] += 1

    return profile

def generate_consensus_string(profile):
    consensus = []
    for i in range(len(profile['A'])):
        max_count = 0
        max_symbol = ''
        for symbol in ['A', 'C', 'G', 'T']:
            if profile[symbol][i] > max_count:
                max_count = profile[symbol][i]
                max_symbol = symbol
        consensus.append(max_symbol)
    
    return ''.join(consensus)

# Read input from the DNA text file
input_file = "rosalind_cons.txt"
with open(input_file, "r") as f:
    lines = f.readlines()

# Extract DNA sequences from FASTA format
dna_strings = []
current_dna = ''
for line in lines:
    if line.startswith(">"):
        if current_dna:
            dna_strings.append(current_dna)
            current_dna = ''
    else:
        current_dna += line.strip()
if current_dna:
    dna_strings.append(current_dna)

# Generate profile matrix and consensus string
profile_matrix = generate_profile_matrix(dna_strings)
consensus = generate_consensus_string(profile_matrix)

# Save results to the output file
output_file = "common_ancestors.txt"
with open(output_file, "w") as f:
    f.write(consensus + '\n')
    for symbol in ['A', 'C', 'G', 'T']:
        f.write(f"{symbol}: {' '.join(map(str, profile_matrix[symbol]))}\n")

# print("Output saved to", output_file)
