# # Coin Change
# You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

# Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

# You may assume that you have an unlimited number of each coin.

# Example 1:

# Input: coins = [1,5,10], amount = 12

# Output: 3
# Explanation: 12 = 10 + 1 + 1. Note that we do not have to use every kind coin available.

# Example 2:

# Input: coins = [2], amount = 3

# Output: -1
# Explanation: The amount of 3 cannot be made up with coins of 2.

# Example 3:

# Input: coins = [1], amount = 0

# Output: 0
# Explanation: Choosing 0 coins is a valid way to make up 0.

# Constraints:

# 1 <= coins.length <= 10
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10000
class Solution:
    def changeMachine(self, coins_arr: list, target: int) -> int:
      count = 0
      amount = target
      print(target)
      for coin in coins_arr:
        count += amount // coin
        amount = amount % coin
        print(count, amount)
      return count, amount
    def coinChange(self, denominations: List[int], target: int) -> int:
      number = len(denominations)
      coins_arr = sorted(denominations, reverse=True)
      for i in range(number):
        print(coins_arr)
        count, amount = self.changeMachine(coins_arr, target)
        print("Result:", count, amount)
        if amount == 0:
          return count
        else:
          coins_arr.pop(0)
      return -1
    
    def coinChange(self, denominations: List[int], target: int) -> int:
      memo = {}
      def dp(n):
        if n in memo: return memo[n]
        if n == 0:
          return 0
        if n < 0:
          return -1
        min_coins = target + 1
        for coin in denominations:
          res = dp(n - coin)
          if res >= 0:
            min_coins = min(min_coins, res + 1)
        memo[n] = -1 if min_coins == target + 1 else min_coins
        return memo[n]
      return dp(target)
