'''In this version of the program, we open two input files (input1.txt and input2.txt) using Python's built-in open
function. We then read the first line of each file using the readline method, and strip any leading or trailing
whitespace using the strip method. This gives us the two DNA strings s and t that we want to compare.

We then call the hamming_distance function to compute the Hamming distance between s and t, and store the result in
the variable d. Finally, we print the result to the console using the print function.

Note that this program assumes that the input files contain only one line of DNA sequence each, with no additional
information. If the input files contain more than one line, or if there is additional information on each line,
you may need to modify the code accordingly to extract the DNA sequences correctly.


'''


def hamming_distance(s, t):
    """
    Computes the Hamming distance between two DNA strings of equal length.
    """
    return sum(1 for i in range(len(s)) if s[i] != t[i])


# Read the input files
with open('input1.txt', 'r') as f1, open('input2.txt', 'r') as f2:
    s = f1.readline().strip()
    t = f2.readline().strip()

# Compute the Hamming distance and print the result
d = hamming_distance(s, t)
print(d)
