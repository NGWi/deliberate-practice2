# Maximum Subarray
# Given an array of integers nums, find the subarray with the largest sum and return the sum.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [2,-3,4,-2,2,1,-1,4]

# Output: 8
# Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

# Example 2:

# Input: nums = [-1]

# Output: -1
# Constraints:

# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000

from typing import List
from functools import reduce
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      max_sum = max(nums)
      current_sum = nums[0]
      
      for num in nums[1:]:
          if current_sum < 0:
              current_sum = 0
          current_sum += num
          if current_sum > max_sum:
              max_sum = current_sum
      
      return max_sum    
# Better memory, slower.
    def maxSubArray2(self, nums: List[int]) -> int:
      max_sum = current_sum = nums[0]
      
      for num in nums[1:]:
          current_sum = max(num, current_sum + num)
          max_sum = max(max_sum, current_sum)
      
      return max_sum
    
    
    def maxSubArray3(self, nums: List[int]) -> int:
      max_sum = current_sum = nums[0]
      
      for num in nums[1:]:
          if current_sum < 0:
              current_sum = 0
          current_sum += num
          if current_sum > max_sum:
              max_sum = current_sum
      
      return max_sum      

    def maxSubArray4(self, nums: List[int]) -> int:
      max_sum = current_sum = nums[0]
      
      for num in nums[1:]:
          if current_sum < 0:
              current_sum = 0
          current_sum += num
          max_sum = max(max_sum, current_sum)
      
      return max_sum
    
    def maxSubArray5(self, nums: List[int]) -> int:
        sums = reduce(lambda sums, num: (max(sums[0], sums[1] + num), max(sums[1] + num, num)), nums[1:], (max(nums), nums[0]))
        return sums[0]
    
    def maxSubArray6(self, nums: List[int]) -> int:
      max_sum = current_sum = nums[0]
      
      for num in nums[1:]:
          if current_sum < num:
              current_sum = num
          current_sum += num
          if current_sum > max_sum:
              max_sum = current_sum
      
      return max_sum
  
    def maxSubArray7(self, nums: List[int]) -> int:
      max_sum = current_sum = nums[0]
      
      for num in nums[1:]:
          if current_sum < 0:
              current_sum = num
          else: current_sum += num
          if current_sum > max_sum:
              max_sum = current_sum
              
      return max_sum
  
    def maxSubArray8(self, nums: List[int]) -> int:
      max_sum = current_sum = nums[0]
      
      for num in nums[1:]:
          if current_sum + num < num:
              current_sum = num
          else: current_sum += num
          if current_sum > max_sum:
              max_sum = current_sum
              
      return max_sum 
      

    
import random
import time
def comparePerf():
    sol = Solution()
    total_time = 0
    total_time2 = 0
    total_time3 = 0
    total_time4 = 0
    total_time5 = 0
    total_time6 = 0
    total_time7 = 0
    total_time8 = 0
    for i in range(1000):
        nums = [random.randint(-1000, 1000) for _ in range(random.randint(1, 10000))]
        start = time.process_time()
        sol.maxSubArray(nums)
        end = time.process_time()
        total_time += end - start
        
        start = time.process_time()
        sol.maxSubArray2(nums)
        end = time.process_time()
        total_time2 += end - start
        
        start = time.process_time()
        sol.maxSubArray3(nums)
        end = time.process_time()
        total_time3 += end - start
        
        start = time.process_time()
        sol.maxSubArray4(nums)
        end = time.process_time()
        total_time4 += end - start
        
        start = time.process_time()
        sol.maxSubArray5(nums)
        end = time.process_time()
        total_time5 += end - start
        
        start = time.process_time()
        sol.maxSubArray6(nums)
        end = time.process_time()
        total_time6 += end - start
        
        start = time.process_time()
        sol.maxSubArray7(nums)
        end = time.process_time()
        total_time7 += end - start
        
        start = time.process_time()
        sol.maxSubArray8(nums)
        end = time.process_time()
        total_time8 += end - start
        
    print (f"Average of maxSubArray took {total_time/1000} seconds to run.")
    print (f"Average of maxSubArray2 took {total_time2/1000} seconds to run.")
    print (f"Average of maxSubArray3 took {total_time3/1000} seconds to run.")
    print (f"Average of maxSubArray4 took {total_time4/1000} seconds to run.")
    print (f"Average of maxSubArray5 took {total_time5/1000} seconds to run.")
    print (f"Average of maxSubArray6 took {total_time6/1000} seconds to run.")
    print (f"Average of maxSubArray7 took {total_time7/1000} seconds to run.")
    print (f"Average of maxSubArray8 took {total_time8/1000} seconds to run.")
            
comparePerf()

# Ave. for 1000 runs of nums.length <= 1000:
# 2 e-05 sec for function1
# 7-8 e-05 sec for function2
# 1.5 e-05 sec for function3
# 4.5-5 e-05 sec for function4
# 10-11 e-05 sec for function5
# function6 is 1% slower than function5
# function7 is 3-4% faster than function5
# function8 (interviewer's solution) = 2 e-05 sec


# Ave. for 1000 runs of nums.length <= 10000 took around 9 times as long.
# Average of maxSubArray took 0.00017761199999999993 seconds to run.
# Average of maxSubArray2 took 0.0007025039999999964 seconds to run.
# Average of maxSubArray3 took 0.00013555100000000505 seconds to run. !!!!
# Average of maxSubArray4 took 0.0004221879999999903 seconds to run.
# Average of maxSubArray5 took 0.0009809480000000123 seconds to run.
# Average of maxSubArray6 took 0.00013817699999999096 seconds to run.
# Average of maxSubArray7 took 0.0001361130000000016 seconds to run. ????
# Average of maxSubArray8 took 0.00018253600000000563 seconds to run.

