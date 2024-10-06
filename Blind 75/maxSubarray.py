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

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      max_sum = max(nums)
      current_sum = nums[0]
      
      for num in nums[1:]:
          current_sum += num
          if current_sum > max_sum:
              max_sum = current_sum
          if current_sum < 0:
              current_sum = 0
      
      return max_sum
