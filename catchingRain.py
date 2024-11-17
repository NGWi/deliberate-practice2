"""
42. Trapping Rain Water
Solved
Hard
Topics
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
Seen this question in a real interview before?
1/5
Yes
No
Accepted
2.4M
Submissions
3.8M
Acceptance Rate
63.5%
"""
from typing import List


class Solution:
    # My first solution (O(3*n)):
    def trap(self, height: List[int]) -> int:
        width = len(height)
        memo = [[0, 0, 0] for w in range(width)]

        highest_l = highest_r = 0
        from_l = 0
        from_r = width - 1
        for h1, h2 in zip(height, reversed(height)):
            print(from_l, from_r)
            if h1 > highest_l:
                highest_l = h1
            if h2 > highest_r:
                highest_r = h2

            memo[from_l][0] = highest_l
            memo[from_l][1] = h1
            memo[from_r][2] = highest_r

            from_l += 1
            from_r -= 1

        total_water = 0
        for record in memo:
            print(record)
            water_height = min(record[0], record[2])
            water = water_height - record[1]
            total_water += water

        return (total_water)

    # My second, faster runtime (O(2*n)), solution:
    def trap2(self, height: List[int]) -> int:
        width = len(height)
        memo = [[0, 0] for w in range(width)]
        highest_l = highest_r = 0

        for h, record in zip(height, memo):
            if h > highest_l:
                highest_l = h
            record[0] = highest_l
            record[1] = h

        total_water = 0
        for i in range(width - 1, -1, -1):
            record = memo[i]
            h = record[1]
            if h > highest_r:
                highest_r = h

            elevation = record[0]
            if elevation > highest_r:
                elevation = highest_r
            water = elevation - record[1]
            total_water += water

        return (total_water)
