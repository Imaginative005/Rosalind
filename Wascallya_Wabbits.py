'''

    Wascally Wabbits
    Figure 1. The growth of Fibonacci's rabbit population for the first six months.
    Figure 2. Erosion at Lake Mungo in New South Wales, which was initiated by European rabbits in the 19th Century.
    Courtesy Pierre Pouliquin.

    In 1202, Leonardo of Pisa (commonly known as Fibonacci) considered a mathematical exercise regarding
    the reproduction of a population of rabbits. He made the following simplifying assumptions about the population:

        The population begins in the first month with a pair of newborn rabbits.
        Rabbits reach reproductive age after one month.
        In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
        Exactly one month after two rabbits mate, they produce one male and one female rabbit.
        Rabbits never die or stop reproducing.

    Fibonacci's exercise was to calculate how many pairs of rabbits would remain in one year.
    We can see that in the second month, the first pair of rabbits reach reproductive age and mate. In the third month,
    another pair of rabbits is born, and we have two rabbit pairs; our first pair of rabbits mates again.
    In the fourth month, another pair of rabbits is born to the original pair, while the second pair reach maturity
    and mate (with three total pairs). The dynamics of the rabbit population are illustrated in Figure 1. After a year,
    the rabbit population boasts 144 pairs.

    Although Fibonacci's assumption of the rabbits' immortality may seem a bit farfetched,
    his model was not unrealistic for reproduction in a predator-free environment:
    European rabbits were introduced to Australia in the mid 19th Century, a place with no real
    indigenous predators for them. Within 50 years, the rabbits had already eradicated many
    plant species across the continent, leading to irreversible changes in the Australian ecosystem
    and turning much of its grasslands into eroded, practically uninhabitable parts of the modern Outback
    (see Figure 2). In this problem, we will use the simple idea of counting rabbits to
    introduce a new computational topic, which involves building up large solutions from smaller ones.

Problem

A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat.
Sequences can be finite or infinite. Two examples are the finite sequence (π,−2–√,0,π)
and the infinite sequence of odd numbers (1,3,5,7,9,…). We use the notation an to represent the n

-th term of a sequence.

A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In
the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the
previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal to
the number of rabbits that were alive two months prior. As a result, if Fn represents the number of rabbit pairs
alive after the n-th month, then we obtain the Fibonacci sequence having terms Fn that are defined by the recurrence
relation Fn=Fn−1+Fn−2 (with F1=F2=1

to initiate the sequence). Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over
two millennia ago.

When finding the n -th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation
to generate terms for progressively larger values of n

. This problem introduces us to the computational technique of dynamic programming, which successively builds up
solutions by using the answers to smaller cases.

Given: Positive integers n≤40
and k≤5

.

Return: The total number of rabbit pairs that will be present after n
months, if we begin with 1 pair and in each generation,
every pair of reproduction-age rabbits produces a litter of k

rabbit pairs (instead of only 1 pair).
Sample Dataset

5 3

Sample Output

19


'''


def rabbit_pairs(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit_pairs(n - 1, k) + k * rabbit_pairs(n - 2, k)


n, k = map(int, input("Enter the values of n and k: ").split())
total_pairs = rabbit_pairs(n, k)
print("The total number of rabbit pairs after", n, "months is:", total_pairs)
'''
aboue code for input of n and k
This program defines a function rabbit_pairs that takes two arguments n and k, and returns 
the total number of rabbit pairs after n months, given that each pair of reproduction-age rabbits produces 
a litter of k rabbit pairs. The function uses recursion to calculate the number of rabbit pairs,
 based on the recurrence relation Fn=Fn−1+Fn−2+k.

In the main program, the user is prompted to enter the values of n and k.
 These values are read from the console using the input function, and then converted to integers 
 using the int function and the map function. The rabbit_pairs function is called with these values, 
 and the resulting total number of rabbit pairs is printed to the console using the print function.

'''
'''Sure! Here's an updated version of the program that reads the values of n and k from an input file: Explanation: 
In this updated version, the program first opens an input file named "input.txt" using the open function. The with 
statement is used to ensure that the file is properly closed when the block is exited. 

The values of n and k are then read from the first line of the input file using the readline method, and parsed using 
the split method and the map function. The resulting values are assigned to the variables n and k. 

The rabbit_pairs function is then called with these values to calculate the total number of rabbit pairs, 
which is printed to the console using the print function. 

'''


def rabbit_pairs(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit_pairs(n - 1, k) + k * rabbit_pairs(n - 2, k)


# Open the input file for reading
with open('rosalind_fib.txt', 'r') as input_file:
    # Read the values of n and k from the input file
    n, k = map(int, input_file.readline().strip().split())

# Calculate the total number of rabbit pairs
total_pairs = rabbit_pairs(n, k)

# Print the result to the console
print("The total number of rabbit pairs after", n, "months is:", total_pairs)
