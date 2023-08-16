'''
In this version of the program, we open the input file (input.txt) using Python's built-in open function.
We then read the contents of the file using the read method, which returns a single string containing the entire file.
We strip any leading or trailing whitespace from this string using the strip method, and then split it into two lines
using the split method with the newline character \n as the separator. This gives us the two DNA strings s
and t that we want to compare.

We then call the hamming_distance function to compute the Hamming distance between s and t,
and store the result in the variable d. Finally, we print the result to the console using the print function.
Note that this program assumes that the input file contains exactly two lines, each containing a single DNA sequence.
If the input file contains more or less than two lines, or if there is additional information on each line,
you may need to modify the code accordingly to extract the DNA sequences correctly.
'''


def hamming_distance(s, t):
    """
    Computes the Hamming distance between two DNA strings of equal length.
    """
    return sum(1 for i in range(len(s)) if s[i] != t[i])


# Read the input file
with open('rosalind_hamm.txt', 'r') as f:
    s, t = f.read().strip().split('\n')

# Compute the Hamming distance and print the result
d = hamming_distance(s, t)
print(d)
