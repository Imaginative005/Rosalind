'''
Counting Point Mutations


Topics: Alignment

    ←
    →

    Evolution as a Sequence of Mistakesclick to expand

Problem
Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.

Given two strings s
and t of equal length, the Hamming distance between s and t, denoted dH(s,t),
is the number of corresponding symbols that differ in s and t


. See Figure 2.

Given: Two DNA strings s
and t

of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)

.
Sample Dataset

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output

7

'''

def hamming_distance(s, t):
    """
    Computes the Hamming distance between two DNA strings of equal length.
    """
    return sum(1 for i in range(len(s)) if s[i] != t[i])

# Example usage
s = 'GAGCCTACTAACGGGAT'
t = 'CATCGTAATGACGGCCT'
d = hamming_distance(s, t)
print(d)

'''
Explanation:
The hamming_distance function takes two DNA strings s and t as input and returns their Hamming distance. 
It works by iterating over the indices of the strings using the range function, 
and counting the number of times the symbols at each index differ between s and t. 
This count is then returned as the Hamming distance.

In the example usage above, we set the values of s and t to the example input strings from the problem, and call the hamming_distance function to compute their Hamming distance. The result is printed to the console.
'''