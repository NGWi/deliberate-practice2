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
    def canJump4(self, nums: List[int]) -> bool:
      last_i = len(nums) - 1
      max_index = 0
      index = 0
      while max_index < last_i:
        num = nums[index]
        from_here = index + num
        if from_here > max_index:
          max_index = from_here
        if max_index == index:
          return False
        index += 1
      return True
    
import random
import time
def performanceTest():
    s = Solution()
    time_jump = 0
    time_jump2 = 0
    time_jump3 = 0
    time_jump4 = 0
    times = 10000
    for i in range(times):
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
        
        start = time.time()
        s.canJump4(nums)
        end = time.time()
        time_jump4 += end - start
        
    print (f"canJump took average of {time_jump/times} seconds to run.")
    print (f"canJump2 took average of {time_jump2/times} seconds to run.")
    print (f"canJump3 took average of {time_jump3/times} seconds to run.")
    print (f"canJump4 took average of {time_jump4/times} seconds to run.")
    

if __name__ == "__main__":
    performanceTest()

# 100000 runs (computer started to overheat)
# canJump took average of 0.0005017874693870545 seconds to run.
# canJump2 took average of 0.0005050669622421265 seconds to run.
# canJump3 took average of 0.0005683367085456848 seconds to run.
# canJump4 took average of 0.00021681216478347778 seconds to run.
        
