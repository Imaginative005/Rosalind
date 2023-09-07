from collections import defaultdict

def count_4mers(s):
    k = 4  # Set the value of k to 4
    kmer_counts = defaultdict(int)  # Use a dictionary to store counts

    # Iterate through the DNA string and count 4-mers
    for i in range(len(s) - k + 1):
        kmer = s[i:i + k]  # Extract the 4-mer
        kmer_counts[kmer] += 1  # Increment the count for this 4-mer

    # Create a list of counts in lexicographic order
    counts = [kmer_counts[kmer] for kmer in sorted(kmer_counts.keys())]

    return counts

# Input DNA string
s = """
CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG
"""

# Remove newline characters and other whitespace
s = s.replace('\n', '').replace('\r', '').replace(' ', '')

# Call the function to count 4-mers
result = count_4mers(s)

# Print the result as space-separated values
print(' '.join(map(str, result)))
