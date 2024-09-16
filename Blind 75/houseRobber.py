#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

class Solution:
    def rob(self, nums: List[int]) -> int:  # Longer than average time on LeetCode but consistently best 10% memory:
        length = len(nums)
        a = b = c = 0
        index = 0
        while index < length:
            c = max(nums[index] + a, b)
            a, b = b, c
            index += 1
        return c
      
    def robHashmap(self, nums: List[int]) -> int:  # Using a dict(hashMap) I almost always get best quartile time and worst quartile memory:
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        else:
            up_to_house = {0: nums[0], 1: max(nums[0], nums[1])}
        index = 2
        while index < length:
           up_to_house[index] = max(up_to_house[index - 1], up_to_house[index - 2] + nums[index])
           index += 1
        return up_to_house[length - 1]