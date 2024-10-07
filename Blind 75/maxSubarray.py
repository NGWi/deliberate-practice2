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
    def maxSubArray2a(self, nums: List[int]) -> int:
      max_sum = current_sum = nums[0]
      
      for num in nums[1:]:
          current_sum = max(num, current_sum + num)
          max_sum = max(max_sum, current_sum)
      
      return max_sum

    def maxSubArray2b(self, nums: List[int]) -> int:
      max_sum = current_sum = nums[0]
      
      for num in nums[1:]:
          current_sum = max(num, current_sum + num)
          if current_sum > max_sum:
              max_sum = current_sum
      return max_sum
  
    def maxSubArray2c(self, nums: List[int]) -> int:
      max_sum = current_sum = nums[0]
      
      for num in nums[1:]:
          current_sum = max(num, current_sum + num)
          max_sum = max(current_sum, max_sum)
      
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
    total_time2a = 0
    total_time2b = 0
    total_time2c = 0
    total_time3 = 0
    total_time4 = 0
    total_time5 = 0
    total_time6 = 0
    total_time7 = 0
    total_time8 = 0
    iterations = 10000
    for i in range(iterations):
        nums = [random.randint(-1000, 1000) for _ in range(random.randint(1, 10000))]
        start = time.process_time()
        sol.maxSubArray(nums)
        end = time.process_time()
        total_time += end - start
        
        start = time.process_time()
        sol.maxSubArray2a(nums)
        end = time.process_time()
        total_time2a += end - start
        
        start = time.process_time()
        sol.maxSubArray2b(nums)
        end = time.process_time()
        total_time2b += end - start
        
        start = time.process_time()
        sol.maxSubArray2c(nums)
        end = time.process_time()
        total_time2c += end - start
        
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
        
    print (f"Average of maxSubArray took {total_time/iterations} seconds to run.")
    print (f"Average of maxSubArray2a took {total_time2a/iterations} seconds to run.")
    print (f"Average of maxSubArray2b took {total_time2b/iterations} seconds to run.")
    print (f"Average of maxSubArray2c took {total_time2c/iterations} seconds to run.")
    print (f"Average of maxSubArray3 took {total_time3/iterations} seconds to run.")
    print (f"Average of maxSubArray4 took {total_time4/iterations} seconds to run.")
    print (f"Average of maxSubArray5 took {total_time5/iterations} seconds to run.")
    print (f"Average of maxSubArray6 took {total_time6/iterations} seconds to run.")
    print (f"Average of maxSubArray7 took {total_time7/iterations} seconds to run.")
    print (f"Average of maxSubArray8 took {total_time8/iterations} seconds to run.")
            
comparePerf()

# Ave. for 1000 runs of nums.length <= 1000:
# 2 e-05 sec for function1
# 7-8 e-05 sec for function2a
# 1.5 e-05 sec for function3
# 4.5-5 e-05 sec for function4
# 10-11 e-05 sec for function5
# function6 is 1% slower than function5
# function7 is 3-4% faster than function5
# function8 (interviewer's solution) = 2 e-05 sec


# Ave. for 1000 runs of nums.length <= 10000 took around 9 times as long.
# Average of maxSubArray took 0.0001860785999999955 seconds to run.
# Average of maxSubArray2a took 0.0007462492000000246 seconds to run.
# Average of maxSubArray2b took 0.00043617429999999365 seconds to run.
# Average of maxSubArray2c took 0.0007407634000000413 seconds to run.
# Average of maxSubArray3 took 0.00014317699999995585 seconds to run.
# Average of maxSubArray4 took 0.000445313399999978 seconds to run.
# Average of maxSubArray5 took 0.0010340596999999971 seconds to run.
# Average of maxSubArray6 took 0.000146263699999996 seconds to run.
# Average of maxSubArray7 took 0.00014279200000002568 seconds to run.
# Average of maxSubArray8 took 0.00019248230000002109 seconds to run.

