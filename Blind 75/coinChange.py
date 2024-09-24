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

from typing import List 

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
    
    def change (self, coins: List[int], target: int) -> int:
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
    
    def changeSorted (self, coins: List[int], target: int) -> int:
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

import random
import time
import timeit

def generate_random_coins(n):
    return [random.randint(1, 2**31) for _ in range(n)]

def test_functions():
    num_loops = 100
    num_coins = random.randint(1, 50) # For < 50 or amount < 10 mil., there is no advantage to sorting, on average.
    target = random.randint(1, 10000000)

    total_time_change = 0
    total_time_change_sorted = 0

    timeit_change = 0
    timeit_change_sorted = 0
    
    solution = Solution()
    
    for _ in range(num_loops):
        coins = generate_random_coins(num_coins)

        start_time = time.time()
        result_change = solution.change(coins, target)
        end_time = time.time()
        total_time_change += end_time - start_time

        start_time = time.time()
        result_change_sorted = solution.changeSorted(coins, target)
        end_time = time.time()
        total_time_change_sorted += end_time - start_time

        assert result_change == result_change_sorted
        
        timeit_change += timeit.timeit(lambda: solution.change(coins, target), number=1)
        timeit_change_sorted += timeit.timeit(lambda: solution.changeSorted(coins, target), number=1)

    average_time_change = total_time_change / num_loops
    average_time_change_sorted = total_time_change_sorted / num_loops
    timeit_ave_change = timeit_change / num_loops
    timeit_ave_change_sorted = timeit_change_sorted / num_loops

    print(f"Average time taken by change: {average_time_change:.6f} seconds")
    print(f"Average time taken by changeSorted: {average_time_change_sorted:.6f} seconds")
    print("According to timeit:")
    print(f"Average time taken by change: {timeit_ave_change:.6f} seconds")
    print(f"Average time taken by changeSorted: {timeit_ave_change_sorted:.6f} seconds")

test_functions()