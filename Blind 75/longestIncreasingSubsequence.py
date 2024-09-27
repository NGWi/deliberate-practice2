# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence.

# A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

# For example, "cat" is a subsequence of "crabt".

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
 
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
          up_to = [1] # len of LIS up to this index
          l_len = len(nums)
          for i in range(1, l_len):
            up_to.append(1) # minimum len of LIS - for just that num
            for j in range(0, i + 1):
              prev_len = up_to[j]
              if nums[j] < nums[i] and prev_len >= up_to[i]:
                up_to[i] = prev_len + 1
          
          lis_len = 0
          for i in range(0, l_len):
            i_len = up_to[i]
            if i_len >= lis_len:
              lis_len = i_len
          return lis_len
        
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
    def binaryPlacement(self, rankings: list, rankings_len: int, num: int) -> int:
        """
        Returns the index where num should be inserted in rankings. (subs_len - 1 ;))
        """
        left, max = 0, rankings_len
        while left < right:
            mid = (left + right) // 2 # Rounds down to stay within ranking's range.
            if rankings[mid] < num:
                left = mid + 1  # +1 is to avoid getting stuck always 1 less than right because of the rounding down
            else:
                right = mid
        return left

    def lengthOfLIS(self, nums: List[int]) -> int:
        rankings = [nums[0]] # Will contain lowest num so far that ends an LIS of length of this index + 1
        rankings_len = 1
        for num in nums[1:]:
            placement = self.binaryPlacement(rankings, rankings_len, num)
            if placement == rankings_len:
                rankings.append(num) # Add num as the longest yet
                rankings_len += 1
            else:
                rankings[placement] = num
        return rankings_len
      
    def lengthOfLIS(self, nums: List[int]) -> int:
        rankings = [nums[0]] # Alternative name: best_of_len_x. Will contain lowest num so far that ends an LIS of length of this index + 1
        rankings_len = 1
        for num in nums[1:]:
            placement, max = 0, rankings_len # Revving up a binary search for the correct placement of nums in rankings :-)
            while placement < max:           # Binary search loop.
                mid = (placement + max) // 2 # Rounds down to stay within ranking's range.
                if rankings[mid] < num:
                    placement = mid + 1 # +1 is to avoid getting stuck always 1 less than max because of the rounding down
                else:
                    max = mid                 
            if placement == rankings_len:
                rankings.append(num) # Add num as the end of the longest IS yet
                rankings_len += 1
            else:
                rankings[placement] = num
        return rankings_len