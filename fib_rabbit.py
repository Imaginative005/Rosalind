def fibonacci_rabbits(n, m):
    dp = [0] * m
    dp[0] = 1

    for i in range(2, n + 1):
        new_pairs = sum(dp[:-1])  # Sum of pairs from the last m - 1 months
        dp = [new_pairs] + dp[:-1]  # Shift the values in dp array

    total_pairs = sum(dp)
    return total_pairs

# Read input
n, m = map(int, input().split())

# Calculate and print the result
result = fibonacci_rabbits(91, 16)
print(result)
