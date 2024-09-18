# House Robber II
# You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

# You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

# Return the maximum amount of money you can rob without alerting the police.

# Example 1:

# Input: nums = [3,4,3]

# Output: 4
# Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses. The maximum you can rob is nums[1] = 4.

# Example 2:

# Input: nums = [2,9,8,3,6]

# Output: 15
# Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses. The maximum you can rob is nums[1] + nums[4] = 15.

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

from typing import List 

class Solution:
    def route(self, nums: List[int]):
      a = b = 0
      for house in nums:
          a, b = b, max(house + a, b)
      return b
  
    def rob(self, nums: List[int]) -> int:  # Worse than average time on LeetCode.
      if not nums:
        return 0
      if len(nums) == 1:
        return nums[0] 
      route_a = self.route(nums[:-1])
      route_b = self.route(nums[1:])
      return max(route_a, route_b)
      
    def efficientRoute(self, nums: List[int], index: int, end: int):
      a = b = 0
      while index < end:
          a, b = b, max(nums[index] + a, b)
          index += 1
      return b
      
    def robEfficient(self, nums: List[int]) -> int:  # Actually less time efficient than above, even for larger house lists as demonstrated with time-tests below.
        length = len(nums)
        if not nums:
          return 0
        if length == 1:
          return nums[0]
        route_a = self.efficientRoute(nums, 0, length - 1)
        route_b = self.efficientRoute(nums, 1, length)
        return max(route_a, route_b)
        
      
    def robHashmap(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        
        up_to_house = {0: [nums[0], True]}
        if nums[0] > nums[1]: 
          up_to_house[1] = [nums[0], True]
        else:
          up_to_house[1] = [nums[1], False]           
        index = 2
        while index < length:
            print (nums[index])
            if up_to_house[index - 1][0] > up_to_house[index - 2][0] + nums[index]:
              up_to_house[index] = [up_to_house[index - 1][0], up_to_house[index - 1][1]]
            else:
              up_to_house[index] = [up_to_house[index - 2][0] + nums[index], up_to_house[index - 2][1]]
            print (up_to_house[index])
            index += 1
        if up_to_house[length - 1][1] == False: 
            result_a = up_to_house[length - 1][0] 
        else: 
            result_a = up_to_house[length - 2][0]
        print("Result A:", result_a)
        
        down_to_house = {length - 1: [nums[length - 1], True]}
        if nums[length - 1] > nums[length - 2]: 
          down_to_house[length - 2] = [nums[length - 1], True]
        else:
          down_to_house[length - 2] = [nums[length - 2], False]
        print (down_to_house )          
        index = length - 3
        while index >= 0:
            print (nums[index])
            if down_to_house[index + 1][0] > down_to_house[index + 2][0] + nums[index]:
              down_to_house[index] = [down_to_house[index + 1][0], down_to_house[index + 1][1]]
            else:
              down_to_house[index] = [down_to_house[index + 2][0] + nums[index], down_to_house[index + 2][1]]
            print (down_to_house[index])
            index -= 1
        if down_to_house[0][1] == False: 
            result_b = down_to_house[0][0] 
        else: 
            result_b = down_to_house[1][0]
        print("Result B:", result_b)
        
        return max(result_a, result_b)
      
    def robShortenedHashSolution(self, nums: List[int]) -> int:  
        pass
      
    
import random
import time
import timeit

def generate_random_houses(n):
    return [random.randint(0, 100) for _ in range(n)]

def test_functions():
    num_loops = 100
    num_houses = random.randint(0, 100)

    total_time_rob = 0
    total_time_rob_efficient = 0

    timeit_rob = 0
    timeit_rob_efficient = 0
    
    solution = Solution()
    
    for _ in range(num_loops):
        houses = generate_random_houses(num_houses)

        start_time = time.time()
        result_rob = solution.rob(houses)
        end_time = time.time()
        total_time_rob += end_time - start_time

        start_time = time.time()
        result_rob_efficient = solution.robEfficient(houses)
        end_time = time.time()
        total_time_rob_efficient += end_time - start_time

        # You can also add a check to make sure the results are equal
        assert result_rob == result_rob_efficient
        
        timeit_rob += timeit.timeit(lambda: solution.rob(houses), number=1)
        timeit_rob_efficient += timeit.timeit(lambda: solution.robEfficient(houses), number=1)

    average_time_rob = total_time_rob / num_loops
    average_time_rob_efficient = total_time_rob_efficient / num_loops
    timeit_ave_rob = timeit_rob / num_loops
    timeit_ave_rob_efficient = timeit_rob_efficient / num_loops

    print(f"Average time taken by rob: {average_time_rob:.6f} seconds")
    print(f"Average time taken by robEfficient: {average_time_rob_efficient:.6f} seconds")
    print("According to timeit:")
    print(f"Average time taken by rob: {timeit_ave_rob:.6f} seconds")
    print(f"Average time taken by robEfficient: {timeit_ave_rob_efficient:.6f} seconds")

test_functions()
