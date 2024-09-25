# # Maximum Product Subarray
# Given an integer array nums, find a subarray that has the largest product within the array and return it.

# A subarray is a contiguous non-empty sequence of elements within an array.

# You can assume the output will fit into a 32-bit integer.

# Example 1:

# Input: nums = [1,2,-3,4]

# Output: 4
# Example 2:

# Input: nums = [-2,-1]

# Output: 2
# Constraints:

# 1 <= nums.length <= 1000
# -10 <= nums[i] <= 10

leet_test_184 = [-3,2,-2,1,-1,0,-3,-1]
class Solution:
    # Fails for leet_test_184
    # def countNegatives(self, nums: List[int]) -> int:
    #     count = 0
    #     for i in range(len(nums)):
    #         if nums[i] < 0:
    #             count += 1
    #     return count
    # def negsAllowed(self, total_negs: int) -> int:
    #     negs_to_skip = total_negs % 2
    #     return total_negs - negs_to_skip    
    # def subarray(self, nums: List[int], index: int, negs_allowed: int) -> int:
    #     product = None
    #     for j in range(index, len(nums)):
    #         num = nums[j]
    #         print("Num:", num)
    #         if num < 0:
    #             if negs_allowed == 0:
    #                 print(product)
    #                 return product if product is not None else num
    #             else:
    #                 product = num if product is None else product * num
    #                 negs_allowed -= 1
    #         elif num == 0:
    #             print(product)
    #             return product if product is not None else num
    #         else:
    #             product = num if product is None else product * num
    #     print(product)
    #     return product
      
    # def maxProduct(self, nums: List[int]) -> int:
    #     max_product = max(nums)
    #     total_negs = self.countNegatives(nums)
    #     negs_allowed = self.negsAllowed(total_negs)
    #     for i in range(len(nums)):
    #         print("Starting index:", i)
    #         print("Negs allowed:", negs_allowed)
    #         product = self.subarray(nums, i, negs_allowed)
    #         if product > max_product:
    #             max_product = product
    #         if nums[i] < 0:
    #             total_negs -= 1
    #             negs_allowed = self.negsAllowed(total_negs)
    #     return max_product
    
        # Times out on huge Lists    
    # def negsAllowed(self, total_negs: int) -> int:
    #     negs_to_skip = total_negs % 2
    #     return total_negs - negs_to_skip
    
    # def compare(self, max_product: int, product: int) -> int:
    #     if product and product > max_product:
    #         max_product = product
    #     return max_product
         
    # def subarray(self, nums: List[int], max_product: int, start_index: int, negs_allowed: int) -> int:
    #     product = None
    #     for num in nums[start_index:]:
    #         if num < 0:
    #             if negs_allowed == 0:
    #                 return self.compare(max_product, product)
    #             else:
    #                 product = product * num if product else num
    #                 negs_allowed -= 1
    #         elif num == 0:
    #             return self.compare(max_product, product)
    #         else:
    #             product = product * num if product else num
    #         max_product = self.compare(max_product, product)
    #     return max_product
       
    # def maxProduct(self, nums: List[int]) -> int:
    #     max_product = max(nums)
    #     total_negs = sum(1 for num in nums if num < 0)
    #     negs_allowed = self.negsAllowed(total_negs)
    #     for i in range(len(nums)):
    #         max_product = self.subarray(nums, max_product, i, negs_allowed)
    #         if nums[i] < 0:
    #             total_negs -= 1
    #             negs_allowed = self.negsAllowed(total_negs)
    #     return max_product
      
      # Passes LeetCode with best quartile time but worst quartile memory
    def maxProduct(self, nums: List[int]) -> int:
        temp_max = temp_min = nums[0]
        ultimate_max = max(nums)
        
        for num in nums[1:]:
            temp_max, temp_min = temp_max * num, temp_min * num
            if num < 0: temp_max, temp_min = temp_min, temp_max
            temp_max = max(temp_max, num)
            temp_min = min(temp_min, num)
            if temp_max > ultimate_max: ultimate_max = temp_max
            
        return ultimate_max
      
      # Trying to eliminate poitless iterations, but still buggy
    # def maxProduct(self, nums: List[int]) -> int:
    #     temp_max = temp_min = nums[0]
    #     ultimate_max = max(nums)
    #     total_negs = sum(1 for num in nums if num < 0)
    #     even_negs_left = total_negs % 2 == 0
        
    #     for num in nums[1:]:
    #         print(num)
    #         if num >= 0 or even_negs_left: 
    #             if num < 0:
    #                 temp_max, temp_min = temp_min, temp_max
    #                 even_negs_left = not even_negs_left
    #             temp_max = max(temp_max * num, num)
    #             temp_min = min(temp_min * num, num)
    #         else: temp_max, temp_min = 0, 0


    #         if temp_max > ultimate_max: ultimate_max = temp_max
    #         print(temp_max, temp_min, ultimate_max)
            
    #     return ultimate_max
      
      # Favorite working solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp_max = temp_min = nums[0]
        ultimate_max = max(nums)
        
        for num in nums[1:]:
            if num < 0:
                temp_max, temp_min = temp_min, temp_max
            
            temp_max = max(num, temp_max * num)
            temp_min = min(num, temp_min * num)
            
            if temp_max > ultimate_max:
                ultimate_max = temp_max
        
        return ultimate_max
      
    def maxProduct(self, nums: List[int]) -> int:
        temp_max = temp_min = ultimate_max = nums[0]
        
        for num in nums[1:]:
            temp_max, temp_min = temp_max * num, temp_min * num
            temp_max, temp_min = max(num, temp_max, temp_min), min(num, temp_max, temp_min)
            
            ultimate_max = max(ultimate_max, temp_max)
        
        return ultimate_max
      
    def maxProduct(self, nums: List[int]) -> int:
        temp_max = temp_min = nums[0]
        ultimate_max = max(nums)

        for num in nums[1:]:
            temp_max, temp_min = temp_max * num, temp_min * num
            temp_max, temp_min = max(num, temp_max, temp_min), min(num, temp_max, temp_min)
            
            ultimate_max = max(ultimate_max, temp_max)
        
        return ultimate_max
      
    def maxProduct(self, nums: List[int]) -> int:
        temp_max = temp_min = ultimate_max = nums[0]
        for num in nums[1:]:
            temp_max, temp_min = max(num, temp_max * num, temp_min * num), min(num, temp_max * num, temp_min * num)
            ultimate_max = max(ultimate_max, temp_max)
        return ultimate_max
    def maxProduct(self, nums: List[int]) -> int:
        temp_max = temp_min = ultimate_max = nums[0]
        for num in nums[1:]: temp_max, temp_min = max(num, (mx := temp_max * num), (mn := temp_min * num)), min(num, mx, mn); ultimate_max = max(ultimate_max, temp_max)
        return ultimate_max
    
    def maxProduct(self, nums: List[int]) -> int:
      temp_max = temp_min = ultimate_max = nums[0]
      for num in nums[1:]: temp_min, _, temp_max = sorted([num, temp_max * num, temp_min * num]); ultimate_max = max(ultimate_max, temp_max)
      return ultimate_max
    
    def maxProduct(self, nums: List[int]) -> int:
        temp_max = temp_min = nums[0]
        ultimate_max = max(nums)
        
        for num in nums[1:]:
            if num < 0:
                temp_max, temp_min = temp_min, temp_max
            elif num == 0:
                temp_max, temp_min = 0, 0
                continue

            temp_max = max(num, temp_max * num)
            temp_min = min(num, temp_min * num)
                
            if temp_max > ultimate_max:
                ultimate_max = temp_max
        
        return ultimate_max
      
      
leet_test_184 = [-3,2,-2,1,-1,0,-3,-1]
        
        