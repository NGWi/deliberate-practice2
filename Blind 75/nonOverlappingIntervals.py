# # Non-overlapping Intervals
# Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.

# Example 1:

# Input: intervals = [[1,2],[2,4],[1,4]]

# Output: 1
# Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.

# Example 2:

# Input: intervals = [[1,2],[2,4]]

# Output: 0
# Constraints:

# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# -50000 <= starti < endi <= 50000
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
      intervals.sort(key = lambda x: x[0])
      length = len(intervals)
      count = 0
      max_more_than = 1
      memo = []
      for i in range(length):
        memo.append(1)
        for j in range(i):
          i_start = intervals[i][0]
          j_end = intervals[j][1]
          if i_start >= j_end:
            more_than = memo[i]
            from_j = memo[j] + 1
            if from_j > more_than:
              memo[i] = from_j
              if more_than > max_more_than:
                max_more_than = from_j
      count = length - max_more_than     
      return count
    
    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        length = len(intervals)
        count = 0
        max_end = intervals[0][1]
        for i in range(1, length):
            interval = intervals[i]
            if interval[0] < max_end:
                count += 1
            else:
                max_end = interval[1]
        return count
      
    def eraseOverlapIntervals3(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        max_end = intervals[0][1]
        count = 0
        for interval in intervals[1:]:
            if interval[0] < max_end:
                count += 1
            else:
                max_end = interval[1]
        return count

import random
import timeit
def perfTest():
    s = Solution()
    loops = 1000
    n = 10000
    biggest_i = 50000
    methods = [s.eraseOverlapIntervals, s.eraseOverlapIntervals2, s.eraseOverlapIntervals3]
    times = [0, 0, 0 ]
    for _ in range(loops):
      intervals = [[random.randint(-biggest_i, biggest_i) for _ in range(2)] for _ in range(random.randint(1,n))]
      for i, method in enumerate(methods):
        times[i] += timeit.timeit(lambda: method(intervals), number=1)
    for t, method in zip(times, methods):
      print(method.__name__, end=' ')
      average = t/loops
      print(f"{average} seconds")
      
perfTest()

# 1000
# eraseOverlapIntervals 0.009028654706205999 seconds
# eraseOverlapIntervals2 6.313143305305857e-05 seconds
# eraseOverlapIntervals3 2.723811016767286e-05 seconds

