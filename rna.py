# [new_item for item in list]
'''
def rna_transcribe(codon):
    condon_string = ""
    for n in codon:
        if n == "T":
            condon_string = codon.replace("T", "U")
        else:
            condon_string = codon.join(n)
    return condon_string

'''
# OR
with open("rosalind_rna.txt") as dna:
    dna_code = dna.readline()
    print(f'The dna code: {dna_code}')


def rna(code):
    return code.replace("T", "U")


print(f'RNA code: {rna(dna_code)}')
# print(len("GATGGAACTTGACTACGTAAATT"))
# print(rna_transcribe("GATGGAACTTGACTACGTAAATT"))

