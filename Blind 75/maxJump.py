# Jump Game
# You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

# Return true if you can reach the last index starting from index 0, or false otherwise.

# Example 1:

# Input: nums = [1,2,0,1,0]

# Output: true
# Explanation: First jump from index 0 to 1, then from index 1 to 3, and lastly from index 3 to 4.

# Example 2:

# Input: nums = [1,2,1,0,1]

# Output: false
# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
      last_i = len(nums) - 1
      max_index = 0
      index = 0
      while max_index < last_i:
        num = nums[index]
        max_index = max(max_index, index + num)
        if max_index == index:
          return False
        index += 1
      return True
    def canJump2(self, nums: List[int]) -> bool:
      last_i = len(nums) - 1
      max_index = 0
      index = 0
      while max_index < last_i:
        num = nums[index]
        max_index = max(index + num, max_index)
        if max_index == index:
          return False
        index += 1
      return True    
    def canJump3(self, nums: List[int]) -> bool:
      max_index = 0
      for index, num in enumerate(nums):
        if index > max_index:
          return False
        max_index = max(max_index, index + num)
      return True
    
import random
import time
def performanceTest():
    s = Solution()
    time_jump = 0
    time_jump2 = 0
    time_jump3 = 0
    for i in range(10000):
        nums = [random.randint(0, 1000) for _ in range(random.randint(0, 10000))]
        start = time.time()
        s.canJump(nums)
        end = time.time()
        time_jump += end - start
        
        start = time.time()
        s.canJump2(nums)
        end = time.time()
        time_jump2 += end - start
        
        start = time.time()
        s.canJump3(nums)
        end = time.time()
        time_jump3 += end - start
        
    print (f"Average of canJump took {time_jump/1000} seconds to run.")
    print (f"Average of canJump2 took {time_jump2/1000} seconds to run.")
    print (f"Average of canJump3 took {time_jump3/1000} seconds to run.")
    

if __name__ == "__main__":
    performanceTest()
    
# Average of canJump took 0.004467843532562256 seconds to run.
# Average of canJump2 took 0.004453927755355835 seconds to run.
# Average of canJump3 took 0.004969877243041992 seconds to run.
        
