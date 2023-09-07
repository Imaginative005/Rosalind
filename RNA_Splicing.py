# Define the genetic code as a dictionary
genetic_code = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
    "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

# Read input DNA string and intron sequences from FASTA format
with open("rosalind_splc_second_file.txt") as file:
    lines = file.readlines()

dna_string = ""
introns = []

for line in lines:
    if line.startswith(">"):
        continue
    if dna_string == "":
        dna_string = line.strip()
    else:
        introns.append(line.strip())

# Remove introns from the DNA string
for intron in introns:
    dna_string = dna_string.replace(intron, "")

# Transcribe DNA to RNA
rna_string = dna_string.replace("T", "U")

# Translate RNA into a protein string
protein_string = ""
for i in range(0, len(rna_string), 3):
    codon = rna_string[i:i+3]
    if codon in genetic_code:
        amino_acid = genetic_code[codon]
        if amino_acid == "Stop":
            break
        protein_string += amino_acid

# Print the protein string
print(protein_string)
