# Insert New Interval
# You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.

# You are given another interval newInterval = [start, end].

# Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

# Return intervals after adding newInterval.

# Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

# Example 1:

# Input: intervals = [[1,3],[4,6]], newInterval = [2,5]

# Output: [[1,6]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]

# Output: [[1,2],[3,5],[6,7],[9,10]]
# Constraints:

# 0 <= intervals.length <= 1000
# newInterval.length == intervals[i].length == 2
# 0 <= start <= end <= 1000
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]
        interval_i = len(intervals) - 1
        while interval_i >= 0:
          interval = intervals[interval_i]
          start_i = interval[0]
          end_i = interval[1]
          if new_start > end_i:
            intervals.insert(interval_i + 1, [new_start, new_end])
            return intervals
          if new_end < start_i:
            if interval_i == 0:
                break
            else:
                interval_i -= 1
                continue
          if new_start > start_i:
            new_start = start_i
          if new_end < end_i:
            new_end = end_i
          intervals.pop(interval_i)
          interval_i -= 1
        intervals.insert(0, [new_start, new_end])
        return intervals
      
    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        new_start = newInterval[0]
        new_end = newInterval[1]
        length = len(intervals)
        i = 0
        while i < length:
            interval_end = intervals[i][1]
        # Add all intervals that come before the 'newInterval'
            if interval_end < new_start:
              result.append(intervals[i])
              i += 1
              continue
        # Merge any overlapping intervals to the one 'newInterval'
            interval_start = intervals[i][0]
            if interval_start <= new_end:
              if new_start > interval_start:
                new_start = interval_start
              if new_end < interval_end:
                new_end = interval_end
              i += 1
              continue
        # Add either the 'newInterval' or
        # its union with any overlapping intervals
            result.append([new_start, new_end])
        # Add all the rest of the intervals
            result.extend(intervals[i:])
            return result
    # Add either the 'newInterval' or
    # its union with any overlapping intervals
        result.append([new_start, new_end])
        return result

#### Using merge function
    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
      # More efficient merge function here
      intervals.sort(key = lambda x: x[0])
      result = [intervals[0]]
      length = len(intervals)
      for i in range(1, length):
        interval = intervals[i]
        interval_start = interval[0]
        interval_end = interval[1]
        results_end = result[-1][1]
        if results_end >= interval_start:
          if results_end < interval_end:
            # Merge
            result[-1][1] = interval_end
        else: # The interval comes after
          result.append(interval)
      return result
    def insert3(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      # Merge overlapping intervals in the intervals list
      intervals = self.merge2(intervals)
      
      # Insert the newInterval into the merged list
      result = []
      new_start = newInterval[0]
      new_end = newInterval[1]
      length = len(intervals)
      i = 0
      while i < length:
          interval_end = intervals[i][1]
          # Add all intervals that come before the 'newInterval'
          if interval_end < new_start:
            result.append(intervals[i])
            i += 1
            continue
          # Add the newInterval
          result.append([new_start, new_end])
          # Add all the rest of the intervals
          result.extend(intervals[i:])
          break
      else:
          result.append([new_start, new_end])
      # Merge overlapping intervals in the result list
      return self.merge2(result)

    
    def merge3(self, intervals: List[List[int]]) -> List[List[int]]:
      result = [intervals[0]]
      length = len(intervals)
      for i in range(1, length):
        interval = intervals[i]
        interval_start = interval[0]
        interval_end = interval[1]
        results_end = result[-1][1]
        if results_end >= interval_start:
          if results_end < interval_end:
            # Merge
            result[-1][1] = interval_end
        else: # The interval comes after
          result.append(interval)
      return result    
    def insert4(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      # Find the correct position to insert the newInterval
      left, right = 0, len(intervals)
      start = newInterval[0]
      while left < right:
          mid = (left + right) // 2
          if intervals[mid][0] < start:
              left = mid + 1
          else:
              right = mid
      intervals.insert(left, newInterval)
      return self.merge3(intervals) 

    def merge4(self, intervals: List[List[int]]) -> List[List[int]]:
      result = [intervals[0]]
      for interval_start, interval_end in intervals[1:]:
        results_end = result[-1][1]
        if results_end >= interval_start:
          if results_end < interval_end:
            # Merge
            result[-1][1] = interval_end
        else: # The interval comes after
          result.append([interval_start, interval_end])
      return result    
    def insert5(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      # Find the correct position to insert the newInterval
      
      left, right = 0, len(intervals)
      start = newInterval[0]
      while left < right:
          mid = (left + right) // 2
          if intervals[mid][0] < start:
              left = mid + 1
          else:
              right = mid
      intervals.insert(left, newInterval)
      return self.merge4(intervals)  
    
    def comparePerf(self):
        """
        Compare the performance between the insert methods.
        """
        from timeit import timeit
        from random import randint
        
        n = 1000
        integers = 10000
        loops = 10000
        times = [0, 0, 0, 0, 0]
        methods = [self.insert, self.insert2, self.insert3, self.insert4, self.insert5]
        for _ in range(loops):
          intervals = [[randint(0, integers), randint(0, integers)] for _ in range(n)]
          intervals.sort()
          newInterval = [randint(0, integers), randint(0, integers)]
          for i, method in enumerate(methods):
              times[i] += timeit(lambda: method(intervals, newInterval), number=1)
        for t, method in zip(times, methods):
          print(method.__name__, end=' ')
          average = t/loops
          print(f"{average} seconds")            
if __name__ == '__main__':
    s = Solution()
    s.comparePerf()
    
# number size = 1000
# insert 1.691435812972486e-06 seconds
# insert2 7.072120771044866e-05 seconds
# insert3 0.00012078263610601425 seconds
# insert4 8.831768034724519e-05 seconds
# insert5 4.0851754252798855e-05 seconds

# numer size = 10000
# insert 1.4016175409778952e-06 seconds
# insert2 7.943631889065728e-05 seconds
# insert3 0.00012727607210399582 seconds
# insert4 8.527925226371736e-05 seconds
# insert5 4.8484498809557405e-05 seconds