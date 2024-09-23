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
#     def changeMachine(self, coins_arr: list, target: int) -> int:
#       count = 0
#       amount = target
#       print(target)
#       for coin in coins_arr:
#         count += amount // coin
#         amount = amount % coin
#         print(count, amount)
#       return count, amount
#     def coinChange(self, coins: List[int], target: int) -> int:
#       number = len(coins)
#       coins_arr = sorted(coins, reverse=True)
#       for i in range(number):
#         print(coins_arr)
#         count, amount = self.changeMachine(coins_arr, target)
#         print("Result:", count, amount)
#         if amount == 0:
#           return count
#         else:
#           coins_arr.pop(0)
#       return -1
    
    def coinChange(self, coins: List[int], target: int) -> int:
      
      memo = {}
      def results_table(n):
        if n in memo: return memo[n]
        if n == 0: return 0
        if n < 0: return -1
        min_coins = target + 1
        for coin in coins:
          result = results_table(n - coin)
          if result >= 0:
            min_coins = min(min_coins, result + 1)
        if min_coins == target + 1:
          memo[n] = -1  
        else: 
          memo[n] = min_coins
        return memo[n]
      return results_table(target)
    
    def coinChange(self, coins: List[int], target: int) -> int:
      results_table = {0: 0} # Base case: 0 coins needed to make the amount 0
      def get_result(amount: int) -> int: # If results_table[amount] exists, return it. Otherwise, return target + 1, an impossibly high number.
          return results_table.get(amount, target + 1)
      
      for coin in coins:
          for i in range(coin, target + 1):
              # Update results_table(i) with the minimum number of coins, from the ones we've retrieved from the coins list so far, required to make amount i
              so_far = get_result(i)
              new = get_result(i - coin) + 1
              if new < so_far:
                results_table[i] = new

      # If results_table[target] is still target + 1, it means the target amount cannot be made up with the given coins
      result = get_result(target)
      if result == target + 1:
        return -1
      return result
    
    def coinChange(self, coins: List[int], target: int) -> int:
      results_table = {0: 0} # Base case: 0 coins needed to make the amount 0
      def get_result(amount: int) -> int: # If results_table[amount] exists, return it. Otherwise, return target + 1, an impossibly high number.
          return results_table.get(amount, target + 1)
      
      coins = sorted(coins, reverse=True)
      for coin in coins:
          for i in range(coin, target + 1):
              # Update results_table(i) with the minimum number of coins, from the ones we've retrieved from the coins list so far, required to make amount i
              so_far = get_result(i)
              new = get_result(i - coin) + 1
              if new < so_far:
                results_table[i] = new

      # If results_table[target] is still target + 1, it means the target amount cannot be made up with the given coins
      result = get_result(target)
      if result == target + 1:
        return -1
      return result
