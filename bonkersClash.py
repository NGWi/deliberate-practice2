#  	Goal
# In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition.

# Write a program outputting all integer partitions of n in reverse lexicographic order.
# Each partition satisfies:
# a1 + a2 + ... + ak = n and a1 >= a2 ... >= ak
# Input
# Read an integer n.
# Output
# Output all integer partitions of n in reverse lexicographic order.
# Constraints
# 1 <= n <= 9
# Example
# Input
# 4
# Output
# 4
# 3 1
# 2 2
# 2 1 1
# 1 1 1 1

def partitions(n):
    def generate_partitions(remaining, max_part, current_partition):
        if remaining == 0:
            # We've found a valid partition, print it
            print(' '.join(map(str, current_partition)))
            return
        
        # Start from the max_part and go down to 1
        for i in range(min(remaining, max_part), 0, -1):
            generate_partitions(remaining - i, i, current_partition + [i])

    # Start generating partitions from n with maximum part n
    generate_partitions(n, n, [])

# Read input
n = int(input())

# Call the function to generate and print partitions
partitions(n)