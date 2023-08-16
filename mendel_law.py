'''
Mendel's First Law solved by 18426

Dec. 4, 2012, 2:02 a.m. by Rosalind Team

Topics: Heredity, Probability

    ←
    →

    Introduction to Mendelian Inheritanceclick to expand

Problem Figure 2. The probability of any outcome (leaf) in a probability tree diagram is given by the product of
probabilities from the start of the tree to the outcome. For example, the probability that X is blue and Y is blue is
equal to (2/5)(1/4), or 1/10.

Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random
variable, which is simply a variable that can take a number of different distinct outcomes depending on the result of
an underlying random process.

For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X represent the random
variable corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(
X=red)=35 and Pr(X=blue)=25

.

Random variables can be combined to yield new random variables. Returning to the ball example, let Y model the color
of a second ball drawn from the bag (without replacing the first ball). The probability of Y being red depends on
whether the first ball was red or blue. To represent all outcomes of X and Y, we therefore use a probability tree
diagram. This branching diagram represents all possible individual probabilities for X and Y

, with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of
probabilities along the path from the beginning of the tree; see Figure 2 for an illustrative example.

An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be
written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A be the event
"Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red
and Y=blue), or 310+110=25

(see Figure 2 above).

Given: Three positive integers k , m, and n, representing a population containing k+m+n organisms: k individuals are
homozygous dominant for a factor, m are heterozygous, and n

are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant
allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate. Sample Dataset

2 2 2

Sample Output

0.78333

'''


def probability_dominant_allele(k, m, n):
    total_pop = k + m + n

    # Probability of selecting homozygous dominant individuals
    prob_kk = (k / total_pop) * ((k - 1) / (total_pop - 1))

    # Probability of selecting heterozygous individuals
    prob_km = (k / total_pop) * (m / (total_pop - 1)) + (m / total_pop) * (k / (total_pop - 1))

    # Probability of selecting homozygous recessive individuals
    prob_nn = (n / total_pop) * ((n - 1) / (total_pop - 1))

    # Probability of selecting a dominant allele from the selected individuals
    prob_dominant_allele = 1 - prob_nn - 0.25 * prob_km - 0.5 * prob_kk

    return prob_dominant_allele


# Reading input from file
with open("rosalind_iprb.txt", "r") as f:
    k, m, n = map(int, f.readline().strip().split())

# Calculating probability of dominant allele
prob = probability_dominant_allele(k, m, n)

# Writing output to file
with open("mendel_prob_output.txt", "w") as f:
    f.write(str(prob))
# Code explaination:
'''
In this code, the probability_dominant_allele function takes in the values of k, m, and n, 
and returns the probability of two randomly selected mating organisms producing an 
individual possessing a dominant allele. 
This function is used to solve the problem by reading the input values from a file named input.txt, 
calculating the probability, and then writing the output value to a file named output.txt.

The input file should contain three positive integers k, m, and n, separated by spaces, 
representing a population containing k individuals that are homozygous dominant, 
m individuals that are heterozygous, and n individuals that are homozygous recessive.



'''