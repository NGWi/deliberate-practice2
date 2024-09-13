# # Climbing Stairs
# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

# Return the number of distinct ways to climb to the top of the staircase.

# Example 1:

# Input: n = 2

# Output: 2
# Explanation:

# 1 + 1 = 2
# 2 = 2
# Example 2:

# Input: n = 3

# Output: 3
# Explanation:

# 1 + 1 + 1 = 3
# 1 + 2 = 3
# 2 + 1 = 3
# Constraints:

# 1 <= n <= 30

class Solution:
    def climbStairs(self, n: int) -> int:
      if n <= 3: # Or 2
        return n
      else:
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairsV2(self, n: int) -> int:
      if n <= 3: # Or 2
        return n
      else:
        a = 2
        b = 3
        for i in range(3, n): # Or (2,..) if 2 above.
          c = a + b
          a = b
          b = c
        return b